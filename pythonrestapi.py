import requests
import sys

# allow self signed
requests.packages.urllib3.disable_warnings()

# credentials
USER = 'developer'
PASS = 'C1sco12345'

# URL for GET Request
url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces"

# set yang+json as the data format
headers = {'Content-Type': 'application/yang-data+json',
            'Accept': 'application/yang-data+json'}

# Run GET
response = requests.get(url, auth=(USER, PASS),
                        headers=headers, verify=False)


print(response.text)
