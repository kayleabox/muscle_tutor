# this program will help the user learn the muscles of the body,
# their attachments and functions
import random
#import menu_functions

#create the structure of the quiz
#generate random questions about the muscles in a certain part of the body
#use a dictionary to store the questions and answers

arm_function = {'biceps brachii':'flex the elbow','deltoid':'flex shoulder', 'triceps brachii': 'extension of elbow'}
thorax_spine_function = {'rectus abdominis':'flex the spine', 'longissimus':'extension of spine', 'multifidi':'rotate to opposite', 'rotatores':'rotation to opposite'}
head_neck_function = {'scm':'flex neck laterally to same side', 'scalenes':'elevate ribs', 'masseter':'elevate mandible', 'temporalis':'elevate mandible'}
leg_function = {}
hand_function = {}
feet_function = {}
hip_function = {}
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

HEAD_NECK = 1
ARM_SHOULDER = 2
HAND = 3
THORAX_SPINE = 4
HIP = 5
LEG = 6
FOOT = 7
QUIT = 8

def main():
    print('would you like to take a quiz about muscles?')
    print('enter any key to continue or q to quit.')
    play = input('> ')
    selection = 1
    while play != 'q':

        menu()
        region_to_test = 0
        while region_to_test != QUIT:
            region_to_test = get_choice()
            if region_to_test == HEAD_NECK:
                muscles = random.sample(head_neck_function.keys(),3)
                options = head_neck_function[muscles[0]], head_neck_function[muscles[1]], head_neck_function[muscles[2]]
                question = random.choice(muscles)
                correct_answer = head_neck_function[question]
            elif region_to_test == ARM_SHOULDER:
                muscles = random.sample(arm_function.keys(),3)
                options = arm_function[muscles[0]], arm_function[muscles[1]], arm_function[muscles[2]]
                question = random.choice(muscles)
                correct_answer = arm_function[question]
            elif region_to_test == HAND:
                muscles = random.sample(hand_function.keys(),3)
                options = hand_function[muscles[0]], hand_function[muscles[1]], hand_function[muscles[2]]
                question = random.choice(muscles)
                correct_answer = hand_function[question]
            elif region_to_test == THORAX_SPINE:
                muscles = random.sample(thorax_spine_function.keys(),3)
                options = thorax_spine_function[muscles[0]], thorax_spine_function[muscles[1]], thorax_spine_function[muscles[2]]
                question = random.choice(muscles)
                correct_answer = thorax_spine_function[question]
            elif region_to_test == HIP:
                muscles = random.sample(hip_function.keys(),3)
                options = hip_function[muscles[0]], hip_function[muscles[1]], hip_function[muscles[2]]
                question = random.choice(muscles)
                correct_answer = hip_function[question]
            elif region_to_test == LEG:
                muscles = random.sample(leg_function.keys(),3)
                options = leg_function[muscles[0]], leg_function[muscles[1]], leg_function[muscles[2]]
                question = random.choice(muscles)
                correct_answer = leg_function[question]
            elif region_to_test == FOOT:
                muscles = random.sample(feet_function.keys(),3)
                options = feet_function[muscles[0]], feet_function[muscles[1]], feet_function[muscles[2]]
                question = random.choice(muscles)
                correct_answer = feet_function[question]
            else:
                print('invalid input. please try again.')

            #muscles = random.sample(arm_function.keys(),3)
            #options = arm_function[muscles[0]], arm_function[muscles[1]], arm_function[muscles[2]]
            #question = random.choice(muscles)
            print( 'muscle ', question)
            #correct_answer = arm_function[question]
            print ('function ', correct_answer)

            while selection != correct_answer:
                print('what is the function of ', question , "?")
                print("\n(a)%s  (b)%s   (c)%s" % tuple(options))
                a, b, c = options[0], options[1], options[2]
                selection = input ("> ")
                print ('answer ', selection)

                if selection == 'a':
                    if options[0] == correct_answer:
                        correct_answer = 'a'
                        print('correct!')
                    else:
                        print('try again')
                elif selection == 'b':
                    if options[1] == correct_answer:
                        correct_answer = 'b'
                        print('correct!')
                    else:
                        print('try again')
                elif selection == 'c':
                    if options[2] == correct_answer:
                        correct_answer = 'c'
                        print('correct!')
                    else:
                        print('try again')
                elif selection == 'q':
                    print('goodbye!')
                    exit()
                else:
                    print('choose a valid option')

def menu():
    print('menu options\n')
    print('__________________\n')
    print('1)head and neck\n')
    print('2)arm and shoulder\n')
    print('3)hand\n')
    print('4)thorax and spine\n')
    print('5)hip\n')
    print('6)leg\n')
    print('7)foot\n')

def get_choice():
    choice = int(input('what part of the body would you like to work on?'))
    return choice

main()
