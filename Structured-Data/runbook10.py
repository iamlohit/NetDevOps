from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def test_this(task):
    version_results = task.run(task=netmiko_send_command, command_string="show version", use_textfsm=True)
    structured_output = version_results.result
    print(structured_output)

results = nr.run(task=test_this)
# print_result(results)
