def size_maker(responses_pack): #list(d.keys()) - response у географических, type у организаций
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
                if left_bottom[0] < points['left'] or points['left'] == 'Not defined':
                    points['left'] = left_bottom[0]
                if left_bottom[1] < points['bottom'] or points['bottom'] == 'Not defined':
                    points['bottom'] = left_bottom[0]
                if right_top[0] > points['right'] or points['right'] == 'Not defined':
                    points['right'] = right_top[0]
                if right_top[1] > points['top'] or points['top'] == 'Not defined':
                    points['top'] = right_top[1]
        elif list(elem.keys())[0] == 'type':
            for organization in elem['features']:
                if organization['properties']['boundedBy'][0][0] < points['left'] \
                        or points['left'] == 'Not defined':
                    points['left'] = organization['properties']['boundedBy'][0][0]
                if organization['properties']['boundedBy'][0][1] < points['bottom'] \
                        or points['bottom'] == 'Not defined':
                    points['bottom'] = organization['properties']['boundedBy'][0][1]
                if organization['properties']['boundedBy'][1][0] > points['right'] \
                        or points['right'] == 'Not defined':
                    points['right'] = organization['properties']['boundedBy'][1][0]
                if organization['properties']['boundedBy'][1][1] > points['top'] \
                        or points['top'] == 'Not defined':
                    points['top'] = organization['properties']['boundedBy'][1][1]

