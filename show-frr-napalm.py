import ipdb
from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import napalm_cli

def show_frr(task):

    cmds = ["show isis segment-routing prefix-segments", "show isis segment-routing adjacency-segments",\
            "show isis interface","show isis ti-lfa path","show isis ti-lfa tunnel",\
            "show isis segment-routing tunnel","show tunnel fib",\
            "show mpls lfib route","show ip route"]

    result = task.run(task=napalm_cli, commands=cmds)

def main():
    nr = InitNornir(config_file="nornir.yaml")
    lab = nr.filter(F(groups__contains="ti_lfa"))
    aggresult = lab.run(task=show_frr)
    print_result(aggresult)

if __name__ == "__main__":
    main()
