def delta_finder(ll1, ll2):
    from math import sin, cos, acos
    ll1 = list(map(float, ll1))
    ll2 = list(map(float, ll2))
    return 111.2 * acos(sin(ll1[0]) * sin(ll2[0]) + cos(ll1[0]) * cos(ll2[0]) * cos(ll2[1] - ll1[1]))