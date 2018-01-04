import psycopg2
import requests
import time
from lxml import html

try:
	connstring = "dbname='Twitter' user='postgres' host='localhost' password='coucou'"
	print("Connecting to database %s..." %(connstring))
	conn = psycopg2.connect(connstring)
	print("Connection is successful.")
except:
	print("Failed to connect to the database")

#The next step is to define a cursor to work with.
cursor = conn.cursor()

#Table creation in the Twitter database
cursor.execute("CREATE TABLE IF NOT EXISTS Twitter_1D (SampleNumber int, Followers int, Date date, Heure varchar(8))")

Sample = 1
for i in range(1000):
	website = requests.get('https://twitter.com/onedirection?lang=fr')
	tree=html.fromstring(website.content)
	followers=tree.xpath("//a[@data-nav='followers']/span/@data-count")[0]
	
	date = time.strftime("%d/%m/%y")
	heure = time.strftime("%H:%M:%S")
	
	print(followers, " ", date, " ", heure)
	
	cursor.execute("INSERT INTO Twitter_1D VALUES ('"+ str(Sample) +"','"+ str(followers) +"','"+ str(date) +"','"+ str(heure) +"')")
	conn.commit()
	Sample += 1
	time.sleep(5)

conn.close()
