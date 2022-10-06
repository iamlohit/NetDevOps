# from distutils.command.config import config
from distutils.command.config import config
from nornir import InitNornir
from nornir_scrapli.tasks import send_configs_from_file
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

results = nr.run(task=send_configs_from_file, file="configcommands.txt")
print_result(results)
