
def gen_rand_question(muscle_dict):
    muscles = random.sample(muscle_dict.keys(),3)
    options = muscle_dict[muscles[0]], muscle_dict[muscles[1]], muscle_dict[muscles[2]]
    question = random.choice(muscles)
    while question in already_asked:
        muscles = random.sample(muscle_dict.keys(), 3)
        options = muscle_dict[muscles[0]], muscle_dict[muscles[1]], muscle_dict[muscles[2]]
        question = random.choice(muscles)
    already_asked.append(question)
    correct_answer = muscle_dict[question]
    return muscles, options, question, correct_answer
    """still need to figure out how to make sure answer choices are not duplicates"""



