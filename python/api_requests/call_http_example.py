

import requests

url = "https://my-azure-http-example-function.azurewebsites.net/api/HttpExample"

querystring = {"name":"Dave"}

response = requests.request("GET", url, params=querystring)

print(response.text)