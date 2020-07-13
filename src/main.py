import requests

URL = "https://robertturff.pythonanywhere.com/management/ip"

file = open("../settings.txt", "r")
ApiKey = "Api-Key "
ApiKey += file.readline()
file.close()

headers = {"Authorization" : str(ApiKey)}
response = requests.post(url=URL, json={"title": "pivpn"}, headers=headers)

print("Status code: ", response.status_code)
print("Printing Entire Post Request")
print(response.text)
