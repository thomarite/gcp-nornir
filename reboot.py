import ipdb
import sys
from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result

def continue_func(msg="Do you want to continue (y/n)? "):
    response = input(msg).lower()
    if 'y' in response:
        return True
    else:
        sys.exit()

def main():
    nr = InitNornir(config_file="nornir.yaml")
    #lab = nr.filter(name="l1r2")
    lab = nr.filter(F(groups__contains="ti_lfa"))
    print("lab = ",lab.inventory.hosts.keys())

    # Save the config
    print("\nSave Config:\n")
    result = lab.run(
        task=netmiko_send_command,
        command_string="write mem",
    )
    print_result(result)

    # Reload - This is a very slow commands - had to global_delay_factor: 5 in netmiko params
    continue_func(msg="Do you want to reload the device (y/n)? ")
    result = lab.run(
        task=netmiko_send_command,
        use_timing=True,
        command_string="reload",
    )
    #ipdb.set_trace()
    print("\nReload command:\n")
    print_result(result)

    # Confirm the reload (if 'confirm' is in the output)
    reload = True
    for device_name, multi_result in result.items():
        if not ('confirm' in multi_result[0].result):
            reload = False
            print("device %s is not ready to be reloaded" % device_name)
            print(multi_result[0].result)

    if reload:
        result = lab.run(
            task=netmiko_send_command,
            use_timing=True,
            command_string="y",
        )
        print_result(result)


if __name__ == "__main__":
    main()
