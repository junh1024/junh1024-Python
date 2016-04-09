# IRC2Interview

What this does is convert IRC logs to interviews/play style text

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
4) Output text will be copied to clipboard
