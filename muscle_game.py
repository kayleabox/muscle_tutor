# this program will help the user learn the muscles of the body,
# their attachments and functions
import random


#create the structure of the quiz
#generate random questions about the muscles in a certain part of the body
#use a dictionary to store the questions and answers

arm_function = {'biceps brachii':'flex the elbow','deltoid':'flex shoulder', 'triceps brachii': 'extension of elbow'}
back_function = {}
headneck_function = {}
leg_function = {}
hand_function = {}
feet_function = {}
abdomen_function = {}
hip_function = {}
arm_origin = {}
back_origin = {}
headneck_origin = {}
leg_origin = {}
hand_origin = {}
feet_origin = {}
abdomen_origin = {}
hip_origin = {}
arm_insertion = {}
back_insertion = {}
headneck_insertion = {}
leg_insertion = {}
hand_insertion = {}
feet_insertion = {}
abdomen_insertion = {}
hip_insertion = {}


play = 1
selection = 1
while play != 'q':

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