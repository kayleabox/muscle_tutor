def ask_question():
    while selection != correct_answer:
        print('what is the function of ', question , "?")
        print("\n(a)%s  (b)%s   (c)%s" % tuple(options))
        a, b, c = options[0], options[1], options[2]
        selection = input ("> ")
        print ('answer ', selection)
        return selection

def check_answer(selection):
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