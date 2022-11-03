import requests
response = requests.get("https://raw.githubusercontent.com/idris110/dwm/main/naive.py").text
print(response)