"""Reflow"""

from io import StringIO
import pyperclip 

text = pyperclip.paste() #get from clipboard

text=text.replace("\r\n\r\n","$$$$")
text=text.replace("\r\n","")
text=text.replace("$$$$","\r\n\r\n")

pyperclip.copy(text) #output to clipboard

input("Press Enter to continue...")