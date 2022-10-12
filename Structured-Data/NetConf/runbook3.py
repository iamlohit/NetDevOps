from nornir import InitNornir
from nornir_scrapli.tasks import netconf_get_config
from nornir_utils.plugins.functions import print_result
import xmltodict
import ipdb

nr = InitNornir(config_file="config.yaml")

def pull_netconf_data(task):
    result = task.run(task=netconf_get_config, source="running", filter_="/native/router/ospf/router-id", filter_type="xpath")
    task.host["facts"] = xmltodict.parse(result.result)
    ospf_rid = task.host["facts"]["rpc-reply"]["data"]["native"]["router"]["ospf"]["router-id"]
    print(f"{task.host} has an OSPF router-id of {ospf_rid}")

results = nr.run(task=pull_netconf_data)
# print_result(results)
# ipdb.set_trace()

