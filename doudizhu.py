import random

list_all = [
    'rt-3', 'rt-4', 'rt-5', 'rt-6', 'rt-7', 'rt-8', 'rt-9', 'rt-10', 'rt-11', 'rt-12', 'rt-13', 'rt-14', 'rt-15',
    'bt-3', 'bt-4', 'bt-5', 'bt-6', 'bt-7', 'bt-8', 'bt-9', 'bt-10', 'bt-11', 'bt-12', 'bt-13', 'bt-14', 'bt-15',
    'fp-3', 'fp-4', 'fp-5', 'fp-6', 'fp-7', 'fp-8', 'fp-9', 'fp-10', 'fp-11', 'fp-12', 'fp-13', 'fp-14', 'fp-15',
    'mh-3', 'mh-4', 'mh-5', 'mh-6', 'mh-7', 'mh-8', 'mh-9', 'mh-10', 'mh-11', 'mh-12', 'mh-13', 'mh-14', 'mh-15',
    'j-16', 'j-17'
]
list_mine = ['fp-3', 'fp-4', 'rt-4', 'mh-4', 'bt-8', 'fp-8', 'mh-10', 'bt-10', 'rt-10', 'mh-11', 'bt-12', 'fp-13', 'mh-13', 'bt-14', 'mh-14', 'rt-14', 'mh-15']
list_outside1 = ['rt-3', 'bt-3', 'bt-5', 'mh-6', 'fp-6', 'rt-7', 'bt-7', 'bt-9', 'rt-9', 'mh-9', 'fp-10', 'bt-11', 'bt-13', 'rt-13', 'fp-15', 'rt-15', 'j-17']
list_outside2 = ['mh-3', 'bt-4', 'fp-5', 'mh-5', 'rt-5', 'bt-6', 'rt-6', 'mh-7', 'fp-7', 'rt-8', 'mh-8', 'fp-9', 'rt-11', 'fp-11', 'fp-12', 'rt-12', 'j-16']
list_base = ['mh-12', 'fp-14', 'bt-15']


def set_picks():
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


def find_type(picks):
    num_list = extract_num(picks)

    if len(num_list) == 1:
        return {'type': 'danpai', 'num': num_list[0]}

    if len(num_list) == 2:
        if wangzha(num_list):
            return {'type': 'wangzha', 'num': '14'}
        if duizi(num_list):
            return {'type': 'duizi', 'num': duizi(num_list)}

    if len(num_list) == 3:
        if sanbudai(num_list):
            return {'type': 'sanbudai', 'num': sanbudai(num_list)}

    if len(num_list) == 4:
        if zhadan(num_list):
            return {'type': 'zhadan', 'num': zhadan(num_list)}
        if sandaiyi(num_list):
            return {'type': 'sandaiyi', 'num': sandaiyi(num_list)}

    if len(num_list) == 5:
        if sandaiyidui(num_list):
            return {'type': 'sandaiyidui', 'num': sandaiyidui(num_list)}

    if len(num_list) == 6:
        if sidaier(num_list):
            return {'type': 'sidaier', 'num': sidaier(num_list)}

    if len(num_list) > 4:
        if shunzi(num_list):
            return {'type': 'shunzi', 'num': shunzi(num_list)}

    if len(num_list) == 6 or len(num_list) == 8 or len(num_list) == 10:
        if feiji(num_list):
            return {'type': 'feiji', 'num': feiji(num_list)}

    if len(num_list) == 8:
        if sidailiangdui(num_list):
            return {'type': 'sidailiangdui', 'num': sidailiangdui(num_list)}

    return {'type': 'unknown', 'num': 'unknown'}


# 顺子, 返回最小牌面
def shunzi(num_list):
    if len(num_list) < 4:
        return False
    if all([int(num_list[i]) + 1 == int(num_list[i+1]) for i in range(len(num_list)-1)]):
        return num_list[0]
    return False


# 三不带
def sanbudai(num_list):
    if len(num_list) != 3:
        return False
    if num_list[0] == num_list[1] == num_list[2]:
        return num_list[0]
    return False


# 三带一, 返回三的牌面
def sandaiyi(num_list):
    if len(num_list) != 4:
        return False
    if num_list[0] == num_list[1] == num_list[2] != num_list[3]:
        return num_list[0]
    if num_list[1] == num_list[2] == num_list[3] != num_list[0]:
        return num_list[1]
    return False


