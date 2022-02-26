def delta_finder(ll1, ll2):
    from math import cos, sqrt, radians
    ll1 = list(map(lambda x: float(x), ll1))
    ll2 = list(map(lambda x: float(x), ll2))
    radians_lattitude = radians((ll1[1] + ll2[1]) / 2.)
    lat_lon_factor = cos(radians_lattitude)
    if 0 >= ll1[1] >= ll2[1]:
        length = abs(ll2[1]) - abs(ll1[1])
    elif 0 >= ll2[1] >= ll1[1]:
        length = abs(ll1[1]) - abs(ll2[1])
    elif ll2[1] <= 0 <= ll1[1]:
        length = abs(ll2[1]) + ll1[1]
    elif ll1[1] <= 0 <= ll2[1]:
        length = abs(ll1[1]) + ll2[1]
    else:
        length = abs(ll1[1] - ll2[1])
    if 0 >= ll1[1] >= ll2[1]:
        width = abs(ll2[0]) - abs(ll1[0])
    elif 0 >= ll2[1] >= ll1[1]:
        width = abs(ll1[0]) - abs(ll2[0])
    elif ll2[0] <= 0 <= ll1[0]:
        width = abs(ll2[0]) + ll1[0]
    elif ll1[0] <= 0 <= ll2[0]:
        width = abs(ll1[0]) + ll2[0]
    else:
        width = abs(ll1[0] - ll2[0])
    width = width * lat_lon_factor * 111
    length = length * 111
    return sqrt(width * width + length * length)


def define_working_hours(responses):
    sp = []
    for elem in responses['features']:
        f = False
        for elem1 in elem['properties']['CompanyMetaData']['Hours']['Availabilities']:
            if 'TwentyFourHours' in elem1:
                if elem1['TwentyFourHours']:
                    sp.append(f"{','.join(map(str, elem['geometry']['coordinates']))},pm2gnm")
                    f = True
                    break
            if 'Intervals' in elem1:
                f = True
                sp.append(f"{','.join(map(str, elem['geometry']['coordinates']))},pm2blm")
                break
        if not f:
            sp.append(f"{','.join(map(str, elem['geometry']['coordinates']))},pm2grm")
    return sp
