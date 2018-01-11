import matplotlib.pyplot as plt
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
cursor.execute("select Count from TwitterAD")
X = cursor.fetchall()
cursor.execute("select Followers from TwitterAD")
Y = cursor.fetchall()
x=[]
y=[]
z=[]
for i in range(len(X)):
	x.append(X[i][0])
for k in range(len(Y)):
	y.append(Y[k][0])
print(x)
print(y)
conn.close()

maxvalue = max(y)
for j in range(len(Y)):
	z.append(maxvalue)

plt.plot(x,y,'b-', x, z, 'r--')
plt.axis([4,len(x),min(y)-100, max(y)+100])
plt.ylabel('Followers')
plt.xlabel('Timeline')
plt.title('Black Sabbath followers on Twitter')
plt.show()