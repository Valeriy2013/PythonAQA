import json
import os.path
import pathlib


def get_json_data(file):
    path = get_full_path(file)
    with open(path) as json_file:
        json_data = json.load(json_file)
        return json_data


def get_full_path(file):
    path = pathlib.Path(__file__).parent.parent.resolve()
    return os.path.join(path, "DataProvider/" + file)
