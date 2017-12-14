import requests
from lxml import html
president = requests.get('https://twitter.com/EmmanuelMacron?lang=fr')
print(president)
tree = html.fromstring(president.content)
data_counts = tree.xpath("//@data-count")
print(data_counts)
followers = data_counts[2]
print(followers)
#Output: number of followers at t0
