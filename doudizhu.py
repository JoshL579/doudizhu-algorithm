import random

list_all = [
    'rt-3', 'rt-4', 'rt-5', 'rt-6', 'rt-7', 'rt-8', 'rt-9', 'rt-10', 'rt-11', 'rt-12', 'rt-13', 'rt-14', 'rt-15',
    'bt-3', 'bt-4', 'bt-5', 'bt-6', 'bt-7', 'bt-8', 'bt-9', 'bt-10', 'bt-11', 'bt-12', 'bt-13', 'bt-14', 'bt-15',
    'fp-3', 'fp-4', 'fp-5', 'fp-6', 'fp-7', 'fp-8', 'fp-9', 'fp-10', 'fp-11', 'fp-12', 'fp-13', 'fp-14', 'fp-15',
    'mh-3', 'mh-4', 'mh-5', 'mh-6', 'mh-7', 'mh-8', 'mh-9', 'mh-10', 'mh-11', 'mh-12', 'mh-13', 'mh-14', 'mh-15',
    'j-16', 'j-17'
]
list_mine = ['fp-3', 'fp-4', 'rt-4', 'mh-4', 'bt-8', 'fp-8', 'mh-10', 'bt-10', 'rt-10', 'mh-11', 'bt-12', 'fp-13', 'mh-13', 'bt-14', 'mh-14', 'rt-14', 'mh-15']
list_outside = ['rt-3', 'bt-3', 'bt-5', 'mh-6', 'fp-6', 'rt-7', 'bt-7', 'bt-9', 'rt-9', 'mh-9', 'fp-10', 'bt-11', 'bt-13', 'rt-13', 'fp-15', 'rt-15', 'j-17',
                'mh-3', 'bt-4', 'fp-5', 'mh-5', 'rt-5', 'bt-6', 'rt-6', 'mh-7', 'fp-7', 'rt-8', 'mh-8', 'fp-9', 'rt-11', 'fp-11', 'fp-12', 'rt-12', 'j-16',
                'mh-12', 'fp-14', 'bt-15']
list_outside1 = ['rt-3', 'bt-3', 'bt-5', 'mh-6', 'fp-6', 'rt-7', 'bt-7', 'bt-9', 'rt-9', 'mh-9', 'fp-10', 'bt-11', 'bt-13', 'rt-13', 'fp-15', 'rt-15', 'j-17']
list_outside2 = ['mh-3', 'bt-4', 'fp-5', 'mh-5', 'rt-5', 'bt-6', 'rt-6', 'mh-7', 'fp-7', 'rt-8', 'mh-8', 'fp-9', 'rt-11', 'fp-11', 'fp-12', 'rt-12', 'j-16']
list_base = ['mh-12', 'fp-14', 'bt-15']


# 列出所有可能的顺子
def find_all_shunzi(list_input):
    list_input = _remove_duplicate(list_input)
    list_link = []
    list_return = []
    for i, item in enumerate(list_input):
        if i == 0:
            list_link.append(item)
            continue
        if int(item) == int(list_link[-1]) + 1:
            list_link.append(item)
            if len(list_link) > 4:
                list_return.append(list_link[-5:])
            continue
        if len(list_link) > 4 and len(list_input) - i - 1 < 5:
            break
        if len(list_link) > 4:
            list_return.append(list_link)
        list_link = [item]
    if len(list_link) > 4:
        if list_link != list_return[-1]:
            list_return.append(list_link)
        return list_return
    return False
    #   input ['3', '4', '4', '4', '8', '8', '10', '10', '10', '11', '12', '13', '13', '14', '14', '14', '15']
    #   output [['10', '11', '12', '13', '14'], ['11', '12', '13', '14', '15'], ['10', '11', '12', '13', '14', '15']]


# 列出所有可能的三不带
def find_all_sanbudai(list_input):
    list_input = _extract_num(list_input)
    sets = {}
    list_return = []
    for item in list_input:
        if sets.get(item, False):
            sets[item] = str(int(sets[item]) + 1)
            continue
        sets[item] = '1'
    for k in sets:
        if sets[k] == '3':
            list_return.append([k, k, k])
    if len(list_return) == 0:
        return False
    return list_return
    # input ['3', '4', '4', '4', '8', '8', '10', '10', '10', '11', '12', '13', '13', '14', '14', '14', '15']
    # output [['4', '4', '4'], ['10', '10', '10'], ['14', '14', '14']]


# 列出所有可能的三带一（不拆双和炸）
def find_all_sandaiyi(list_input):
    list_input = _extract_num(list_input)
    sets = {}
    list_triple = []
    list_single = []
    list_return = []
    for item in list_input:
        if sets.get(item, False):
            sets[item] = str(int(sets[item]) + 1)
            continue
        sets[item] = '1'
    for k in sets:
        if sets[k] == '3':
            list_triple.append(k)
        if sets[k] == '1':
            list_single.append(k)
    for three in list_triple:
        for one in list_single:
            list_return.append([three, three, three, one])
    if len(list_return) == 0:
        return False
    return list_return
    # input ['3', '4', '4', '4', '8', '8', '10', '10', '10', '11', '12', '13', '13', '14', '14', '14', '15']
    # output [['4', '4', '4', '3'], ['4', '4', '4', '11'], ['4', '4', '4', '12'], ['4', '4', '4', '15'], ['10', '10', '10', '3'], ['10', '10', '10', '11'], ['10', '10', '10', '12'], ['10', '10', '10', '15'], ['14', '14', '14', '3'], ['14', '14', '14', '11'], ['14', '14', '14', '12'], ['14', '14', '14', '15']]


