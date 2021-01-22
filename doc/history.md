## 2.74.0
 * Update minecraft-data to 2.74.0

## 2.73.1
 * Update minecraft-data to 2.73.1

## 2.71.0
 * Update minecraft-data to 2.71.0
 * Add following data: commands, mapIcons

## 2.70.1
 * Update minecraft-data to 2.70.1

## 2.70.0
 * Update minecraft-data to 2.70.0

## 2.69.0
 * Update minecraft-data to 2.69.0
 * Added loginPacket data

## 2.67.0
 * Update minecraft-data to 2.67.0

## 2.65.0
 * Update minecraft-data to 2.65.0
 * Made the following data accessible: blockCollisionShapes, enchantments, foods, protocolComments, particles
 * Instruments and biomes now provide _name access

## 2.64.0
 * Update minecraft-data to 2.64.0

## 2.63.0
 * Update minecraft-data to 2.63.0

## 2.62.1
 * Several changes since project semi-abandonment
 * Project now uses a more generic approach to adapting minecraft-data schema
 * Added support for Minecraft PE
 * Project now tracks with minecraft-data release number
 * Update minecraft-data to 2.62.1

## 0.5.1
 * update minecraft-data to 2.2.0
   * still only pc versions are available as imports for now
   * note that although the file structure of minecraft-data changed, the imports are still `minecraft_data.vX`
 * add `v1_10`

## 0.5.0
 * update minecraft-data
   * solve the entities.json savegame/protocol ID confusion
 * remove `entities`, use `mobs` and `objects` instead (they have overlapping IDs)

## 0.4.0
 * update minecraft-data
   * up to date 1.9 blocks, items, recipes
   * some protocol.json updates
   * add status effects
   * add version
   * fixes in windows.json : fix in brewing stand and add container window

## 0.3.4
 * fix package_data
 * update minecraft_data : some item.json fixes

## 0.3.3
 * small fix about os.path.join

## 0.3.2
 * update to new minecraft-data file location

## 0.3.1
 * repair README links for pypi

## 0.3.0
 * changed function names to follow pep8

## 0.2.0
 * add windows
 * update protocol schema

## 0.1.1
 * fix pypi package : include json files
 * add licence file

## 0.1.0
 * provide : id-indexed data, name-indexed data, unindexed data and two functions to find items or blocks
