# this program will help the user learn the muscles of the body,
# their attachments and functions
import random
#import muscle_functions_group1

#create the structure of the quiz
#generate random questions about the muscles in a certain part of the body
#use a dictionary to store the questions and answers

def main():
    arm_function = {'biceps brachii':'flex the elbow','deltoid':'flex shoulder', 'triceps brachii': 'extension of elbow'}
    thorax_spine_function = {}
    head_neck_function = {}
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

    print('would you like to take a quiz about muscles?')
    print('enter any key to continue or q to quit.')
    play = input('> ')
    selection = 1
    while play != 'q':

        menu()
        region_to_test = get_choice()

        muscles = random.sample(arm_function.keys(),3)
        options = arm_function[muscles[0]], arm_function[muscles[1]], arm_function[muscles[2]]
        question = random.choice(muscles)
        print( 'muscle ', question)
        correct_answer = arm_function[question]
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
    print('2)head and neck\n')
    print('1)arm and shoulder\n')
    print('3)hand\n')
    print('4)thorax and spine\n')
    print('5)hip\n')
    print('6)leg\n')
    print('7)foot\n')

def get_choice():
    choice = input('what part of the body would you like to work on?')
    return choice

main()
