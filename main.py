from io import BytesIO
import requests
from PIL import Image
import argparse
from size_maker import size_maker
from delta_finder import delta_finder

parser = argparse.ArgumentParser()
parser.add_argument('address', metavar='str', nargs='+',
                    type=str, help='address to show')
parser.add_argument('--delta', '-delta', default='0.005', type=str,
                    help='delta')
args = parser.parse_args()
toponym_to_find = " ".join(args.address)
geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
search_api_server = "https://search-maps.yandex.ru/v1/"

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)

if not response:
    pass
json_response = response.json()
toponym = json_response["response"]["GeoObjectCollection"][
    "featureMember"][0]["GeoObject"]
toponym_coodrinates = toponym["Point"]["pos"]
toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
search_params = {
    "apikey": "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3",
    "text": "аптека",
    "lang": "ru_RU",
    "ll": ",".join([toponym_longitude, toponym_lattitude]),
    "type": "biz",
    "results": '2'
}

pharmacy_response = requests.get(search_api_server, params=search_params).json()
delta, ll = size_maker([pharmacy_response, json_response])
map_params = {
    "ll": ll,
    "spn": delta,
    "l": "map",
    "pt": f'{",".join([toponym_longitude, toponym_lattitude])},org~'
          f'{",".join(map(str, pharmacy_response["features"][0]["geometry"]["coordinates"]))}'
}
map_api_server = "http://static-maps.yandex.ru/1.x/"
map_response = requests.get(map_api_server, params=map_params)
delta_r = delta_finder(toponym_coodrinates.split(), pharmacy_response["features"][0]["geometry"]["coordinates"])
print(pharmacy_response['features'][0]['properties']['name'])
print(pharmacy_response['features'][0]['properties']['description'])
print(pharmacy_response['features'][0]['properties']['CompanyMetaData']['Hours']['text'])
print(f"{round(delta_r, 2)} км")
Image.open(BytesIO(
    map_response.content)).show()
