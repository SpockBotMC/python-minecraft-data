import json
import os
from glob import glob


def convert(dir):
    data = _grabdata(dir)
    ret = {
        'blocks': _by_id(data['blocks']),
        'blocks_name': _by_name(data['blocks']),
        'blocks_list': data['blocks'],
        'items': _by_id(data['items']),
        'items_name': _by_name(data['items']),
        'items_list': data['items'],
        'biomes': _by_id(data['biomes']),
        'biomes_list': data['biomes'],
        'recipes': data['recipes'],
        'instruments': _by_id(data['instruments']),
        'instruments_list': data['instruments'],
        'materials': data['materials'],
        'mobs': _by_id(_filter('type', 'mob', data['entities'])),
        'objects': _by_id(_filter('type', 'object', data['entities'])),
        'entities_name': _by_name(data['entities']),
        'entities_list': data['entities'],
        'protocol': data['protocol'],
        'windows': _by_id(data['windows']),
        'windows_name': _by_name(data['windows']),
        'windows_list': data['windows'],
        'effects': _by_id(data['effects']),
        'effects_name': _by_name(data['effects']),
        'effects_list': data['effects'],
        'version': data['version']
    }

    def find_item_or_block(find):
        if isinstance(find, int):  # by id
            return find_by(find, ret['items'], ret['blocks'])
        else:  # by name
            return find_by(find, ret['items_name'], ret['blocks_name'])

    ret['find_item_or_block'] = find_item_or_block

    return ret


def _grabdata(dir):
    data = dict()
    for filename in glob(os.path.join(dir, '*.json')):
        with open(filename) as fp:
            base = os.path.splitext(os.path.basename(filename))[0]
            doc = json.load(fp)
            data[base] = doc
    return data


def _by_id(data):
    return _by('id', data)


def _by_name(data):
    return _by('name', data)


def _by(key, data):
    return {item[key]: item for item in data}


def _filter(key, val, data):
    return [d for d in data if d[key] == val]


def find_by(key, *args):
    for arg in args:
        if key in arg:
            return arg[key]
    return None
