
def gen_rand_question(muscle_dict):
    muscles = random.sample(muscle_dict.keys(),3)
    options = muscle_dict[muscles[0]], muscle_dict[muscles[1]], muscle_dict[muscles[2]]
    question = random.choice(muscles)
    #muscle_dict.pop(question)
    correct_answer = muscle_dict[question]
    return muscles, options, question, correct_answer




