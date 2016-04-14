def ask_question( question, options, correct_answer):
    bool_check_answer = False
    while bool_check_answer != True:
        print('what is the function of ', question , "?")
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