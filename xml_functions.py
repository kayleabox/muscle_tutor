import xml.etree.cElementTree as ElementTree
xml_muscles = open('muscles.xml')
tree = ElementTree.parse('muscles.xml')
root = tree.getroot()
attribute=root.attrib

def fill_dict(muscle_dict, region):
    for muscle in tree.iterfind(region):
        origin = muscle.find('origin').text
        insertion = muscle.find('insertion').text
        action = muscle.find('action').text
        name = muscle.get('name')
        muscle_dict[name]=[action, origin, insertion]
    return muscle_dict

xml_muscles.close()