# 列出所有可能的三带一对（不拆三和炸）
def find_all_sandaiyidui(list_input):
    list_input = _extract_num(list_input)
    sets = {}
    list_triple = []
    list_double = []
    list_return = []
    for item in list_input:
        if sets.get(item, False):
            sets[item] = str(int(sets[item]) + 1)
            continue
        sets[item] = '1'
    for k in sets:
        if sets[k] == '3':
            list_triple.append(k)
        if sets[k] == '2':
            list_double.append(k)
    for three in list_triple:
        for double in list_double:
            list_return.append([three, three, three, double, double])
    if len(list_return) == 0:
        return False
    return list_return
    # input ['3', '4', '4', '4', '8', '8', '10', '10', '10', '11', '12', '13', '13', '14', '14', '14', '15']
    # output [['4', '4', '4', '8', '8'], ['4', '4', '4', '13', '13'], ['10', '10', '10', '8', '8'], ['10', '10', '10', '13', '13'], ['14', '14', '14', '8', '8'], ['14', '14', '14', '13', '13']]


# 列出所有可能的对子
def find_all_duizi(list_input):
    list_input = _extract_num(list_input)
    sets = {}
    list_return = []
    for item in list_input:
        if sets.get(item, False):
            sets[item] = str(int(sets[item]) + 1)
            continue
        sets[item] = '1'
    for k in sets:
        if sets[k] == '2':
            list_return.append([k, k])
    if len(list_return) == 0:
        return False
    return list_return
    # input ['3', '4', '4', '4', '8', '8', '10', '10', '10', '11', '12', '13', '13', '14', '14', '14', '15']
    # output [['8', '8'], ['13', '13']]


# 列出所有可能的四带二(不拆三和炸)
def find_all_sidaier(list_input):
    list_input = _extract_num(list_input)
    sets = {}
    list_quadra = []
    list_single = []
    list_return_temp = []
    list_return = []
    for item in list_input:
        if sets.get(item, False):
            sets[item] = str(int(sets[item]) + 1)
            continue
        sets[item] = '1'
    for k in sets:
        if sets[k] == '4':
            list_quadra.append(k)
        if sets[k] == '1':
            list_single.append(k)
    for quadra in list_quadra:
        for single in list_single:
            list_return_temp.append([quadra, quadra, quadra, quadra, single])
    for item_return in list_return_temp:
        for single in list_single:
            if single != item_return[-1]:
                list_return.append(item_return + [single])
    if len(list_return) == 0:
        return False
    return list_return
    # input ['3', '4', '4', '4', '8', '8', '10', '10', '10', '11', '12', '13', '13', '14', '14', '14', '14']
    # output [['14', '14', '14', '14', '3', '11'], ['14', '14', '14', '14', '3', '12'], ['14', '14', '14', '14', '11', '3'], ['14', '14', '14', '14', '11', '12'], ['14', '14', '14', '14', '12', '3'], ['14', '14', '14', '14', '12', '11']]


# 列出所有可能的四带两对(不拆三)
def find_all_sidailiangdui(list_input):
    list_input = _extract_num(list_input)
    sets = {}
    list_quadra = []
    list_double = []
    list_return_temp = []
    list_return = []
    for item in list_input:
        if sets.get(item, False):
            sets[item] = str(int(sets[item]) + 1)
            continue
        sets[item] = '1'
    for k in sets:
        if sets[k] == '4':
            list_quadra.append(k)
        if sets[k] == '2':
            list_double.append(k)
    for quadra in list_quadra:
        for double in list_double:
            list_return_temp.append([quadra, quadra, quadra, quadra, double, double])
    for item_return in list_return_temp:
        for double in list_double:
            if double != item_return[-1]:
                list_return.append(item_return + [double, double])

    # remove duplicate
    for i, item in enumerate(list_return):
        if i == 0:
            continue
        if _sort_list(item) == _sort_list(list_return[i-1]):
            list_return.remove(item)

    if len(list_return) == 0:
        return False
    return list_return
    # input ['3', '4', '4', '4', '8', '8', '10', '10', '10', '11', '12', '13', '13', '14', '14', '14', '14']
    # output [['14', '14', '14', '14', '8', '8', '13', '13']]


# 列出所有可能的炸弹
def find_all_zhadan(list_input):
    list_input = _extract_num(list_input)
    sets = {}
    list_return = []
    for item in list_input:
        if sets.get(item, False):
            sets[item] = str(int(sets[item]) + 1)
            continue
        sets[item] = '1'
    for k in sets:
        if sets[k] == '4':
            list_return.append([k, k, k, k])
    if len(list_return) == 0:
        return False
    return list_return
    # input ['3', '4', '4', '4', '8', '8', '10', '10', '10', '11', '12', '13', '13', '14', '14', '14', '14']
    # output [['14', '14', '14', '14']]


