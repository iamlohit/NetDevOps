from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
import getpass

nr = InitNornir(config_file="config.yaml")

def credential_test(task):
    task.run(task=send_command, command="show ip int brief")

default_password = getpass.getpass("Enter Cisco Default Password: ")
nr.inventory.defaults.password = default_password

results = nr.run(task=credential_test)
print_result(results)