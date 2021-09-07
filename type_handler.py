from util import extract_num


# 输入牌型列表，输出牌型(或非法牌型)
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

