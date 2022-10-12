from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_http.tasks import http_method

nr = InitNornir(config_file="config.yaml")

headers = {"Accept": "application/yang-data+json"}

def test_restconf(task):
    task.run(
        task=http_method,
        method="get",
        verify=False,
        auth=(f"{task.host.username}", f"{task.host.password}"),
        headers=headers,
        url=f"https://{task.host.hostname}:443/restconf/data/native/router" 
    )

results = nr.run(task=test_restconf)
print_result(results)
