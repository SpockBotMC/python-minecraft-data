from minecraft_data.v1_8 import recipes

print(recipes["5"][0])

from minecraft_data.v1_9 import recipes as recipes2

print(recipes2["5"][0])

from minecraft_data.v1_8 import findItemOrBlockById, findItemOrBlockByName

print(findItemOrBlockById(1))

print(findItemOrBlockByName("stone"))

from minecraft_data.v1_8 import windows as windows

print(windows["minecraft:brewing_stand"])