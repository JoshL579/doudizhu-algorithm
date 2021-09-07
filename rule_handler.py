import random
from possible_handler import *
from type_handler import find_type
from config import *


def one_round(list_mine, list_outside):
    funcs = all_funcs()
    for func in funcs:
        print(func(list_mine))

    print('--------------------')
    for func in funcs:
        print(func(list_outside))


def find_winner(picks_previous, picks_current):
    current_res = find_type(picks_current)
    current_type = current_res.get('type')
    current_num = current_res.get('num')

    if not picks_previous:
        return {'type': current_type, 'num': current_num, 'picks': picks_current}

    previous_type = picks_previous.get('type')
    previous_num = picks_previous.get('num')

    if previous_type != current_type:
        return False
    if current_num < previous_num:
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
one_round(list_mine, list_outside)