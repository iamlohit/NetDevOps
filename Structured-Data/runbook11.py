from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_scrapli.functions import print_structured_result
from nornir_utils.plugins.functions import print_result
import ipdb

nr = InitNornir(config_file="config.yaml")

def test_this(task):
    interfaces_result = task.run(task=send_command, command="show ip interface")
    # structured_data = task.host["facts"] = interfaces_result.scrapli_response.genie_parse_output()



results = nr.run(task=test_this)
# print_structured_result(results)
# print_structured_result(results, parser="genie")
print_structured_result(results, parser="textfsm")
# ipdb.set_trace()
