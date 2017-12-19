import requests
import time
from lxml import html

#I chose a very popular Twitter account so there are enough followers to see a rapid evolution

for i in range(1000):
	website = requests.get('https://twitter.com/onedirection?lang=fr')
	tree=html.fromstring(website.content)
	followers=tree.xpath("//@data-count")
	final=followers[2]
	print(final)
	time.sleep(5)

"""Test:
31749140
31749140
31749140
31749140
31749141
31749141
31749141
31749142
31749142
31749142
31749140
31749140
31749140
31749140
31749140
31749139
31749139
31749137
(...)
31749121
31749120
31749120
31749119
31749118
31749118
31749119
31749119
31749121
31749122
31749122
31749122
31749122
31749122

Conclusion: OneDirection is losing followers today =)
"""
