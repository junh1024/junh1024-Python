#python3 pretty print for IRC

# uses portions from HTML.py by Philippe Lagadec ( http://www.decalage.info/python/html ) under the CeCILL  licence (GPL compatible)

import re, sys,string

global count,in_file,read_file,write_file
count=1

def link(text, url):
	return '<a href="%s">%s</a>' % (url, text)
	
def picture(url):
	picHTML= '<img src="%s" alt="%s">' % (url,url)
	return link(picHTML,url)

def init():
	global count,in_file,read_file,write_file

	in_file=sys.argv[1]
		
	read_file = open(in_file,'rb').readlines()
	opennewfile()
	# nick = re.compile(r'(.*)("\w:\\.*\\)(.*".*)$')

	# * set [+\-]

def opennewfile():
	global count,in_file,read_file,write_file
	
	try:
		write_file.write("</body></html>".encode("utf-8"))
		write_file.close
	except:
		pass
	finally:
		temp_filename=''
		temp_filename=in_file+'.'+str(count)+".html"
		write_file = open(temp_filename, "wb") 
		write_file.write("<html><body>".encode("utf-8"))
		count+=1



def main():
	global count,in_file,read_file,write_file
	
	
	init()
	print(count)
	joinparts = re.compile(r'(.*[⇐→←].*)|(.*\* \w+.*set.*[+\-]\w .*)') #also matches setting modes
	dateandnick = re.compile(r'^\[.*?] <(\w+.*?)> (.*)')
	pictures = re.compile(r'(^.*)(http.*?\.(gif|jpg|png))(.*)')
	links = re.compile(r'(^.*)(http.*?)( .*|$)')
	
	for read_line in read_file:
		if count % 1000 ==1 :
			opennewfile()
			# count=0
		line=read_line.decode('utf-8')
		m1 = joinparts.search(line)
		# m2 = fileInProjPat.search(line)
		if m1:
			line=''
			continue
		m2 = dateandnick.search(line)
		if m2:
			content=m2.group(2)
			
			m3=pictures.search(content)
			m4=links.search(content)
			
			if(m3):
				pic=m3.group(2)
				content=m3.group(1)+picture(pic)+m3.group(4)
				
			elif(m4):
				content=m4.group(1)+link(m4.group(2),m4.group(2))+m4.group(3)
			
			line="<strong>"+m2.group(1)+":</strong> "+content+"<br>"
		write_file.write(line.encode("utf-8"))
		# print("working")
		count+=1

	write_file.close
	# input("Press Enter to continue...")

if __name__ == "__main__":
    main()