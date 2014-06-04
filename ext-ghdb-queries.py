# This is pretty simple piece of code to fetch the google dork queries from exploit-db.
# Author: Mayank Pal Singh [mayankpalsingh74@gmail.com]

import sys
import commands
import nltk
import HTMLParser
import time
import random


file_ghdb = open("ghdb.txt","w")
h = HTMLParser.HTMLParser()


# Specify the page number from where you want to fetch queries.
loop = 1

#If you see too many empty google search queries, might be you have downloaded all of them.
while loop < 5000:
	cmd = "wget http://www.exploit-db.com/ghdb/"+str(loop)+"/ -O tempfile.txt"
	status, output = commands.getstatusoutput(cmd)
	cmd = "cat tempfile.txt | grep 'Google search'"
	status, output = commands.getstatusoutput(cmd)
	raw =  nltk.clean_html(output)
	try:
		query = h.unescape(raw)
		val = random.randint(1,10)
		file_ghdb.write(query+"\n")
		print "[$] "+query	
		time.sleep(val)
	except Exception:
		print "[$] Error converting"
	loop+=1	
