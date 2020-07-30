import json
import os
from glob import glob


def convert(_dir, version, edition ='pc'):
    fp = open(os.path.join(_dir, 'dataPaths.json'))
    datapaths = json.load(fp)
    fp.close()
    data = _grabdata(_dir, datapaths[edition][version])
    ret = {}
    if 'blocks' in data:
        ret['blocks'] = _by_id(data['blocks'])
        ret['blocks_name'] = _by_name(data['blocks'])
        ret['blocks_list'] = data['blocks']
    if 'items' in data:
        ret['items'] = _by_id(data['items'])
        ret['items_name'] = _by_name(data['items'])
        ret['items_list'] = data['items']
    if 'biomes' in data:
        ret['biomes'] = _by_id(data['biomes'])
        ret['biomes_list'] = data['biomes']
    if 'recipes' in data:
        ret['recipes'] = data['recipes']
    if 'instruments' in data:
        ret['instruments'] = _by_id(data['instruments'])
        ret['instruments_list'] = data['instruments']
    if 'materials' in data:
        ret['materials'] = data['materials']
    if 'entities' in data:
        ret['mobs'] = _by_id(_filter('type', 'mob', data['entities']))
        ret['objects'] = _by_id(_filter('type', 'object', data['entities']))
        ret['entities_name'] = _by_name(data['entities'])
        ret['entities_list'] = data['entities']
    if 'protocol' in data:
        ret['protocol'] = data['protocol']
    if 'windows' in data:
        ret['windows'] = _by_id(data['windows'])
        ret['windows_name'] = _by_name(data['windows'])
        ret['windows_list'] = data['windows']
    if 'effects' in data:
        ret['effects'] = _by_id(data['effects'])
        ret['effects_name'] = _by_name(data['effects'])
        ret['effects_list'] = data['effects']
    if 'version' in data:
        ret['version'] = data['version']
    if 'particles' in data:
        ret['particles'] = _by_id(data['particles'])
        ret['particles_name'] = _by_name(data['particles'])
        ret['particles_list'] = data['particles']

    def find_item_or_block(find):
        if isinstance(find, int):  # by id
            return find_by(find, ret['items'], ret['blocks'])
        else:  # by name
            return find_by(find, ret['items_name'], ret['blocks_name'])

    ret['find_item_or_block'] = find_item_or_block

    return ret


def _grabdata(_dir, datapaths):
    data = {}
    for category, folder in datapaths.items():
        with open(os.path.join(_dir, folder, f'{category}.json')) as fp:
            data[category] = json.load(fp)
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