# 列出所有可能的飞机不带
# todo: 判断三连飞，四连飞情况
def find_all_feijibudai(list_input):
    list_input = _extract_num(list_input)
    sets = {}
    list_connect_three = []
    for item in list_input:
        if sets.get(item, False):
            sets[item] = str(int(sets[item]) + 1)
            continue
        sets[item] = '1'
    last_set = {}
    for k in sets:
        if last_set and sets[k] == '3' and list(last_set.values())[0] == '3':
            lk = list(last_set.keys())[0]
            list_connect_three.append([lk, lk, lk, k, k, k])
        last_set = {k: sets[k]}
    return list_connect_three


# 列出所有可能的飞机带单
# todo: 判断三连飞，四连飞情况
def find_all_feijidaidan(list_input):
    list_input = _extract_num(list_input)
    sets = {}
    list_connect_three = []
    list_single = []
    list_add_one = []
    list_return_temp = []
    list_return = []
    for item in list_input:
        if sets.get(item, False):
            sets[item] = str(int(sets[item]) + 1)
            continue
        sets[item] = '1'
    last_set = {}
    for k in sets:
        if last_set and sets[k] == '3' and list(last_set.values())[0] == '3':
            lk = list(last_set.keys())[0]
            list_connect_three.append([lk, lk, lk, k, k, k])
        if sets[k] == '1':
            list_single.append(k)
        last_set = {k: sets[k]}
    for sixes in list_connect_three:
        for single in list_single:
            list_add_one.append(sixes + [single])
    for sixes in list_add_one:
        for single in list_single:
            if sixes[-1] != single:
                list_return_temp.append(_sort_list(sixes + [single]))

    # remove duplicate
    for item in list_return_temp:
        if _sort_list(item) not in list_return:
            list_return.append(item)

    return list_return
    # input ['3', '4', '4', '4', '5', '5', '5', '10', '10', '11', '12', '13', '13', '14', '14', '14', '14']
    # output [['3', '4', '4', '4', '5', '5', '5', '11'], ['3', '4', '4', '4', '5', '5', '5', '12'], ['4', '4', '4', '5', '5', '5', '11', '12']]


# 列出所有可能的飞机带双
# todo: 判断三连飞，四连飞情况
def find_all_feijidaishuang(list_input):
    list_input = _extract_num(list_input)
    sets = {}
    list_connect_three = []
    list_double = []
    list_add_one = []
    list_return_temp = []
    list_return = []
    for item in list_input:
        if sets.get(item, False):
            sets[item] = str(int(sets[item]) + 1)
            continue
        sets[item] = '1'
    last_set = {}
    for k in sets:
        if last_set and sets[k] == '3' and list(last_set.values())[0] == '3':
            lk = list(last_set.keys())[0]
            list_connect_three.append([lk, lk, lk, k, k, k])
        if sets[k] == '2':
            list_double.append(k)
        last_set = {k: sets[k]}
    for sixes in list_connect_three:
        for double in list_double:
            list_add_one.append(sixes + [double, double])
    for sixes in list_add_one:
        for double in list_double:
            if sixes[-1] != double:
                list_return_temp.append(_sort_list(sixes + [double, double]))

    # remove duplicate
    for item in list_return_temp:
        if _sort_list(item) not in list_return:
            list_return.append(item)

    return list_return
    # input ['3', '4', '4', '4', '5', '5', '5', '10', '10', '11', '11', '13', '13', '14', '14', '14', '14']
    # output [['4', '4', '4', '5', '5', '5', '10', '10', '11', '11'], ['4', '4', '4', '5', '5', '5', '10', '10', '13', '13'], ['4', '4', '4', '5', '5', '5', '11', '11', '13', '13']]


# 发牌
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


# 输入牌型列表，输出牌型(或非法牌型)
def find_type(picks):
    num_list = _extract_num(picks)

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
# todo: 判断三连飞，四连飞情况
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


# 输入牌面列表，输出数字(字符串类型)列表
def _extract_num(picks):
    num_list = []
    for pick in picks:
        num = pick.split('-')[1]
        num_list.append(num)
    num_list.sort(key=lambda e: int(e))
    print(num_list)
    return num_list


# 数字(字符串)列表去重
def _remove_duplicate(picks):
    return sorted(list(set(_extract_num(picks))), key=lambda e: int(e))


# 数字(字符串)列表排序
def _sort_list(num_list):
    return sorted(num_list, key=lambda e: int(e))



# print(find_type(['bt-3', 'rt-3', 'ft-3', 'ft-3', 'mh-4', 'mh-4']))
# set_picks()
print(find_all_feijidaidan(['fp-3', 'fp-4', 'rt-4', 'mh-4', 'bt-5', 'fp-5', 'mh-5', 'bt-10', 'rt-10', 'mh-11', 'bt-12', 'fp-13', 'mh-13', 'bt-14', 'mh-14', 'rt-14', 'mh-14']))