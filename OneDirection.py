import requests
import time
from lxml import html

#I chose a very popular Twitter account so there are enough followers to see a rapid evolution

for i in range(1000):
	website = requests.get('https://twitter.com/onedirection?lang=fr')
	tree=html.fromstring(website.content)
	followers=tree.xpath("//a[@data-nav='followers']/span/@data-count")
	print(followers[0])
	time.sleep(5)