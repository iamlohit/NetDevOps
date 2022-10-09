from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
# import ipdb

nr = InitNornir(config_file="config.yaml")

def pull_structured_data(task):
    version_result = task.run(task=send_command, command="show version")
    task.host["facts"] = version_result.scrapli_response.genie_parse_output()
    uptime = task.host["facts"]["version"]["uptime"]
    print(f"{task.host} has an uptime of {uptime}")

results = nr.run(task=pull_structured_data)
# print_result(results)
# ipdb.set_trace()
