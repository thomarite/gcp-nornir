import ipdb
from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import netmiko_send_command

def show_frr(task):

    cmds = ["show isis segment-routing prefix-segments", "show isis segment-routing adjacency-segments",\
            "show isis interface","show isis ti-lfa path","show isis ti-lfa tunnel",\
            "show isis segment-routing tunnel","show tunnel fib",\
            "show mpls lfib route","show ip route"]

    for cmd in cmds:
        result = task.run(task=netmiko_send_command, command_string=cmd)
    #print_result(result)

def main():
    nr = InitNornir(config_file="nornir.yaml")
    lab = nr.filter(F(groups__contains="ti_lfa"))
    aggresult = lab.run(task=show_frr)
    print_result(aggresult)

if __name__ == "__main__":
    main()
