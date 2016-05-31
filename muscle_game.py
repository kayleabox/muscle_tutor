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
###xmldict.xml_to_dict()/xmltodict not sure about this module
tree = ElementTree.parse('muscles.xml')
root = tree.getroot()
attribute=root.attrib

#head_and_neck dict
head_and_neck = {}
region = 'head_and_neck/muscle'
xml_functions.fill_dict(head_and_neck, region)
#create arm dictionary
arm = {}
region = 'arm/muscle'
xml_functions.fill_dict(arm, region)
#try to create dictionary thorax_and_spine
thorax_and_spine={}
region='thorax_and_spine/muscle'
xml_functions.fill_dict(thorax_and_spine, region)
#create leg dictionary
leg= {}
region = 'leg/muscle'
xml_functions.fill_dict(leg, region)
#create hand dictionary
hand= {}
region = 'hand/muscle'
xml_functions.fill_dict(hand, region)
#create feet dictionary
feet= {}
region = 'foot/muscle'
xml_functions.fill_dict(feet, region)
#create hip/pelvis dictionary
pelvis = {}
region = 'pelvis/muscle'
xml_functions.fill_dict(pelvis, region)


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
            print('would you like to work on action or origin and insertion?')
            act_org_insrt= input('enter a)action, o)origin, i)insertion.')
            if act_org_insrt == 'a':
                act_org_insrt = 'action'
            elif act_org_insrt == 'o':
                act_org_insrt = 'origin'
            elif act_org_insrt == 'i':
                act_org_insrt = 'insertion'

            if region_to_test == HEAD_NECK:
                for muscle in range(0, len(head_and_neck)):
                    muscles, options, question, correct_answer = ask_question.gen_rand_question(head_and_neck, act_org_insrt, already_asked)
                del already_asked[:]
            elif region_to_test == ARM_SHOULDER:
                for muscle in range(0, len(arm)):
                    muscles, options, question, correct_answer = ask_question.gen_rand_question(arm, act_org_insrt, already_asked)
                del already_asked[:]
            elif region_to_test == HAND:
                for muscle in range(0, len(hand)):
                    muscles, options, question, correct_answer = ask_question.gen_rand_question(hand, act_org_insrt, already_asked)
                del already_asked[:]
            elif region_to_test == THORAX_SPINE:
                for muscle in range(0, len(thorax_and_spine)):
                    muscles, options, question, correct_answer = ask_question.gen_rand_question(thorax_and_spine, act_org_insrt, already_asked)
                del already_asked[:]
            elif region_to_test == HIP:
                for muscle in range(0, len(pelvis)):
                    muscles, options, question, correct_answer = ask_question.gen_rand_question(pelvis, act_org_insrt, already_asked)
                del already_asked[:]
            elif region_to_test == LEG:
                for muscle in range(0, len(leg)):
                    muscles, options, question, correct_answer = ask_question.gen_rand_question(leg, act_org_insrt, already_asked)
                del already_asked[:]
            elif region_to_test == FOOT:
                for muscle in range(0, len(feet)):
                    muscles, options, question, correct_answer = ask_question.gen_rand_question(feet, act_org_insrt, already_asked)
                del already_asked[:]
            elif region_to_test == QUIT:
                print('goodbye!')
                exit()
            else:
                print('invalid input. please try again.')

xml_muscles.close()

main()
