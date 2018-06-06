import xml.etree.ElementTree as ET


template = ET.parse('05-25_20-55-02_TVNZ 2 (AAC,eng)_Taskmaster-4.Vprj')
content  = ET.parse('05-25_20-55-02_TVNZ 2 (AAC,eng)_Taskmaster-5.Vprj')
output   = open('out-4.vprj','w')

# ET.dump(template)

template.write('out-4.vprj')


# template_soup = bs4.BeautifulSoup(template,'html.parser')
# content_soup  = bs4.BeautifulSoup(content )


# print template_soup.CutList

old_cutlist= template.getroot().find("CutList") 
old_scnlist= template.getroot().find("SceneList") 
new_cutlist=  content.getroot().find("CutList") 


# ET.dump(old_cutlist)

for cut in list(old_cutlist):
	# print (cut)
	old_cutlist.remove(cut)

for cut in new_cutlist:
	old_cutlist.insert(99,cut)
	# old_cutlist.remove(cut)
	
# ET.dump(old_cutlist)

print(old_scnlist)