# 三带一对
def sandaiyidui(num_list):
    if len(num_list) != 5:
        return False
    if num_list[0] == num_list[1] == num_list[2] and num_list[0] != num_list[3] and num_list[3] == num_list[4]:
        return num_list[0]
    if num_list[2] == num_list[3] == num_list[4] and num_list[2] != num_list[0] and num_list[0] == num_list[1]:
        return num_list[0]
    return False


# 对子, 返回对子牌面
def duizi(num_list):
    if len(num_list) != 2:
        return False
    if num_list[0] == num_list[1]:
        return num_list[0]
    return False


# 四带二
def sidaier(num_list):
    if len(num_list) != 6:
        return False
    if num_list[0] == num_list[1] == num_list[2] == num_list[3] and num_list[0] != num_list[4] and num_list[0] != num_list[5]:
        return num_list[0]
    if num_list[2] == num_list[3] == num_list[4] == num_list[5] and num_list[2] != num_list[0] and num_list[2] != num_list[1]:
        return num_list[2]
    return False


# 四带两对
def sidailiangdui(num_list):
    if len(num_list) != 8:
        return False
    if num_list[0] == num_list[1] == num_list[2] == num_list[3]:
        if num_list[4] == num_list[5] and num_list[6] == num_list[7] and num_list[4] != num_list[6]:
            return num_list[0]
    if num_list[2] == num_list[3] == num_list[4] == num_list[5]:
        if num_list[0] == num_list[1] and num_list[6] == num_list[7] and num_list[0] != num_list[6]:
            return num_list[2]
    if num_list[4] == num_list[5] == num_list[6] == num_list[7]:
        if num_list[0] == num_list[1] and num_list[2] == num_list[3] and num_list[0] != num_list[2]:
            return num_list[4]
    return False


# 炸弹
def zhadan(num_list):
    if len(num_list) != 4:
        return False
    if num_list[0] == num_list[1] == num_list[2] == num_list[3]:
        return num_list[0]
    return False


# 王炸
def wangzha(num_list):
    if len(num_list) != 2:
        return False
    if num_list[0] == '16' and num_list[1] == '17':
        return '16'
    return False


# 飞机
def feiji(num_list):
    if len(num_list) != 6 and len(num_list) != 8 and len(num_list) != 10:
        return False

    if len(num_list) == 6:
        if num_list[0] == num_list[1] == num_list[2] and num_list[3] == num_list[4] == num_list[5]:
            return num_list[0]

    if len(num_list) == 8:
        if num_list[0] == num_list[1] == num_list[2] and num_list[3] == num_list[4] == num_list[5]:
            if num_list[0] != num_list[6] and num_list[0] != num_list[7] and num_list[3] != num_list[6] and num_list[3] != num_list[7]:
                return num_list[0]
        if num_list[1] == num_list[2] == num_list[3] and num_list[4] == num_list[5] == num_list[6]:
            if num_list[1] != num_list[0] and num_list[1] != num_list[7] and num_list[4] != num_list[0] and num_list[3] != num_list[7]:
                return num_list[1]
        if num_list[2] == num_list[3] == num_list[4] and num_list[5] == num_list[6] == num_list[7]:
            if num_list[2] != num_list[0] and num_list[2] != num_list[1] and num_list[5] != num_list[0] and num_list[5] != num_list[1]:
                return num_list[2]

    if len(num_list) == 10:
        if num_list[0] == num_list[1] == num_list[2] and num_list[3] == num_list[4] == num_list[5]:
            if num_list[6] == num_list[7] and num_list[8] == num_list[9] and num_list[7] != num_list[8]:
                if num_list[0] != num_list[6] and num_list[3] != num_list[8]:
                    return num_list[0]
        if num_list[2] == num_list[3] == num_list[4] and num_list[5] == num_list[6] == num_list[7]:
            if num_list[0] == num_list[1] and num_list[8] == num_list[9] and num_list[0] != num_list[8]:
                if num_list[2] != num_list[0] and num_list[5] != num_list[8]:
                    return num_list[2]
        if num_list[4] == num_list[5] == num_list[6] and num_list[7] == num_list[8] == num_list[9]:
            if num_list[0] == num_list[1] and num_list[2] == num_list[3] and num_list[0] != num_list[2]:
                if num_list[4] != num_list[0] and num_list[7] != num_list[2]:
                    return num_list[0]
    return False


def extract_num(picks):
    num_list = []
    for pick in picks:
        num = pick.split('-')[1]
        num_list.append(num)
    num_list.sort()
    return num_list


# print(find_type(['bt-3', 'rt-3', 'ft-3', 'ft-3', 'mh-4', 'mh-4']))
set_picks()