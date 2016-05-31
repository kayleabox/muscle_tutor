# this program will help the user learn the muscles of the body,
# their attachments and functions
import menu_functions as menu
import ask_question_fun as ask_question
import xml.etree.cElementTree as ElementTree
import xml_functions
import keeping_stats
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
#create thorax_and_spine dicitonary
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
#create foot dictionary
foot= {}
region = 'foot/muscle'
xml_functions.fill_dict(foot, region)
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
    correct = 0
    incorrect = 0
    total = 0
    print('would you like to take a quiz about muscles?')
    print('enter any key to continue or q to quit.')
    play = input('> ')
    while play != 'q':
        region_to_test = 0
        while region_to_test != QUIT:
            menu.menu()
            region_to_test = menu.get_choice()
            if region_to_test != '8':
                act_org_insrt= menu.get_act_org_insrt()
            selection = '0'

            if region_to_test == HEAD_NECK:
                correct, incorrect, total = run_quiz(head_and_neck, selection, act_org_insrt, correct, incorrect, total)
            elif region_to_test == ARM_SHOULDER:
                correct, incorrect, total = run_quiz(arm, selection, act_org_insrt, correct, incorrect, total)
            elif region_to_test == HAND:
                correct, incorrect, total = run_quiz(hand, selection, act_org_insrt, correct, incorrect, total)
            elif region_to_test == THORAX_SPINE:
                correct, incorrect, total = run_quiz(thorax_and_spine, selection, act_org_insrt, correct, incorrect, total)
            elif region_to_test == HIP:
                correct, incorrect, total = run_quiz(pelvis, selection, act_org_insrt, correct, incorrect, total)
            elif region_to_test == LEG:
                correct, incorrect, total = run_quiz(leg, selection, act_org_insrt, correct, incorrect, total)
            elif region_to_test == FOOT:
                correct, incorrect, total = run_quiz(foot, selection, act_org_insrt, correct, incorrect, total)
            elif region_to_test == QUIT:
                print('goodbye!')
                if total != 0:
                    print('you got ', correct, ' correct and ', incorrect, 'incorrect out of', total, '.')
                keeping_stats.check_stats(correct, incorrect, total)
                exit()
            else:
                print('invalid input. please try again.')

xml_muscles.close()

def run_quiz(muscle_dict, selection, act_org_insrt, correct, incorrect, total):
    for muscle in range(0, len(muscle_dict)):
        while selection != 'q':
            selection, correct, incorrect, total = ask_question.gen_rand_question(muscle_dict, act_org_insrt, already_asked, correct, incorrect, total)
    del already_asked[:]
    return correct, incorrect, total

main()
