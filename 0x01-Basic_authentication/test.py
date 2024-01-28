from requests.auth import HTTPBasicAuth
import requests
import base64

coding = "Hello World"

coded = base64.b64encode(coding.encode('utf-8')).decode('utf-8')

print(coded)


url = "https://example.com/api/resource"
username = "your_username"
password = "your_password"

response = requests.get(url, auth=HTTPBasicAuth(username, password))

print(response.text)
