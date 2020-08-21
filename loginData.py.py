#!C:\\Program Files (x86)\\Python38-32\\python.exe

import cgi, cgitb 

form = cgi.FieldStorage() 

name   = form.getvalue('name')
email  = form.getvalue('email')
message  = form.getvalue('message')

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")
print ("<h2>Hello %s %s</h2>" % (name, email, message))
print ("</body>")
print ("</html>")
