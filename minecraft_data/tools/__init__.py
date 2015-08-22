import json
import os
from glob import glob


def convert(dir):
    data = dict()
    for filename in glob(os.path.join(dir, "data/enums/")+"*.json"):
        with open(filename) as fp:
            base = os.path.splitext(os.path.basename(filename))[0]
            doc = json.load(fp)
            data[base] = doc
    return data
