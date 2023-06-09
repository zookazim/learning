
import sys
import requests

url = "http://localhost:7071/api/AzFnProjSqlGenerator"

querystring = sys.stdin.readlines()

response = requests.request("GET", url, params=querystring)

print(response.text)
print("Response code:{}".format(response.status_code))


