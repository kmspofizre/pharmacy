from io import BytesIO
import requests
from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('address', metavar='str', nargs='+',
                    type=str, help='address to show')
parser.add_argument('--delta', '-delta', default='0.005', type=str,
                    help='delta')
args = parser.parse_args()
toponym_to_find = " ".join(args.address)
delta = args.delta
geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

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
map_params = {
    "ll": ",".join([toponym_longitude, toponym_lattitude]),
    "spn": ",".join([delta, delta]),
    "l": "map",
    "pt": ",".join([toponym_longitude, toponym_lattitude]) + ",org"
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(
    response.content)).show()
