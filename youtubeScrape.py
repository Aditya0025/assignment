import simplejson as json
import urllib2
from urllib import urlopen
import sys
import time
import csv
import os
import io
os.chdir(r'C:\Users\adity\Desktop\task')
csvFile =open('test.csv',"w")
#csvFile =open('test.tsv',"w")
#writer = csv.writer(csvFile,delimiter=',')
#writer.writerow('Comments')
csvFile.write("comments\n")
STAGGER_TIME = 1 

# open the url and the screen name 
# (The screen name is the screen name of the user for whom to return results for)
url = "https://www.googleapis.com/youtube/v3/commentThreads?key=AIzaSyCYkTUjKgFGcKDnkNQMgSBbb4obnqIzUEM&textFormat=plainText&part=snippet&videoId=Ye8mB6VsUHw&maxResults=100"

# this takes a python object and dumps it to a string which is a JSON
# representation of that object
url1=urlopen(url)
#data = json.load(urllib2.urlopen(url))
result = json.load(url1)


# print the result
itemList= result.get("items")
length=len(itemList)

for i in range(0,length):
	results= (result["items"][i].get('snippet').get("topLevelComment").get('snippet').get("textDisplay")).encode("utf-8")
	print results
	results=results.replace(",", "")
	#print (result["items"][i].get('snippet').get("topLevelComment").get('snippet').get("textDisplay")).encode("utf-8")
	#writer.writerow((result["items"][i].get('snippet').get("topLevelComment").get('snippet').get("textDisplay")).encode("utf-8"))
	csvFile.write(results)
	csvFile.write('\n')
	time.sleep(STAGGER_TIME)

csvFile.close()
