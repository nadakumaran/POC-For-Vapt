from cmd2img import cmd2img



f=open('ip')

ips=f.readlines()

for ip in ips:
	i=ip.replace("\n","")
	if i!='':
		cmd2img("C:\\Users\\Nandakumaran\\sslscan\\sslscan.exe "+i,i.replace(':','port'))
	#cmd2image()
	
  
f.close()

#in sslscan folder
#https://cbrunet.net/python-poppler/installation.html
#https://towardsdatascience.com/poppler-on-windows-179af0e50150