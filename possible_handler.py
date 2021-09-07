from util import extract_num, remove_duplicate, sort_list


# 列出所有可能的顺子
def find_all_shunzi(list_input):
    list_input = remove_duplicate(list_input)
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
    list_input = extract_num(list_input)
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
    list_input = extract_num(list_input)
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
    list_input = extract_num(list_input)
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
    list_input = extract_num(list_input)
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
    list_input = extract_num(list_input)
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
    list_input = extract_num(list_input)
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
        if sort_list(item) == sort_list(list_return[i-1]):
            list_return.remove(item)

    if len(list_return) == 0:
        return False
    return list_return
    # input ['3', '4', '4', '4', '8', '8', '10', '10', '10', '11', '12', '13', '13', '14', '14', '14', '14']
    # output [['14', '14', '14', '14', '8', '8', '13', '13']]


# 列出所有可能的炸弹
def find_all_zhadan(list_input):
    list_input = extract_num(list_input)
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
    list_input = extract_num(list_input)
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

    if len(list_connect_three) == 0:
        return False
    return list_connect_three


# 列出所有可能的飞机带单
# todo: 判断三连飞，四连飞情况
def find_all_feijidaidan(list_input):
    list_input = extract_num(list_input)
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
                list_return_temp.append(sort_list(sixes + [single]))

    # remove duplicate
    for item in list_return_temp:
        if sort_list(item) not in list_return:
            list_return.append(item)

    if len(list_return) == 0:
        return False
    return list_return
    # input ['3', '4', '4', '4', '5', '5', '5', '10', '10', '11', '12', '13', '13', '14', '14', '14', '14']
    # output [['3', '4', '4', '4', '5', '5', '5', '11'], ['3', '4', '4', '4', '5', '5', '5', '12'], ['4', '4', '4', '5', '5', '5', '11', '12']]


# 列出所有可能的飞机带双
# todo: 判断三连飞，四连飞情况
def find_all_feijidaishuang(list_input):
    list_input = extract_num(list_input)
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
                list_return_temp.append(sort_list(sixes + [double, double]))

    # remove duplicate
    for item in list_return_temp:
        if sort_list(item) not in list_return:
            list_return.append(item)

    if len(list_return) == 0:
        return False
    return list_return
    # input ['3', '4', '4', '4', '5', '5', '5', '10', '10', '11', '11', '13', '13', '14', '14', '14', '14']
    # output [['4', '4', '4', '5', '5', '5', '10', '10', '11', '11'], ['4', '4', '4', '5', '5', '5', '10', '10', '13', '13'], ['4', '4', '4', '5', '5', '5', '11', '11', '13', '13']]
