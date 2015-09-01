# Contribute

## How to update minecraft-data

For each minecraft_version : 
* cd minecraft_data/minecraft_version/data
* git pull

Then in the main dir git add .

You can then create a commit whenever you're ready

## How to publish a new version

1. decide the number of the new version (see http://semver.org/)
2. put it in setup.py
3. add changes in doc/history.md (see what changed in minecraft-data)
4. create a commit with message "Release VERSION_NUMBER"
5. git tag VERSION_NUMBER
6. git push && git push --tags
7. python setup.py sdist upload -r pypi
