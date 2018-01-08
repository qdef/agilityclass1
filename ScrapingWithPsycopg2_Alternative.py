import psycopg2
import requests
import time
from lxml import html
try:
	connstring = "dbname='quxwmelo' user='quxwmelo' host='horton.elephantsql.com' password='q8Hks013GlhDWaJ6xHJHxuUa2T6Pv_zJ'"
	print("Connecting to database %s..." %(connstring))
	conn = psycopg2.connect(connstring)
	print("Connection is successful.")
except:
	print("Failed to connect to the database")
cursor = conn.cursor()

Sample = 1
cursor.execute("CREATE TABLE IF NOT EXISTS Twitter_2D (count integer, time varchar(8), date date, followers integer);")
try:
	cursor.execute("SELECT MAX(count) FROM Twitter_2D;")
	Sample = cursor.fetchall()[0][0] + 1
	print("Sampling resumes at next count")
except:
	print("Could not find former count number.")

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
	time.sleep(5)
conn.close()
