import requests

url = "http://172.16.1.87:80/ins"

payload="{\n  \"ins_api\": {\n    \"version\": \"1.0\",\n    \"type\": \"cli_show\",\n    \"chunk\": \"0\",\n    \"sid\": \"sid\",\n    \"input\": \"sh ip int br\",\n    \"output_format\": \"json\"\n  }\n}"
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic YW50b25pbzphZG1pbg=='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
