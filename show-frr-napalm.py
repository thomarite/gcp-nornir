import ipdb
import argparse
from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import napalm_cli


_version = '0.0.1'

def parse_args():
    parser = argparse.ArgumentParser(description="FRR TI-LFA show commands")
    parser.add_argument(
        '-f', '--file', help='save output to file', nargs='?', default=None, const='output-show-frr-napalm.txt')
    parser.add_argument(
        '-v', '--version', action='version', version='%(prog)s (version {})'.format( _version))
    args = parser.parse_args()
    return args

def show_frr(task):

    cmds = ["show isis segment-routing prefix-segments", "show isis segment-routing adjacency-segments",\
            "show isis interface","show isis ti-lfa path","show isis ti-lfa tunnel",\
            "show isis segment-routing tunnel","show tunnel fib",\
            "show mpls lfib route","show ip route"]

    result = task.run(task=napalm_cli, commands=cmds)

def main():
    args = parse_args()

    nr = InitNornir(config_file="nornir.yaml")
    lab = nr.filter(F(groups__contains="ti_lfa"))
    aggresult = lab.run(task=show_frr)
    device_line = ""
    #ipdb.set_trace()
    for device in aggresult.keys():
        print("/"*80)
        print("///"+" "*74+"///")
        device_line = "Device: %s" % device
        print("///" + device_line.center(74,' ') + "///")
        print("///"+" "*74+"///")
        print("/"*80)
        print()
        for command in aggresult[device][1].result.keys():
            print("command = %s" % command)
            print()
            print(aggresult[device][1].result[command])
            print()
            print("="*80)
            print()
        print()

    if args.file:
        f = open(args.file, "w")
        for device in aggresult.keys():
            f.write("/"*80 + "\n")
            f.write("///"+" "*74+"///\n")
            device_line = "Device: %s" % device
            f.write("///" + device_line.center(74,' ') + "///\n")
            f.write("///"+" "*74+"///\n")
            f.write("/"*80 + "\n")
            f.write("\n")
            for command in aggresult[device][1].result.keys():
                f.write("command = %s\n" % command)
                f.write("\n")
                f.write(aggresult[device][1].result[command])
                f.write("\n")
                f.write("="*80 + "\n")
                f.write("\n")
            f.write("\n")
        f.close()

if __name__ == "__main__":
    main()
