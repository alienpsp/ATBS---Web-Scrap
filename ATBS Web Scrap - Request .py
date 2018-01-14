import requests
res = requests.get('http://automatetheboringstuff.com/files/rj.txt')
# res.raise_for_status() # to check if link is ok in shell

print('The article is ' + str(len(res.text)) + ' words long.')

print(res.text[:500])

