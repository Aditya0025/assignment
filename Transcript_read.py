import simplejson as json
import urllib2
from urllib import urlopen
import sys
import time
import csv
import os
import io
os.chdir(r'C:\Users\jc\Desktop')
File =open('xxx.tsv',"r")
#print File.readlines()
File1= File.readlines()
#print File1
length=len(File1)
print length

str = ''.join(File1)
#print str
#print len(str)
str=str.replace(",","")
str=str.replace("\n","")
print str

csvFile =open('transcript.csv',"w")
#csvFile =open('test.tsv',"w")
#writer = csv.writer(csvFile,delimiter=',')
#writer.writerow('Comments')
csvFile.write("Transcript\n")
csvFile.write(str)
csvFile.close()
