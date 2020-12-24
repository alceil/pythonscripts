import requests
data = requests.get('https://api.rootnet.in/covid19-in/stats/latest').json()
length = len(data['data']['regional'])
print(length)