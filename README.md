# agilityclass1
"""Xpath test for web scraping
This Python script uses "requests" and "lxml" libraries to retrieve the number of Twitter or Instagram followers of a specific social media account. Still in process."""

import requests
from lxml import html
president = requests.get('https://twitter.com/EmmanuelMacron?lang=fr')
print(president)
# Output: <Response [200]>
tree = html.fromstring(president.content)
followers = tree.xpath('/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div/div/ul/li[3]/a/span[3]')
print(tree)
# Output: <Element html at 0x10690b778>
print(followers)
# Output: []

