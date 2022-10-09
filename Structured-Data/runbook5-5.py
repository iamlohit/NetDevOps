from imaplib import Commands
from nornir import InitNornir
from nornir_scrapli.tasks import send_configs_from_file
from nornir_utils.plugins.functions import print_result


nr = InitNornir(config_file="config.yaml")

def ospf_bootstrapping(task):
    version_result = task.run(task=send_configs_from_file, file="ospf-config.txt")

results = nr.run(task=ospf_bootstrapping)
print_result(results)
