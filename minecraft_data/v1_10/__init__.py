import os
import sys

from minecraft_data.tools import convert


_dir = os.path.join(os.path.dirname(__file__), "../data/data/pc/1.10")

for name, data in convert(_dir).items():
    setattr(sys.modules[__name__], name, data)
