#!/usr/bin/env python
from requests import get
from lxml import html
import sys
import mysql.connector

def add_product(URL):
	try:
		response = get(URL)
		tree = html.fromstring(response.content)
	except:
		print("Not a URL!")
		sys.exit()
	xpaths = {'name':'//*[@id="listing-page-cart"]/div[2]/h1/text()',
			  'image':'//*[@id="listing-right-column"]/div/div[1]/div[1]/div/div/div/div/div[1]/ul/li[1]/img/@src',
			  'price':'//*[@id="listing-page-cart"]/div[3]/div[1]/div[1]/div/div[1]/p/text()'}

	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		password="root",
		port='3307',
		database='mysql'
	)
	
	mycursor = mydb.cursor()

	mycursor.execute("SELECT ID FROM products ORDER BY ID DESC LIMIT 1")
	greatest_id = mycursor.fetchall()
	
	line = list()
	line.append(greatest_id[0][0]+1)

	for i in xpaths:
		text = tree.xpath(xpaths[i])[0].strip()
		line.append(text)

	sql = 'INSERT INTO products (ID, name, image, price) VALUES (%s, %s, %s, %s)'
	mycursor.execute(sql, line)
	mydb.commit()
	print(mycursor.rowcount, "record inserted.")
	print(line)

def status(pid):
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		password="root",
		port='3307',
		database='mysql'
	)

	mycursor = mydb.cursor()
	sql = "SELECT * FROM products WHERE ID = %s"
	pid = (pid,)
	mycursor.execute(sql, pid)
	line = mycursor.fetchall()
	print(line)

try:
	operation = sys.argv[1]

except:
	print("please try one of these statements:\npython get_infos.py -a [URL]\npython get_infos.py -s [ID]")
	sys.exit()
	
if operation == "-a" and len(sys.argv) == 3:
	URL = sys.argv[2]
	add_product(URL)

elif operation == "-s" and len(sys.argv) == 3:
	p_id = int(sys.argv[2])
	status(p_id)

else:
	print("please try one of these statements:\npython get_infos.py -a [URL]\npython get_infos.py -s [ID]")










