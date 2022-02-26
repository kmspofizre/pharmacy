def delta_finder(ll1, ll2):
    from math import cos, sqrt
    width, length = 0, 0
    ll1 = list(map(lambda x: cos(float(x)) * 111.3, ll1))
    ll2 = list(map(lambda x: cos(float(x)) * 111.3, ll2))
    if 0 >= ll1[0] >= ll2[0]:
        length = abs(ll2[0]) - abs(ll1[0])
    elif 0 >= ll2[0] >= ll1[0]:
        length = abs(ll1[0]) - abs(ll2[0])
    elif ll2[0] <= 0 <= ll1[0]:
        length = abs(ll2[0]) + ll1[0]
    elif ll1[0] <= 0 <= ll2[0]:
        length = abs(ll1[0]) + ll2[0]
    elif ll1[0] >= 0 and ll1[0] >= ll2[0] >= 0:
        length = ll1[0] - ll2[0]
    elif ll2[0] >= 0 and ll2[0] >= ll1[0] >= 0:
        length = ll2[0] - ll1[0]
    if 0 >= ll1[1] >= ll2[1]:
        width = abs(ll2[1]) - abs(ll1[1])
    elif 0 >= ll2[1] >= ll1[1]:
        width = abs(ll1[1]) - abs(ll2[1])
    elif ll2[1] <= 0 <= ll1[1]:
        width = abs(ll2[1]) + ll1[1]
    elif ll1[1] <= 0 <= ll2[1]:
        width = abs(ll1[1]) + ll2[1]
    elif ll1[1] >= 0 and ll1[1] >= ll2[1] >= 0:
        width = ll1[1] - ll2[1]
    elif ll2[1] >= 0 and ll2[1] >= ll1[1] >= 0:
        width = ll2[1] - ll1[1]
    return sqrt(width * width + length * length)


def define_working_hours(responses):
    pass