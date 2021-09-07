# 输入牌面列表，输出数字(字符串类型)列表
def extract_num(picks):
    num_list = []
    for pick in picks:
        num = pick.split('-')[1]
        num_list.append(num)
    num_list.sort(key=lambda e: int(e))
    # print(num_list)
    return num_list


# 数字(字符串)列表去重
def remove_duplicate(picks):
    return sorted(list(set(extract_num(picks))), key=lambda e: int(e))


# 数字(字符串)列表排序
def sort_list(num_list):
    return sorted(num_list, key=lambda e: int(e))