"""LinkGetter, extracts links of a certain format from HTML source in clipboard"""

from io import StringIO
import pyperclip 
import re, sys, string, base64

prependurl=base64.b64decode(b"aHR0cHM6Ly9hbmltZWJ5dGVzLnR2Lw==")
prependurl=prependurl.decode("utf-8")

text	=pyperclip.paste() #get from clipboard
text	=text.replace("&amp;","&")

prefix	='.*(to\w+\.php.*)".*'
middle	='6\.1'
suffix	='.*'

term	= re.compile(prefix+middle+suffix)

for line in text.splitlines():
	# print(line)
	m1 = term.search(line)
	if m1:
		print(prependurl+m1.group(1))
		# print("match")


# input("Press Enter to continue...")