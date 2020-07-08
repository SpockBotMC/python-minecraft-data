# Contribute

## How to update minecraft-data

For each minecraft_version :
* cd minecraft_data/minecraft_version/data
* git pull
* git checkout tags/[latest minecraft-data release]

Then in the main dir git add .

You can then create a commit whenever you're ready

## How to publish a new version

1. Update setup.py to the minecraft-data release version
2. Add changes in doc/history.md (see what changed in minecraft-data)
3. Create a commit with message "Release VERSION_NUMBER"
4. git tag VERSION_NUMBER
5. git push && git push --tags
6. python setup.py sdist upload -r pypi
