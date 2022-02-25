def size_maker(responses_pack):
    points = {
        'left': 'Not defined',
        'right': 'Not defined',
        'top': 'Not defined',
        'bottom': 'Not defined'
    }
    for elem in responses_pack:
        if list(elem.keys())[0] == 'response':
            for geo_object in elem['response']["GeoObjectCollection"]["featureMember"]:
                left_bottom = tuple(map(float, geo_object['GeoObject']['boundedBy']['Envelope']["lowerCorner"].split()))
                right_top = tuple(map(float, geo_object['GeoObject']['boundedBy']['Envelope']["upperCorner"].split()))
                if points['left'] == 'Not defined':
                    points['left'] = left_bottom[0]
                elif left_bottom[0] < points['left']:
                    points['left'] = left_bottom[0]
                if points['bottom'] == 'Not defined':
                    points['bottom'] = left_bottom[1]
                elif left_bottom[1] < points['bottom']:
                    points['bottom'] = left_bottom[1]
                if points['right'] == 'Not defined':
                    points['right'] = right_top[0]
                elif right_top[0] > points['right']:
                    points['right'] = right_top[0]
                if points['top'] == 'Not defined':
                    points['top'] = right_top[1]
                elif right_top[1] > points['top']:
                    points['top'] = right_top[1]
        elif list(elem.keys())[0] == 'type':
            for organization in elem['features']:
                if points['left'] == 'Not defined':
                    points['left'] = organization['properties']['boundedBy'][0][0]
                elif organization['properties']['boundedBy'][0][0] < points['left']:
                    points['left'] = organization['properties']['boundedBy'][0][0]
                if points['bottom'] == 'Not defined':
                    points['bottom'] = organization['properties']['boundedBy'][0][1]
                elif organization['properties']['boundedBy'][0][1] < points['bottom']:
                    points['bottom'] = organization['properties']['boundedBy'][0][1]
                if points['right'] == 'Not defined':
                    points['right'] = organization['properties']['boundedBy'][1][0]
                elif organization['properties']['boundedBy'][1][0] > points['right']:
                    points['right'] = organization['properties']['boundedBy'][1][0]
                if points['top'] == 'Not defined':
                    points['top'] = organization['properties']['boundedBy'][1][1]
                elif organization['properties']['boundedBy'][1][1] > points['top']:
                    points['top'] = organization['properties']['boundedBy'][1][1]
    if points['left'] < 0 and points['right'] < 0:
        delta_1 = abs(points['right']) - abs(points['left'])
        left_right = (abs(points['right']) + abs(points['left']) / 2) * (-1)
    elif points['left'] < 0:
        delta_1 = abs(points['left']) + points['right']
        left_right = (points['left'] + points['right']) / 2
    else:
        delta_1 = points['right'] - points['left']
        left_right = (points['left'] + points['right']) / 2
    if points['bottom'] < 0 and points['top'] < 0:
        delta_2 = abs(points['top']) - abs(points['bottom'])
        bottom_top = (abs(points['bottom']) + abs(points['top']) / 2) * (-1)
    elif points['bottom'] < 0:
        delta_2 = abs(points['bottom']) + points['top']
        bottom_top = (points['bottom'] + points['top']) / 2
    else:
        delta_2 = points['top'] - points['bottom']
        bottom_top = (points['bottom'] + points['top']) / 2
    return f"{str(delta_1)},{str(delta_2)}", f"{str(left_right)},{str(bottom_top)}"

