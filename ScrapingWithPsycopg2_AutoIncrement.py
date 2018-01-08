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

cursor.execute("CREATE TABLE IF NOT EXISTS TwitterAutoIncrement (Count bigserial primary key, followers integer, time varchar(8), date date);")

while True:
	website = requests.get('https://twitter.com/onedirection?lang=fr')
	tree=html.fromstring(website.content)
	followers=int(tree.xpath("//a[@data-nav='followers']/span/@data-count")[0])
	CurrTime=time.strftime("%H:%M:%S")
	CurrDate=time.strftime("%d/%m/%Y")
	cursor.execute("select max(count) from TwitterAutoIncrement")
	#only if database already exists : 
	#count = int(cursor.fetchall()[0][0]) + 1
	
	#remove the count if database does not exist : 
	#print(count, " ", followers, " ", CurrDate, " ", CurrTime)

	cursor.execute("INSERT INTO TwitterAutoIncrement (time, date, followers) VALUES (%s, %s, %s);", (CurrTime, CurrDate, followers))
	conn.commit()
	time.sleep(5)
conn.close()
