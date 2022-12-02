import requests
import json
import ast

baseurl = 'https://rickandmortyapi.com/api/'
endpoint = 'character'
parsed = []


def main_request(base_url, endp):
    r = requests.get(baseurl + endpoint)
    return r.json()


def get_pages(response):
    return response['info']['pages']


def parse_json_names(response):
    for item in response['results']:
        name = str(item['name'])
        episode = str(len(item['episode']))
        parsed.append(name + ' ' +episode)
    return str(parsed)


def print_data(response):
    for item in response['results']:
        print(item['name'], len(item['episode']))
    return

data = main_request(baseurl, endpoint)

# wraps string data to double quotes:json-quotes-wrap.md
json_string = json.dumps(ast.literal_eval(parse_json_names(data)))
jsonFile = open("../api-testing/data.json", "w")
jsonFile.write(json_string)
jsonFile.close()
# name = json.dumps(data['results'][0]['name'])
# episodes = json.dumps(data['results'][0]['episode'])
