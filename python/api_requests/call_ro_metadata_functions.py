
import sys
import requests
import json

#url = "http://localhost:7071/api/SqlGenerator"

url = "https://rosqlgenerator.azurewebsites.net/api/RoSqlGenerator"

input_lines_list = sys.stdin.readlines()
querystring = ''.join(input_lines_list)

response = requests.request("GET", url, data=querystring)

print(response.text)
print("Response code:{}".format(response.status_code))

proj_sql = data = json.loads(response.text)
