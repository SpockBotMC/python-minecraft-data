import os
import sys

from minecraft_data.tools import convert


class mod(sys.modules[__name__].__class__):
    def __call__(self, version):
        _dir = os.path.join(
            os.path.dirname(__file__), "data/data/"
        )
        return type(version, (object,), convert(_dir, version))


sys.modules[__name__].__class__ = mod
