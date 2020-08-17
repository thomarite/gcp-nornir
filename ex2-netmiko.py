import ipdb
from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result

def my_task(task):
    print(task.host.hostname)
    return f"This is a nornir task exec in {task.host.hostname}"

def main():
    nr = InitNornir(config_file="nornir.yaml")
    aggresult = nr.run(task=netmiko_send_command, command_string="show ip interface brief")
    print_result(aggresult)
    #print()
    #for k,v in aggresult.items():
    #    print("-" * 50)
    #    print(k)
    #    print(v[0].result)
    #    print("-" * 50)
    #ipdb.set_trace()
    #print()

if __name__ == "__main__":
    main()
