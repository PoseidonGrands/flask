def number_split(num):
    res = []
    num = str(num)
    for i in range(len(num), 0, -3):
        res.append(num[max(i - 3, 0):i])
    return ','.join(res[::-1])
