"""What this does is convert IRC logs to interviews/play style text
Features:
- Removes nick carets
- Replaces ' i ' with ' I '
- Capitalizes 1st letter of each sentance

Example:
<junh1024> Both upscaled to 2/3 ch
<junh1024> I upscale to 6/7 ch this time
<junh1024> In prev 2, i made fake stereo width, this time, it's all real stereo, but i chopped it up lots
<junh1024> so 3xstereo vs 3xmono
<drf|Desktop> I mean
<drf|Desktop> I'm still fine with just making it actual mono
<drf|Desktop> it sounds just as good

Output:
J: Both upscaled to 2/3 ch. I upscale to 6/7 ch this time. In prev 2, I made fake stereo width, this time, it's all real stereo, but I chopped it up lots. So 3xstereo vs 3xmono.
drf|Desktop: I mean. I'm still fine with just making it actual mono. It sounds just as good.

Usage:
1) Copy some text.
2) Set nicktokennumber to the index of the string token which is the nickname. Some clients have timestamps as the 0th token. Some clients have nicks as the 0th token.
3) Run Irc2Interview.py
4) Output text will be copied to clipboard"""

from io import StringIO
import pyperclip #or stick the pyperclip folder in the current folder if you're lazy like me

# text = """
# <somewan> Hello Wold!
# """

text = pyperclip.paste() #get from clipboard

text=text.replace(" i "," I ")#capitalize Is
text=text.replace("junh1024-XD","J")
text=text.replace("junh1024","J")#replace my own nick, saves space

nicktokennumber = 0 #0 = first token
lastnick=""
lines=text.splitlines()

output = StringIO() #riced string


lines = [line for line in lines if line.strip()]
firstnick=0

for line in lines:
	tokenizedline = line.split(' ')
	try:
		if tokenizedline[nicktokennumber] != lastnick: #new person speaking
			#prevenes making a new linebreak for new 1st nick
			if(firstnick==0):
				firstnick=1
			else:
				output.write("\r\n")
				
			# print(tokenizedline[nicktokennumber])
			# print(lastnick)
			cleanednick=tokenizedline[nicktokennumber].replace('<','').replace('>','') #remove mIRC carets
			output.write(cleanednick + ':')
	except:
		continue #silences errors if lines are too short to parse
	
	for word in range(nicktokennumber+1,len(tokenizedline)):
		output.write(' ')
		if word == nicktokennumber+1: #1st word
			capitalizedfirstword = tokenizedline[word]
			capitalizedfirstword = capitalizedfirstword.capitalize()
			output.write(capitalizedfirstword)
		else:
			output.write(tokenizedline[word]) #print the the rest of the lines
	output.write('.') #add full stop
	lastnick=tokenizedline[nicktokennumber]
	# print(lastnick)

outputstring=output.getvalue()
print(outputstring) #console preview

pyperclip.copy(outputstring) #output to clipboard
