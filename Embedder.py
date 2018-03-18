#python3

import re, sys,string

in_file=sys.argv[1]
 	
read_file = open(in_file,'rb').readlines()

# nick = re.compile(r'(.*)("\w:\\.*\\)(.*".*)$')
joinparts = re.compile(r'(.*[⇐→←].*)|(.*\* \w+.*set.*[+\-]\w .*)') #also matches setting modes
dateandnick = re.compile(r'\[\d+\-\d+\-\d+\s+\d+:\d+:\d+\] <(\w+?)> (.*)')
# * set [+\-]

write_file = open(in_file+"_out.txt", "wb") 


for line in read_file:
	
	line=line.decode('utf-8')
	m1 = joinparts.search(line)
	# m2 = fileInProjPat.search(line)
	if m1:
		line=''
		continue
	m2 = dateandnick.search(line)
	if m2:
		line="<strong>"+m2.group(1)+":</strong> "+m2.group(2)
	
	write_file.write(line.encode("utf-8"))
	# print("working")
	# 
write_file.close
input("Press Enter to continue...")
