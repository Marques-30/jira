import urllib2, base64
import requests
import ssl
import json
import os
from pprint import pprint
import getpass
import cx_Oracle
import csv
import time

UserName = 'butilm01' #raw_input("Enter Lan-ID: ")
#pswd = getpass.getpass('Password:')

with open("Report_Jira.csv", "wb") as out_file:
            writer=csv.writer(out_file, lineterminator='\n')
            
# Total number of users or licenses used in JIRA. REST api of jira can take values of 50 incremental
            ListStartAt = [0,50,100,150,200,250,300]
            for i in ListStartAt:
                request = urllib2.Request("http://jira.bankofthewest.com:8080/rest/api/2/search?jql=Project=%27DIHC%27")
                base64string = base64.encodestring('%s:%s' % (UserName, UserName)).replace('\n', '')
                request.add_header("Authorization", "Basic %s" % base64string) 
                gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
                result = urllib2.urlopen(request, context=gcontext)
            
                JsonProjectdata = result.read()
                jsonToPython = json.loads(JsonProjectdata)

                print JsonProjectdata
                print jsonToPython

                log=str(JsonProjectdata).split(":")
                cut=str(log).split(",")
                header = ['Expand', 'StartAt', 'maxResults', 'total', 'issues', 'id', 'Key',]
                count = 0 
                while count<9900:
                    expand = log[0 + count]
                    issues = cut[0 + count]
                    print expand
                    print issues
                    control = [expand, issues]
                    writer.writerows(control)
                    count += 1
                    time.sleep(0.1)
