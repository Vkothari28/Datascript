import xml.etree.ElementTree as ET
import os

path = "C:/Users/vinit/Downloads/test"  # change this directory to where the files are
for filename in os.listdir(path):
    if not filename.endswith('.xml'): continue  # if data files are not stored in a .xml format then comment out this line
    print("filename:" +  filename)
    fullname = os.path.join(path, filename)
    tree = ET.parse(fullname)
    root = tree.getroot()  # this is to locate the start of the xml file which is the root
    for wlsUserData in root.findall('wlsUserData'):  ## change WLs user data to root of XML
        # print(wlsUserData.tag, wlsUserData.attrib)

        AgeGroup = wlsUserData.find('wlsAgeGroup') ## change wlsAgeGroup to the category under root you want to search
        AgeGroup_number = AgeGroup.text



        print("Age Group:" + AgeGroup_number)

    for wlsUniqueId in root.findall('wlsUniqueId'):  # loop to search for unique Id and prints

        print("UniqueId:" + wlsUniqueId.text + os.linesep)







