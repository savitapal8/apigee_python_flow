
























import xml.etree.ElementTree as ET

def createflow(filename, proxytettag, tagtype):
        tree = ET.parse(filename)
        root = tree.getroot()
        for child in root:
            if child.tag == proxytettag:
                for subchild in child:
                    if subchild.tag == tagtype:
                        for sub_subchild in subchild:
                            print(sub_subchild[0].text)

createflow('default.xml', "PreFlow", "Request")