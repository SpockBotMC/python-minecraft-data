import json
import os
from glob import glob


def convert(dir):
    data = _grabdata(dir)
    ret = {
        'blocks': _byId(data['blocks']),
        'blocksByName': _byName(data['blocks']),
        'blocksArray': data['blocks'],
        'items': _byId(data['items']),
        'itemsByName': _byName(data['items']),
        'itemsArray': data['items'],
        'biomes': _byId(data['biomes']),
        'biomesArray': data['biomes'],
        'recipes': data['recipes'],
        'instruments': _byId(data['instruments']),
        'intrumentsArray': data['instruments'],
        'materials': data['materials'],
        'entities': _byId(data['entities']),
        'entitiesByName': _byName(data['entities']),
        'entitiesArray': data['entities'],
        'protocol': data['protocol'],
        'windows': _byId(data['windows']),
        'windowsByName': _byName(data['windows']),
        'windowsArray': data['windows'],
    }
    def findItemOrBlockById(id):
        return findBy(id, ret['items'], ret['blocks'])

    def findItemOrBlockByName(name):
        return findBy(name, ret['itemsByName'], ret['blocksByName'])

    ret['findItemOrBlockById'] = findItemOrBlockById
    ret['findItemOrBlockByName'] = findItemOrBlockByName

    return ret


def _grabdata(dir):
    data = dict()
    for filename in glob(os.path.join(dir, "data/enums/")+"*.json"):
        with open(filename) as fp:
            base = os.path.splitext(os.path.basename(filename))[0]
            doc = json.load(fp)
            data[base] = doc
    return data


def _byId(data):
    return _by('id', data)


def _byName(data):
    return _by('name', data)


def _by(key, data):
    return {item[key]: item for item in data}


def findBy(key, *args):
    for arg in args:
        if key in arg:
            return arg[key]
    return None

