from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
import ipdb

nr = InitNornir(config_file="config.yaml")

def pull_structured_data(task):
    interface_result = task.run(task=send_command, command="show ip interface")
    task.host["facts"] = interface_result.scrapli_response.genie_parse_output()

results = nr.run(task=pull_structured_data)
# print_result(results)
ipdb.set_trace()