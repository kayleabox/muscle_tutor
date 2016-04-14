# this program will help the user learn the muscles of the body,
# their attachments and functions
import random
import menu_functions as menu
import ask_question_fun as ask_question
#import question_gen_functions as question_gen

#create the structure of the quiz
#generate random questions about the muscles in a certain part of the body
#use a dictionary to store the questions and answers

arm_function = {'biceps brachii':'flex the elbow','deltoid':'flex shoulder', 'triceps brachii': 'extension of elbow'}
thorax_spine_function = {'rectus abdominis':'flex the spine', 'longissimus':'extension of spine', 'multifidi':'rotate to opposite', 'rotatores':'rotation to opposite'}
head_neck_function = {'scm':'flex neck laterally to same side', 'scalenes':'elevate ribs', 'masseter':'elevate mandible', 'temporalis':'elevate mandible'}
leg_function = {'rectus femorus':'1', 'adductor magnus':'2', 'vastus lat':'3', 'vastus int':'4', 'vastus med':'5', 'biceps fem':'6'}
hand_function = {}
feet_function = {}
hip_function = {'glute max':'1', 'glute med':'2', 'glute min':'3', 'piriformis':'4', 'quadratus fem':'5'}
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
    selection = 1
    while play != 'q':

        menu.menu()
        region_to_test = 0
        while region_to_test != QUIT:
            region_to_test = menu.get_choice()
            if region_to_test == HEAD_NECK:
                """muscles = random.sample(head_neck_function.keys(),3)
                options = head_neck_function[muscles[0]], head_neck_function[muscles[1]], head_neck_function[muscles[2]]
                question = random.choice(muscles)
                correct_answer = head_neck_function[question]"""
                for muscle in range(0, len(head_neck_function)):
                    muscles, options, question, correct_answer = gen_rand_question(head_neck_function)
                    ask_question.ask_question(question, options, correct_answer)
            elif region_to_test == ARM_SHOULDER:
                """muscles = random.sample(arm_function.keys(),3)
                options = arm_function[muscles[0]], arm_function[muscles[1]], arm_function[muscles[2]]
                question = random.choice(muscles)
                correct_answer = arm_function[question]"""
                for muscle in range(0, len(arm_function)):
                    muscles, options, question, correct_answer = gen_rand_question(arm_function)
                    ask_question.ask_question(question, options, correct_answer)
            elif region_to_test == HAND:
                """muscles = random.sample(hand_function.keys(),3)
                options = hand_function[muscles[0]], hand_function[muscles[1]], hand_function[muscles[2]]
                question = random.choice(muscles)
                correct_answer = hand_function[question]"""
                for muscle in range(0, len(hand_function)):
                    muscles, options, question, correct_answer = gen_rand_question(hand_function)
                    ask_question.ask_question(question, options, correct_answer)
            elif region_to_test == THORAX_SPINE:
                """muscles = random.sample(thorax_spine_function.keys(),3)
                options = thorax_spine_function[muscles[0]], thorax_spine_function[muscles[1]], thorax_spine_function[muscles[2]]
                question = random.choice(muscles)
                correct_answer = thorax_spine_function[question]"""
                for muscle in range(0, len(thorax_spine_function)):
                    muscles, options, question, correct_answer = gen_rand_question(thorax_spine_function)
                    ask_question.ask_question( question, options, correct_answer)
            elif region_to_test == HIP:
                """muscles = random.sample(hip_function.keys(),3)
                options = hip_function[muscles[0]], hip_function[muscles[1]], hip_function[muscles[2]]
                question = random.choice(muscles)
                correct_answer = hip_function[question]"""
                for muscle in range(0, len(hip_function)):
                    muscles, options, question, correct_answer = gen_rand_question(hip_function)
                    ask_question.ask_question(question, options, correct_answer)
            elif region_to_test == LEG:
                """muscles = random.sample(leg_function.keys(),3)
                options = leg_function[muscles[0]], leg_function[muscles[1]], leg_function[muscles[2]]
                question = random.choice(muscles)
                correct_answer = leg_function[question]"""
                for muscle in range(0, len(leg_function)):
                    muscles, options, question, correct_answer = gen_rand_question(leg_function)
                    ask_question.ask_question(question, options, correct_answer)
            elif region_to_test == FOOT:
                """muscles = random.sample(feet_function.keys(),3)
                options = feet_function[muscles[0]], feet_function[muscles[1]], feet_function[muscles[2]]
                question = random.choice(muscles)
                correct_answer = feet_function[question]"""
                for muscle in range(0, len(feet_function)):
                    muscles, options, question, correct_answer = gen_rand_question(feet_function)
                    ask_question.ask_question(question, options, correct_answer)
            elif region_to_test == QUIT:
                print('goodbye!')
                exit()
            else:
                print('invalid input. please try again.')




def gen_rand_question(muscle_dict):
    muscles = random.sample(muscle_dict.keys(),3)
    options = muscle_dict[muscles[0]], muscle_dict[muscles[1]], muscle_dict[muscles[2]]
    question = random.choice(muscles)
    correct_answer = muscle_dict[question]
    return muscles, options, question, correct_answer


main()
