import json
import os
from glob import glob


def convert(_dir, version, edition ='pc'):
    with open(os.path.join(_dir, 'dataPaths.json')) as f:
        datapaths = json.load(f)
    data = _grabdata(_dir, datapaths[edition][version])
    ret = {}
    for datum in ('recipes', 'materials', 'protocol', 'version',
            'blockCollisionShapes', 'protocolComments', 'loginPacket',
            'commands', 'tints'):
        if datum in data:
            ret[datum] = data[datum]
    for datum in ('blocks', 'items', 'windows', 'effects', 'particles',
            'biomes', 'instruments', 'enchantments', 'foods', 'mapIcons'):
        if datum in data:
            ret[datum] = _by_id(data[datum])
            ret[f"{datum}_name"] = _by_name(data[datum])
            ret[f"{datum}_list"] = data[datum]
    for datum in ('blockLoot', 'entityLoot'):
        if datum in data:
            ret[datum] = _parse_loot(data[datum], datum)
            ret[f"{datum}_list"] = data[datum]
    if 'entities' in data:
        ret['mobs'] = _by_id(_filter('type', 'mob', data['entities']))
        ret['objects'] = _by_id(_filter('type', 'object', data['entities']))
        ret['entities_name'] = _by_name(data['entities'])
        ret['entities_list'] = data['entities']


    def find_item_or_block(find):
        if isinstance(find, int):  # by id
            return find_by(find, ret['items'], ret['blocks'])
        else:  # by name
            return find_by(find, ret['items_name'], ret['blocks_name'])

    ret['find_item_or_block'] = find_item_or_block

    return ret


def commondata(_dir, edition = 'pc'):
    ret = {}
    common_path = os.path.join(_dir, edition, 'common')
    for common_file in os.listdir(common_path):
        key = common_file.split('.', 1)[0]
        with open(os.path.join(common_path, common_file)) as f:
            data = json.load(f)
            ret.update({key: data})
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

def _parse_loot(data, loot_string):
    field = loot_string[:loot_string.rfind('Loot')]
    return {d[field]: d['drops'] for d in data}

def _by(key, data):
    return {item[key]: item for item in data}


def _filter(key, val, data):
    return [d for d in data if d[key] == val]


def find_by(key, *args):
    for arg in args:
        if key in arg:
            return arg[key]
    return None
