import os
import jsonref


class DataJsonReader(dict):
    def __init__(self, file_name):
        base_path = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(base_path, file_name)
        base_uri = f"file://{base_path}/"

        with open(json_path) as input_file:
            self.update(jsonref.loads(input_file.read(),
                                      base_uri=base_uri, jsonschema=True))
