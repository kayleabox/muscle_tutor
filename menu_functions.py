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
    print('8)quit\n')


def get_choice():
    choice = input('what part of the body would you like to work on?')
    return choice

def get_act_org_insrt():
    print('would you like to work on action or origin and insertion?')
    act_org_insrt= input('enter a)action, o)origin, i)insertion.')
    act_org_insrt = set_action_origin_insertion(act_org_insrt)
    return act_org_insrt

def set_action_origin_insertion(act_org_insrt):
    if act_org_insrt == 'a':
        act_org_insrt = 'action'
    elif act_org_insrt == 'o':
        act_org_insrt = 'origin'
    elif act_org_insrt == 'i':
        act_org_insrt = 'insertion'
    return act_org_insrt