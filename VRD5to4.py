import xml.etree.ElementTree as ET
import re, sys,string

content_file=sys.argv[1]

template = ET.parse(r'D-Template-4.Vprj')
content  = ET.parse(content_file)
# output   = open('out-4.vprj','w')

# ET.dump(template)




# template_soup = bs4.BeautifulSoup(template,'html.parser')
# content_soup  = bs4.BeautifulSoup(content )


# print template_soup.CutList

old_cutlist= template.getroot().find("CutList") 
old_scnlist= template.getroot().find("SceneList") 
new_cutlist=  content.getroot().find("CutList") 
new_scnlist=  content.getroot().find("SceneList") 

old_filename=  template.getroot().find("Filename") 
old_OSP=  template.getroot().find("OpenStreamParams") 
old_InputFilename=  old_OSP.find("InputFilename") 
new_filename=   content.getroot().find("Filename") 


# ET.dump(old_cutlist)

for cut in list(old_cutlist):
	# print (cut)
	old_cutlist.remove(cut)

for cut in new_cutlist:
	old_cutlist.insert(99,cut)
# old_cutlist.remove(cut)
	
for thing in new_scnlist:
	old_scnlist.insert(99,thing)
	# old_cutlist.remove(cut)

# for 
# ET.dump(template)
# print(old_filename.text)
old_filename.text=new_filename.text
old_InputFilename.text=new_filename.text
# print(old_filename.text)

template.write(content_file+"4.vprj")

# input("ddd")
# print(old_scnlist)