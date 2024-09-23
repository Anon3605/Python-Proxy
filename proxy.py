import requests

# responses = requests.get('https://ipinfo.io/json')
proxies = {
    'http': 'http://38.51.232.18:8080',
    'https': 'http://38.51.232.18:8080'
}
responses = requests.get('https://ipinfo.io/json', proxies=proxies, timeout=10)

print(responses)
print(responses.text)