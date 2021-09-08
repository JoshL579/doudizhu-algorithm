import random
from possible_handler import *
from type_handler import find_type
from config import *


def one_round(my_possible_picks, enemy_possible_picks, picks_previous, starter):
    possible_pairs = []

    # 非首发开牌情况
    # case: starter=me
    if starter == 'me':
        for picks in enemy_possible_picks:
            if is_possible_picks(picks_previous, picks):
                updated_picks = [origin_picks for origin_picks in enemy_possible_picks if origin_picks != picks]
                for second_picks in updated_picks:
                    if is_possible_picks(picks, second_picks):
                        possible_pairs.append([picks_previous.get('picks'), picks, second_picks])

    print(possible_pairs)


def possible_picks(list_mine, list_outside):
    my_possible_picks = []
    enemy_possible_picks = []
    funcs = all_funcs()

    # combine possible picks of mine
    for func in funcs:
        possible_picks = func(list_mine)
        if possible_picks:
            my_possible_picks = my_possible_picks + possible_picks

    # combine possible picks of enemy
    for func in funcs:
        possible_picks = func(list_outside)
        if possible_picks:
            enemy_possible_picks = enemy_possible_picks + func(list_outside)

    print(my_possible_picks)
    print('--------------------')
    print(enemy_possible_picks)
    return my_possible_picks, enemy_possible_picks


def is_possible_picks(picks_previous, picks_current):
    current_res = find_type(picks_current)
    current_type = current_res.get('type')
    current_num = current_res.get('num')

    if not picks_previous:
        return {'type': current_type, 'num': current_num, 'picks': picks_current}

    try:    # dict
        previous_type = picks_previous.get('type')
        previous_num = picks_previous.get('num')
    except:     #list
        picks_previous = find_type(picks_previous)
        previous_type = picks_previous.get('type')
        previous_num = picks_previous.get('num')

    if previous_type != current_type:
        return False
    if int(current_num) <= int(previous_num):
        return False
    return {'type': current_type, 'num': current_num, 'picks': picks_current}


# 发牌
def set_picks(list_all):
    list_mine = random.sample(list_all, 17)
    list_remain = [card for card in list_all if card not in list_mine]

    list_outside1 = random.sample(list_remain, 17)
    list_remain = [card for card in list_remain if card not in list_outside1]

    list_outside2 = random.sample(list_remain, 17)
    list_remain = [card for card in list_remain if card not in list_outside2]

    print('list_mine')
    print(sorted(list_mine, key=lambda e: int(e.split('-')[1])))
    print('list_outside1')
    print(sorted(list_outside1, key=lambda e: int(e.split('-')[1])))
    print('list_outside2')
    print(sorted(list_outside2, key=lambda e: int(e.split('-')[1])))
    print('list_base')
    print(sorted(list_remain, key=lambda e: int(e.split('-')[1])))


# return find all function list for further loop
def all_funcs():
    return [
        find_all_shunzi,
        find_all_sanbudai,
        find_all_sandaiyi,
        find_all_sandaiyidui,
        find_all_duizi,
        find_all_sidaier,
        find_all_sidailiangdui,
        find_all_zhadan,
        find_all_feijibudai,
        find_all_feijidaidan,
        find_all_feijidaishuang
    ]




