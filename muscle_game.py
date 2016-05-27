# this program will help the user learn the muscles of the body,
# their attachments and functions
import random
import menu_functions as menu
import ask_question_fun as ask_question
import xml.etree.cElementTree as ElementTree
import xml_functions
# create the structure of the quiz
# generate random questions about the muscles in a certain part of the body
# use a dictionary to store the questions and answers

#read info from file muscles.xml
xml_muscles = open ('muscles.xml')
for line in xml_muscles:
   print (line)
###xmldict.xml_to_dict()/xmltodict not sure about this module
tree = ElementTree.parse('muscles.xml')
root = tree.getroot()
attribute=root.attrib
print(root, attribute)
for child in root:
    print(child.tag, child.attrib)
for muscle in root.iter('muscle'):
    print(muscle.attrib)
#finds muscles and there subbranches(origin, insertion, action)
for muscle in root.iter('muscle'):
    origin = muscle.find('origin').text
    insertion = muscle.find('insertion').text
    action = muscle.find('action').text
    name = muscle.get('name')
    print("muscle = ", name, "action = ", action, "origin = ", origin, "insertion = ", insertion)
#this gets the name of the item
for element in tree.iterfind('thorax_and_spine/muscle'):
    print(element.tag, element.attrib)
#gets specific muscle
for element in tree.iterfind('thorax_and_spine/muscle[@name="trapezius"]'):
    print(element.tag, element.attrib)
#head_and_neck dict
head_and_neck = {}
region = 'head_and_neck/muscle'
xml_functions.fill_dict(head_and_neck, region)
print(head_and_neck.keys())
print(head_and_neck.values())
#create arm dictionary
arm = {}
region = 'arm/muscle'
xml_functions.fill_dict(arm, region)
print(arm.keys())
print(arm.values())
#try to create dictionary thorax_and_spine
thorax_and_spine={}
region='thorax_and_spine/muscle'
xml_functions.fill_dict(thorax_and_spine, region)
print(thorax_and_spine.keys())
print(thorax_and_spine.values())
#create leg dictionary
leg= {}
region = 'leg/muscle'
xml_functions.fill_dict(leg, region)
print(leg.keys())
print(leg.values())
#create hand dictionary
hand= {}
region = 'hand/muscle'
xml_functions.fill_dict(hand, region)
print(hand.keys())
print(hand.values())
#create feet dictionary
feet= {}
region = 'feet/muscle'
xml_functions.fill_dict(feet, region)
print(feet.keys())
print(feet.values())
#create hip/pelvis dictionary
pelvis = {}
region = 'pelvis/muscle'
xml_functions.fill_dict(pelvis, region)
print(pelvis.keys())
print(pelvis.values())

dup_option = []
already_asked = []

HEAD_NECK = '1'
ARM_SHOULDER = '2'
HAND = '3'
THORAX_SPINE = '4'
HIP = '5'
LEG = '6'
FOOT = '7'
QUIT = '8'


def main():
    print('would you like to take a quiz about muscles?')
    print('enter any key to continue or q to quit.')
    play = input('> ')
    while play != 'q':

        menu.menu()
        region_to_test = 0
        while region_to_test != QUIT:
            region_to_test = menu.get_choice()
            if region_to_test == HEAD_NECK:
                for muscle in range(0, len(head_and_neck)):
                    muscles, options, question, correct_answer = ask_question.gen_rand_question(head_and_neck, already_asked)
                    #ask_question.ask_question(question, options, correct_answer)
                del already_asked[:]
            elif region_to_test == ARM_SHOULDER:
                for muscle in range(0, len(arm)):
                    muscles, options, question, correct_answer = ask_question.gen_rand_question(arm, already_asked)
                    #ask_question.ask_question(question, options, correct_answer) # this into the gen_rand_question function
                del already_asked[:]
            elif region_to_test == HAND:
                for muscle in range(0, len(hand)):
                    muscles, options, question, correct_answer = ask_question.gen_rand_question(hand, already_asked)
                    #ask_question.ask_question(question, options, correct_answer) # this into the gen_rand_question function
                del already_asked[:]
            elif region_to_test == THORAX_SPINE:
                for muscle in range(0, len(thorax_and_spine)):
                    muscles, options, question, correct_answer = ask_question.gen_rand_question(thorax_and_spine, already_asked)
                    #ask_question.ask_question(question, options, correct_answer)# this into the gen_rand_question function
                del already_asked[:]
            elif region_to_test == HIP:
                for muscle in range(0, len(pelvis)):
                    muscles, options, question, correct_answer = ask_question.gen_rand_question(pelvis, already_asked)
                    #ask_question.ask_question(question, options, correct_answer) # this into the gen_rand_question function
                del already_asked[:]
            elif region_to_test == LEG:
                for muscle in range(0, len(leg)):
                    muscles, options, question, correct_answer = ask_question.gen_rand_question(leg, already_asked)
                    #ask_question.ask_question(question, options, correct_answer) # this into the gen_rand_question function
                del already_asked[:]
            elif region_to_test == FOOT:
                for muscle in range(0, len(feet)):
                    muscles, options, question, correct_answer = ask_question.gen_rand_question(feet, already_asked)
                    #ask_question.ask_question(question, options, correct_answer) # this into the gen_rand_question function
                del already_asked[:]
            elif region_to_test == QUIT:
                print('goodbye!')
                exit()
            else:
                print('invalid input. please try again.')

xml_muscles.close()

main()
