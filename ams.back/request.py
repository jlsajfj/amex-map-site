import requests

url = "https://bdaas.americanexpress.com/api/servicing/v1/maps"

querystring = {"recent_active_indicator":"false","lat_lng":"40.7579747,-73.9855426","page_size":"100"}

payload = ""
headers = {}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)