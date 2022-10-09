from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
import getpass

nr = InitNornir(config_file="config.yaml")

south_password = getpass.getpass("Enter South Group Password: ")
north_password = getpass.getpass("Enter North Group Password: ")
r7_password = getpass.getpass("Enter R7 Password: ")

nr.inventory.groups["south"].password = south_password
nr.inventory.groups["north"].password = north_password
nr.inventory.hosts["vIOS7"].password = r7_password

def credential_test(task):
    task.run(task=send_command, command="show ip int brief")

results = nr.run(task=credential_test)
print_result(results)