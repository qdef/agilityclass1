import psycopg2
import requests
import time
from lxml import html


try:
	conn = psycopg2.connect("dbname='Twitter' user='postgres' host='localhost' password='coucou'")
except:
	print("Failed to connect to the database")


#The next step is to define a cursor to work with. 
cur = conn.cursor()

#Now that we have the cursor defined we can execute a query. 
cur.execute("""SELECT datname from pg_database""")

#When you have executed your query you need to have a list [variable?] to put your results in. 
rows = cur.fetchall()
	
#Now all the results from our query are within the variable named rows. 
#Using this variable you can start processing the results. 
#To print the screen you could do the following. 
print ("\nShow me the databases:\n")
for row in rows:
	print ("   ", row[0])
	
	

"""
for i in range(1000):
	website = requests.get('https://twitter.com/onedirection?lang=fr')
	tree=html.fromstring(website.content)
	followers=tree.xpath("//a[@data-nav='followers']/span/@data-count")
	print(followers[0])
	time.sleep(5)
"""