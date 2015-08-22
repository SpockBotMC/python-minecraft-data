import json


def read_json(name, version):
    f = open('data/'+version+'/enums/'+name+'.json', 'r')
    return json.loads(f.read())

blocks = read_json('blocks', '1.8')
biomes = read_json('biomes', '1.8')
items = read_json('items', '1.8')
recipes = read_json('recipes', '1.8')
instruments = read_json('instruments', '1.8')
materials = read_json('materials', '1.8')
entities = read_json('entities', '1.8')
protocol = read_json('protocol', '1.8')
