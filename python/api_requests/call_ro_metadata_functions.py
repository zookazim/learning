

import requests

url = "http://localhost:7071/api/AzFnProjSqlGenerator"

querystring = {"name":"Dave"}

response = requests.request("GET", url, params=querystring)

print(response.text)
print("Response code:{}".format(response.status_code))

