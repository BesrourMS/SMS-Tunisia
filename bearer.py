import requests

url = "https://api.orange.com/oauth/v3/token"

payload = "grant_type=client_credentials"
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "insomnia/2023.5.8",
    "Authorization": "Basic "
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
