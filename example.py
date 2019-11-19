import minecraft_data
mcd = minecraft_data("1.13.2")

print(mcd.version)

print(mcd.find_item_or_block(1))
print(mcd.find_item_or_block('stone'))

print(mcd.recipes['5'][0])

print(mcd.windows['minecraft:brewing_stand'])

print(mcd.effects_name['Haste'])
