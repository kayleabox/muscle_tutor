# this program will help the user learn the muscles of the body,
# their attachments and functions
import random
import menu_functions as menu
import ask_question_fun as ask_question
import xml.etree.cElementTree as ElementTree

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
for muscle in root.iter('muscle'):
    origin = muscle.find('origin').text
    insertion = muscle.find('insertion').text
    action = muscle.find('action').text
    name = muscle.get('name')
    print("muscle = ", name, "action = ", action, "origin = ", origin, "insertion = ", insertion)

arm_function = {'biceps brachii': 'flex the elbow', 'deltoid': 'flex shoulder', 'triceps brachii': 'extension of elbow'}
thorax_spine_function = {'rectus abdominis': 'flex the spine', 'longissimus': 'extension of spine',
                         'multifidi': 'rotate to opposite', 'rotatores': 'rotation to opposite'}
head_neck_function = {'scm': 'flex neck laterally to same side', 'scalenes': 'elevate ribs',
                      'masseter': 'elevate mandible', 'temporalis': 'elevate mandible'}
leg_function = {'rectus femorus': '1', 'adductor magnus': '2', 'vastus lat': '3', 'vastus int': '4', 'vastus med': '5',
                'biceps fem': '6'}
hand_function = {'7':'7', '6':'6', '5':'5', '3':'6','4':'5', '8':'7' }
feet_function = {}
hip_function = {'glute max': '1', 'glute med': '2', 'glute min': '3', 'piriformis': '4', 'quadratus fem': '5'}
arm_origin = {}
thorax_spine_origin = {}
head_neck_origin = {}
leg_origin = {}
hand_origin = {}
feet_origin = {}
hip_origin = {}
arm_insertion = {}
thorax_spine_insertion = {}
head_neck_insertion = {}
leg_insertion = {}
hand_insertion = {}
feet_insertion = {}
hip_insertion = {}

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
                for muscle in range(0, len(head_neck_function)):
                    muscles, options, question, correct_answer = ask_question.gen_rand_question(head_neck_function, already_asked)
                    #ask_question.ask_question(question, options, correct_answer)
                del already_asked[:]
            elif region_to_test == ARM_SHOULDER:
                for muscle in range(0, len(arm_function)):
                    muscles, options, question, correct_answer = ask_question.gen_rand_question(arm_function, already_asked)
                    #ask_question.ask_question(question, options, correct_answer) # this into the gen_rand_question function
                del already_asked[:]
            elif region_to_test == HAND:
                for muscle in range(0, len(hand_function)):
                    muscles, options, question, correct_answer = ask_question.gen_rand_question(hand_function, already_asked)
                    #ask_question.ask_question(question, options, correct_answer) # this into the gen_rand_question function
                del already_asked[:]
            elif region_to_test == THORAX_SPINE:
                for muscle in range(0, len(thorax_spine_function)):
                    muscles, options, question, correct_answer = ask_question.gen_rand_question(thorax_spine_function, already_asked)
                    #ask_question.ask_question(question, options, correct_answer)# this into the gen_rand_question function
                del already_asked[:]
            elif region_to_test == HIP:
                for muscle in range(0, len(hip_function)):
                    muscles, options, question, correct_answer = ask_question.gen_rand_question(hip_function, already_asked)
                    #ask_question.ask_question(question, options, correct_answer) # this into the gen_rand_question function
                del already_asked[:]
            elif region_to_test == LEG:
                for muscle in range(0, len(leg_function)):
                    muscles, options, question, correct_answer = ask_question.gen_rand_question(leg_function, already_asked)
                    #ask_question.ask_question(question, options, correct_answer) # this into the gen_rand_question function
                del already_asked[:]
            elif region_to_test == FOOT:
                for muscle in range(0, len(feet_function)):
                    muscles, options, question, correct_answer = ask_question.gen_rand_question(feet_function, already_asked)
                    #ask_question.ask_question(question, options, correct_answer) # this into the gen_rand_question function
                del already_asked[:]
            elif region_to_test == QUIT:
                print('goodbye!')
                exit()
            else:
                print('invalid input. please try again.')

xml_muscles.close()

main()
