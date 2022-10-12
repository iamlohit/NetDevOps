from nornir import InitNornir
from nornir_scrapli.tasks import send_configs
from nornir_utils.plugins.functions import print_result
from nornir_jinja2.plugins.tasks import template_file
from nornir_utils.plugins.tasks.data import load_yaml

nr = InitNornir(config_file="config.yaml")

def load_config_data(task):
    data = task.run(task=load_yaml, file=f"./config_data/{task.host}.yaml")
    task.host["facts"] = data.result
    test_templates(task)


def test_templates(task):
    template = task.run(task=template_file, template="bgp.j2", path="templates")
    task.host["bgp_config"] = template.result
    rendered = task.host["bgp_config"]
    configuration = rendered.splitlines()
    task.run(task=send_configs, configs=configuration)

results = nr.run(task=load_config_data)
print_result(results)
