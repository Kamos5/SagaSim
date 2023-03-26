import json

def loadFiles(file='diseases'):
    # Opening JSON file
    with open('inputFiles/' + file +'.json', encoding="utf-8") as json_file:
        data = json.load(json_file)

    return data
