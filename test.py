import requests,json


requests.packages.urllib3.disable_warnings()

scale_url = 'https://10.0.50.155/scalemgmt/v2/nodes'
header = {'content-type': 'application/json', 'accept': 'application/json'}

test = requests.get(scale_url, headers=header, auth=('admin', 'admin001'), verify=False)

print(test.text)
