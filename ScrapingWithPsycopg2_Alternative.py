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
cursor = conn.cursor()

# in case you wanna delete the former version of this table:
#cursor.execute("DROP TABLE IF EXISTS Twitter_2D")

cursor.execute("CREATE TABLE IF NOT EXISTS Twitter_2D (count integer, time varchar(8), date date, followers integer);")
Sample = 1
while True:
	website = requests.get('https://twitter.com/onedirection?lang=fr')
	tree=html.fromstring(website.content)
	followers=int(tree.xpath("//a[@data-nav='followers']/span/@data-count")[0])
	CurrTime=time.strftime("%H:%M:%S")
	CurrDate=time.strftime("%d/%m/%Y")
	
	print(Sample, " ", followers, " ", CurrDate, " ", CurrTime)
	
	cursor.execute("INSERT INTO Twitter_2D (count, time, date, followers) VALUES (%s, %s, %s, %s);", (Sample, CurrTime, CurrDate, followers))
	conn.commit()
	Sample += 1
	#print(time.ctime(CurrTime), followers)
	time.sleep(5)
conn.close()
