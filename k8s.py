#!/usr/bin/python3
import cgi
import subprocess
import re

print("content-type:text/html")
print()

f=cgi.FieldStorage()
cmd=f.getvalue('x')
p="kubectl"
if re.search(p,cmd):
     output=subprocess.getoutput("sudo "+ cmd + " --kubeconfig /root/kubews/admin.conf")
else:
     output=subprocess.getoutput("sudo "+ cmd)

print(output)
