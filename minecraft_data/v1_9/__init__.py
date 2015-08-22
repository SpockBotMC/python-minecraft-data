import os
import sys

from minecraft_data.tools import convert


_dir = os.path.dirname(__file__)

for name, data in convert(_dir).items():
    setattr(sys.modules[__name__], name, data)

