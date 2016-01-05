from minecraft_data.v1_8 import find_item_or_block

print(find_item_or_block(1))

print(find_item_or_block("stone"))

from minecraft_data.v1_8 import recipes

print(recipes["5"][0])

from minecraft_data.v1_8 import windows as windows

print(windows["minecraft:brewing_stand"])

from minecraft_data.v1_9 import recipes as recipes2

print(recipes2["5"][0])


from minecraft_data.v1_8 import effects_name

print(effects_name["Haste"])


from minecraft_data.v1_8 import version

print(version)