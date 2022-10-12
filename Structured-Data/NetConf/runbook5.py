from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_http.tasks import http_method
import json
# import ipdb

nr = InitNornir(config_file="config.yaml")

headers = {"Accept": "application/yang-data+json"}

def test_restconf(task):
    response = task.run(
        task=http_method,
        method="get",
        verify=False,
        auth=(f"{task.host.username}", f"{task.host.password}"),
        headers=headers,
        url=f"https://{task.host.hostname}:443/restconf/data/native/router" 
    )
    task.host["facts"] = json.loads(response.result)
    ospf_rid = task.host["facts"]["Cisco-IOS-XE-native:router"]["Cisco-IOS-XE-ospf:router-ospf"]["ospf"]["process-id"][0]["router-id"]
    print(f"{task.host} OSPF RID is {ospf_rid}")

results = nr.run(task=test_restconf)
# print_result(results)
# ipdb.set_trace()