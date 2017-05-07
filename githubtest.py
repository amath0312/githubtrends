import urllib.request
import json

url = 'https://api.github.com/search/repositories?q=stars:">10"+pushed:>2017-05-05&sort=stars&order=desc&page=1&per_page=5'
url = 'https://api.github.com/search/repositories?q=stars:">10"+created:>2017-05-05&sort=stars&order=desc&page=1&per_page=5'
response = urllib.request.urlopen(url).read().decode('utf-8')
data = json.loads(response)
print(data['total_count'])
print(response)
for item in data['items']:
  print(item['full_name']+': '+item['url']+', star='+str(item['stargazers_count'])+','+item['created_at'])