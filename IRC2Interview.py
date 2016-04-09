from io import StringIO



text = """
<junh1024> Both upscaled to 2/3 ch
<junh1024> I upscale to 6/7 ch this time
<junh1024> In prev 2, i made fake stereo width, this time, it's all real stereo, but i chopped it up lots
<junh1024> so 3xstereo vs 3xmono
<drf|Desktop> I mean
<drf|Desktop> I'm still fine with just making it actual mono
<drf|Desktop> it sounds just as good

"""

text=text.replace(" i "," I ")#capitalize Is

nicktokennumber = 0 #0 = first token
lastnick=""

lines = text.splitlines() #split by line
output = StringIO() #riced string


for line in lines:
	tokenizedline = line.split(' ')
	try:
		if tokenizedline[nicktokennumber] != lastnick: #different nick
			# print(tokenizedline[nicktokennumber])
			# print(lastnick)
			cleanednick=tokenizedline[nicktokennumber].replace('<','').replace('>','')
			output.write('\r\n' + cleanednick + ':')
	except:
		continue
	for word in range(nicktokennumber+1,len(tokenizedline)):
		output.write(' '+ tokenizedline[word]) #print the the rest of the lines
	output.write('.') #add full top
	lastnick=tokenizedline[nicktokennumber]
	# print(lastnick)

outputstring=output.getvalue()
print(outputstring)
