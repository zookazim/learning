
import sys
import requests
import json

#url = "http://localhost:7071/api/SqlGenerator"

url = "https://azfnprojmetadata.azurewebsites.net/SqlGenerator"

input_lines_list = sys.stdin.readlines()
querystring = ''.join(input_lines_list)

response = requests.request("GET", url, data=querystring)

print(response.text)
print("Response code:{}".format(response.status_code))


