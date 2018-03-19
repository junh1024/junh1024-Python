#python3 pretty print for IRC

# uses portions from HTML.py by Philippe Lagadec ( http://www.decalage.info/python/html ) under the CeCILL  licence (GPL compatible)

import re, sys,string

def link(text, url):
	return '<a href="%s">%s</a>' % (url, text)
	
def picture(url):
	picHTML= '<img src="%s">' % (url)
	return picHTML
	

in_file=sys.argv[1]
 	
read_file = open(in_file,'rb').readlines()

# nick = re.compile(r'(.*)("\w:\\.*\\)(.*".*)$')
joinparts = re.compile(r'(.*[⇐→←].*)|(.*\* \w+.*set.*[+\-]\w .*)') #also matches setting modes
dateandnick = re.compile(r'^\[.*?] <(\w+.*?)> (.*)')
pictures = re.compile(r'(^.*)(http.*?\.(gif|jpg|png))( .*|$)')
# links = r'(^.*)(http.*)( .*|$)'
# * set [+\-]

write_file = open(in_file+".html", "wb") 
write_file.write("<html><body>".encode("utf-8"))


for line in read_file:
	
	line=line.decode('utf-8')
	m1 = joinparts.search(line)
	# m2 = fileInProjPat.search(line)
	if m1:
		line=''
		continue
	m2 = dateandnick.search(line)
	if m2:
		content=m2.group(2)
		
		m3=pictures.search(content)
		if(m3):
			pic=m3.group(2)
			content=m3.group(1)+picture(pic)+m3.group(4)
		
		
		
		line="<strong>"+m2.group(1)+":</strong> "+content+"<br>"
	
	write_file.write(line.encode("utf-8"))
	# print("working")
	# 
write_file.close
# input("Press Enter to continue...")

