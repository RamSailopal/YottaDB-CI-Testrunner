#!/usr/bin/python3
import json
import subprocess
import getopt
import sys
import datetime
HTML=0
finres=0
dat = datetime.datetime.now()
options, remainder = getopt.getopt(sys.argv[1:], 'f:o', ['file=','output'])
options1=options[0]
if len(options)==0:
   file="test.json"
for opt,arg in options:
   if opt in ("-f", "--file"):
      file=options1[1]
   else:
      file="test.json"
   if opt in ("-o", "--output"):
      HTML=1
if (HTML==1):
   e = open("results.html", "w")
   e.write("<HTML>\n<BODY>\n<H1>YottaDB Test Results - " + dat.strftime("%c") + "</H1>\n<TABLE>\n<TR><TH align=\"center\">Test Name</TH><TH align=\"center\">Test No</TH><TH align=\"center\">Global Entry</TH><TH align=\"center\">Actual</TH><TH align=\"center\">Expected</TH><TH align=\"center\">Result</TH></TR>\n")
with open(file) as f:
  data = json.load(f)
for i in data:
   for j in i["tests"]:
      cnt=0
      print("Executing test - " + j["name"])
      cmd=j["action"]
      process = subprocess.Popen(cmd,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              shell=True)
      result = process.communicate()
      for k in j["result"]:
         print("\nChecking global entry - " + k["global"])
         cmd="ydb <<< 'W $G(" + k["global"] + ")' | awk '/(^$)|(^YDB>)/ { next } { print }'"
         process = subprocess.Popen(cmd,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              shell=True)
         result = process.communicate()
         result1=result[0].decode('utf-8').replace("\n","")
         if (str(result1) == str(k["value"])):
            cnt=cnt+1
            print("Actual:  " + str(result1) + "  Expected:  " + str(k["value"]) + "  ............... " + "PASS")
            if(HTML==1):
               e.write("<TR><TD align=\"center\">" +  j["name"]  + "</TD><TD align=\"center\">" + str(cnt) + "</TD><TD align=\"center\">" + str(k["global"]) + "</TD><TD align=\"center\">" + str(result1) + "</TD><TD align=\"center\">" + str(k["value"]) + "</TD><TD><FONT COLOR=\"#58D68D\">PASS</FONT></TD></TR>\n")
         else:
            finres=1
            print("Actual:  " + str(result1) + "  Expected:  " + str(k["value"]) + " ............... " + "FAIL")
            if(HTML==1):
               e.write("<TR><TD align=\"center\">" + str(cnt) + "</TD><TD align=\"center\">" + str(k["global"]) + "</TD><TD align=\"center\">" + str(result1) + "</TD><TD align=\"center\">" + str(k["value"]) + "</TD><TD><FONT COLOR=\"red\">FAIL</FONT></TD></TR>\n")
f.close()
if (finres==0):
   finres1="<FONT COLOR=\"#58D68D\">PASS</FONT>"
else:
   finres1="<FONT COLOR=\"red\">FAIL</FONT>"
if(HTML==1):
   e.write("</TABLE>\n<P><B>Overall result for test run - </B>" + finres1 + "</P></BODY>\n</HTML>")
   e.close()
sys.exit(finres)
