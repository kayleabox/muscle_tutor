def gen_questions_one():
    while region_to_test != QUIT:
        if region_to_test == HEAD_NECK:
            muscles = random.sample(head_neck_function.keys(),3)
            options = head_neck_function[muscles[0]], head_neck_function[muscles[1]], head_neck_function[muscles[2]]
        elif region_to_test == ARM_SHOULDER:
            muscles = random.sample(arm_function.keys(),3)
            options = arm_function[muscles[0]], arm_function[muscles[1]], arm_function[muscles[2]]
        elif region_to_test == HAND:
            muscles = random.sample(hand_function.keys(),3)
            options = hand_function[muscles[0]], hand_function[muscles[1]], hand_function[muscles[2]]
        elif region_to_test == THORAX_SPINE:
            muscles = random.sample(thorax_spine.keys(),3)
            options = thorax_spine_function[muscles[0]], thorax_spine_function[muscles[1]], thorax_spine_function[muscles[2]]
        elif region_to_test == HIP:
            muscles = random.sample(hip_function.keys(),3)
            options = hip_function[muscles[0]], hip_function[muscles[1]], hip_function[muscles[2]]
        elif region_to_test == LEG:
            muscles = random.sample(leg_function.keys(),3)
            options = leg_function[muscles[0]], leg_function[muscles[1]], leg_function[muscles[2]]
        elif region_to_test == FOOT:
            muscles = random.sample(foot_function.keys(),3)
            options = foot_function[muscles[0]], foot_function[muscles[1]], foot_function[muscles[2]]
        else:
            print('invalid input. please try again.')


def gen_questions_two():
    while region_to_test != QUIT:
        region_to_test = menu.get_choice()
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


def gen_rand_question(muscle_dict):
    muscles = random.sample(muscle_dict.keys(),3)
    options = muscle_dict[muscles[0]], muscle_dict[muscles[1]], muscle_dict[muscles[2]]
    question = random.choice(muscles)
    correct_answer = muscle_dict[question]
    return muscles, options, question, correct_answer