# print(find_type(['bt-3', 'rt-3', 'ft-3', 'ft-3', 'mh-4', 'mh-4']))
# set_picks()
# print(find_all_feijidaidan(['fp-3', 'fp-4', 'rt-4', 'mh-4', 'bt-5', 'fp-5', 'mh-5', 'bt-10', 'rt-10', 'mh-11', 'bt-12', 'fp-13', 'mh-13', 'bt-14', 'mh-14', 'rt-14', 'mh-14']))
possible_picks(list_mine, list_outside)
print(one_round(
    my_possible_picks=[['10', '11', '12', '13', '14'], ['11', '12', '13', '14', '15'], ['10', '11', '12', '13', '14', '15'], ['4', '4', '4'], ['10', '10', '10'], ['14', '14', '14'], ['4', '4', '4', '3'], ['4', '4', '4', '11'], ['4', '4', '4', '12'], ['4', '4', '4', '15'], ['10', '10', '10', '3'], ['10', '10', '10', '11'], ['10', '10', '10', '12'], ['10', '10', '10', '15'], ['14', '14', '14', '3'], ['14', '14', '14', '11'], ['14', '14', '14', '12'], ['14', '14', '14', '15'], ['4', '4', '4', '8', '8'], ['4', '4', '4', '13', '13'], ['10', '10', '10', '8', '8'], ['10', '10', '10', '13', '13'], ['14', '14', '14', '8', '8'], ['14', '14', '14', '13', '13'], ['8', '8'], ['13', '13']],
    enemy_possible_picks=[['3', '4', '5', '6', '7'], ['4', '5', '6', '7', '8'], ['5', '6', '7', '8', '9'], ['6', '7', '8', '9', '10'], ['7', '8', '9', '10', '11'], ['8', '9', '10', '11', '12'], ['9', '10', '11', '12', '13'], ['10', '11', '12', '13', '14'], ['11', '12', '13', '14', '15'], ['12', '13', '14', '15', '16'], ['13', '14', '15', '16', '17'], ['3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17'], ['3', '3', '3'], ['11', '11', '11'], ['12', '12', '12'], ['15', '15', '15'], ['3', '3', '3', '4'], ['3', '3', '3', '10'], ['3', '3', '3', '14'], ['3', '3', '3', '16'], ['3', '3', '3', '17'], ['11', '11', '11', '4'], ['11', '11', '11', '10'], ['11', '11', '11', '14'], ['11', '11', '11', '16'], ['11', '11', '11', '17'], ['12', '12', '12', '4'], ['12', '12', '12', '10'], ['12', '12', '12', '14'], ['12', '12', '12', '16'], ['12', '12', '12', '17'], ['15', '15', '15', '4'], ['15', '15', '15', '10'], ['15', '15', '15', '14'], ['15', '15', '15', '16'], ['15', '15', '15', '17'], ['3', '3', '3', '8', '8'], ['3', '3', '3', '13', '13'], ['11', '11', '11', '8', '8'], ['11', '11', '11', '13', '13'], ['12', '12', '12', '8', '8'], ['12', '12', '12', '13', '13'], ['15', '15', '15', '8', '8'], ['15', '15', '15', '13', '13'], ['8', '8'], ['13', '13'], ['5', '5', '5', '5', '4', '10'], ['5', '5', '5', '5', '4', '14'], ['5', '5', '5', '5', '4', '16'], ['5', '5', '5', '5', '4', '17'], ['5', '5', '5', '5', '10', '4'], ['5', '5', '5', '5', '10', '14'], ['5', '5', '5', '5', '10', '16'], ['5', '5', '5', '5', '10', '17'], ['5', '5', '5', '5', '14', '4'], ['5', '5', '5', '5', '14', '10'], ['5', '5', '5', '5', '14', '16'], ['5', '5', '5', '5', '14', '17'], ['5', '5', '5', '5', '16', '4'], ['5', '5', '5', '5', '16', '10'], ['5', '5', '5', '5', '16', '14'], ['5', '5', '5', '5', '16', '17'], ['5', '5', '5', '5', '17', '4'], ['5', '5', '5', '5', '17', '10'], ['5', '5', '5', '5', '17', '14'], ['5', '5', '5', '5', '17', '16'], ['6', '6', '6', '6', '4', '10'], ['6', '6', '6', '6', '4', '14'], ['6', '6', '6', '6', '4', '16'], ['6', '6', '6', '6', '4', '17'], ['6', '6', '6', '6', '10', '4'], ['6', '6', '6', '6', '10', '14'], ['6', '6', '6', '6', '10', '16'], ['6', '6', '6', '6', '10', '17'], ['6', '6', '6', '6', '14', '4'], ['6', '6', '6', '6', '14', '10'], ['6', '6', '6', '6', '14', '16'], ['6', '6', '6', '6', '14', '17'], ['6', '6', '6', '6', '16', '4'], ['6', '6', '6', '6', '16', '10'], ['6', '6', '6', '6', '16', '14'], ['6', '6', '6', '6', '16', '17'], ['6', '6', '6', '6', '17', '4'], ['6', '6', '6', '6', '17', '10'], ['6', '6', '6', '6', '17', '14'], ['6', '6', '6', '6', '17', '16'], ['7', '7', '7', '7', '4', '10'], ['7', '7', '7', '7', '4', '14'], ['7', '7', '7', '7', '4', '16'], ['7', '7', '7', '7', '4', '17'], ['7', '7', '7', '7', '10', '4'], ['7', '7', '7', '7', '10', '14'], ['7', '7', '7', '7', '10', '16'], ['7', '7', '7', '7', '10', '17'], ['7', '7', '7', '7', '14', '4'], ['7', '7', '7', '7', '14', '10'], ['7', '7', '7', '7', '14', '16'], ['7', '7', '7', '7', '14', '17'], ['7', '7', '7', '7', '16', '4'], ['7', '7', '7', '7', '16', '10'], ['7', '7', '7', '7', '16', '14'], ['7', '7', '7', '7', '16', '17'], ['7', '7', '7', '7', '17', '4'], ['7', '7', '7', '7', '17', '10'], ['7', '7', '7', '7', '17', '14'], ['7', '7', '7', '7', '17', '16'], ['9', '9', '9', '9', '4', '10'], ['9', '9', '9', '9', '4', '14'], ['9', '9', '9', '9', '4', '16'], ['9', '9', '9', '9', '4', '17'], ['9', '9', '9', '9', '10', '4'], ['9', '9', '9', '9', '10', '14'], ['9', '9', '9', '9', '10', '16'], ['9', '9', '9', '9', '10', '17'], ['9', '9', '9', '9', '14', '4'], ['9', '9', '9', '9', '14', '10'], ['9', '9', '9', '9', '14', '16'], ['9', '9', '9', '9', '14', '17'], ['9', '9', '9', '9', '16', '4'], ['9', '9', '9', '9', '16', '10'], ['9', '9', '9', '9', '16', '14'], ['9', '9', '9', '9', '16', '17'], ['9', '9', '9', '9', '17', '4'], ['9', '9', '9', '9', '17', '10'], ['9', '9', '9', '9', '17', '14'], ['9', '9', '9', '9', '17', '16'], ['5', '5', '5', '5', '8', '8', '13', '13'], ['6', '6', '6', '6', '8', '8', '13', '13'], ['7', '7', '7', '7', '8', '8', '13', '13'], ['9', '9', '9', '9', '8', '8', '13', '13'], ['5', '5', '5', '5'], ['6', '6', '6', '6'], ['7', '7', '7', '7'], ['9', '9', '9', '9'], ['11', '11', '11', '12', '12', '12'], ['4', '10', '11', '11', '11', '12', '12', '12'], ['4', '11', '11', '11', '12', '12', '12', '14'], ['4', '11', '11', '11', '12', '12', '12', '16'], ['4', '11', '11', '11', '12', '12', '12', '17'], ['10', '11', '11', '11', '12', '12', '12', '14'], ['10', '11', '11', '11', '12', '12', '12', '16'], ['10', '11', '11', '11', '12', '12', '12', '17'], ['11', '11', '11', '12', '12', '12', '14', '16'], ['11', '11', '11', '12', '12', '12', '14', '17'], ['11', '11', '11', '12', '12', '12', '16', '17'], ['8', '8', '11', '11', '11', '12', '12', '12', '13', '13']],
    picks_previous=picks_previous,
    starter='me'
))