import minecraft_data
# Java edition minecraft-data
mcd = minecraft_data("1.13")

print(mcd.version)

print(mcd.find_item_or_block(1))
print(mcd.find_item_or_block('stone'))

print(mcd.recipes['5'][0])

print(mcd.windows['minecraft:brewing_stand'])

print(mcd.effects_name['Haste'])

# Bedrock Edition minecraft-data
mcd_pe = minecraft_data("1.0", "bedrock")

print(mcd_pe.version)
print(mcd_pe.find_item_or_block('stone'))

# Query common data. E.g. to map the protocol version to a minecraft version
protocol_version = 754 # example protocol version
for version in minecraft_data.common().protocolVersions:
    if version["version"] == protocol_version:
        print(version["minecraftVersion"]) # 1.16.5
        break
