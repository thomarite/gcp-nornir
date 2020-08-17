import ipdb
from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import napalm_configure

def isis_core_config(task):
    index = task.host.name.split("l1r")[1]
    isis_net = "000" + index
    exceed = len(isis_net) - 4
    isis_net = isis_net[exceed:]
    isis_core = \
    "interface Loopback1\n\
     description CORE Loopback\n\
     ip address 10.0.0.{index}/32\n\
     node-segment ipv4 index {index}\n\
     isis enable CORE\n\
     isis metric 1\n\
    router isis CORE\n\
     net 49.0000.0001.0010.0000.0000.{isis_net}.00\n\
     is-type level-2\n\
     log-adjacency-changes\n\
     timers local-convergence-delay protected-prefixes\n\
     set-overload-bit on-startup wait-for-bgp\n\
     address-family ipv4 unicast\n\
      bfd all-interfaces\n\
      fast-reroute ti-lfa mode node-protection\n\
     segment-routing mpls\n\
      router-id 10.0.0.{index}\n\
      adjacency-segment allocation sr-peers backup-eligible\n\
      no shutdown\n".format(index=index, isis_net=isis_net)
    result = task.run(task=napalm_configure, configuration=isis_core)
    #print_result(result)

def main():
    nr = InitNornir(config_file="nornir.yaml")
    lab = nr.filter(F(groups__contains="ti_lfa"))
    aggresult = lab.run(task=isis_core_config)
    print_result(aggresult)

if __name__ == "__main__":
    main()
