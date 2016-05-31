import random

def gen_rand_question(muscle_dict, act_org_insrt, already_asked):
    muscles, options, question = gen_options(muscle_dict, act_org_insrt)
    while options[0] == options[1] or options[0] == options[2] or options[1] == options[2]:
        if options[0] == options[1]:
            print (options[0]," ", options[1])
            print ("options[0] == options[1]\n")
            new_options(muscle_dict, 0, options, muscles)
        elif options[0] == options[2]:
            print (options[0]," ", options[2])
            print ("options[0] == options[2]\n")
            new_options(muscle_dict, 0, options, muscles)
        elif options[1] == options[2]:
            print (options[1]," ", options[2])
            print ("options[1] == options[2]\n")
            new_options(muscle_dict, 1, options, muscles)

    while question in already_asked:
        muscles, options, question = gen_options(muscle_dict, act_org_insrt)
    already_asked.append(question)
    correct_answer = muscle_dict[question]
    if act_org_insrt == 'a' or act_org_insrt == 'action':
        correct_answer = correct_answer[0]
    elif act_org_insrt == 'o' or act_org_insrt == 'origin':
        correct_answer = correct_answer[1]
    elif act_org_insrt == 'i' or act_org_insrt == 'insertion':
        correct_answer = correct_answer[2]
    ask_question(question,options, correct_answer, act_org_insrt)
    return muscles, options, question, correct_answer
    """still need to figure out how to make sure answer choices are not duplicates"""

def gen_options(muscle_dict, act_org_insrt):
    muscles = random.sample(muscle_dict.keys(),3)
    options = muscle_dict[muscles[0]], muscle_dict[muscles[1]], muscle_dict[muscles[2]]
    if act_org_insrt == 'a' or act_org_insrt == 'action':
        options = options[0][0], options[1][0], options[2][0]
    elif act_org_insrt == 'o' or act_org_insrt == 'origin':
        options = options[0][1], options[1][1], options[2][1]
    elif act_org_insrt == 'i' or act_org_insrt == 'insertion':
        options = options[0][2], options[1][2], options[2][2]
    options = list(options)
    question = random.choice(muscles)
    return muscles, options, question

def new_options(muscle_dict, index, options, muscles):
    del options[index]
    del muscles[index]
    new_muscle = random.sample(muscle_dict.keys(), 1)
    muscles.insert(index, new_muscle)
    options.insert(index, muscle_dict[new_muscle[0]])

def ask_question( question, options, correct_answer, act_org_insrt):
    bool_check_answer = False
    while bool_check_answer != True:
        print('what is the', act_org_insrt, 'of ', question , '?')
        print("\n(a)%s  (b)%s   (c)%s" % tuple(options))
        a, b, c = options[0], options[1], options[2]
        selection = input ("> ")
        print ('answer ', selection)
        bool_check_answer = check_answer(selection,options, correct_answer)

def check_answer(selection, options, correct_answer):
    if selection == 'a':
        if options[0] == correct_answer:
            correct_answer = 'a'
            print('correct!')
            return True
        else:
            print('try again')
            return False
    elif selection == 'b':
        if options[1] == correct_answer:
            correct_answer = 'b'
            print('correct!')
            return True
        else:
            print('try again')
            return False
    elif selection == 'c':
        if options[2] == correct_answer:
            correct_answer = 'c'
            print('correct!')
            return True
        else:
            print('try again')
            return False
    elif selection == 'q':
        print('goodbye!')
        exit()
    else:
        print('choose a valid option')
        return False