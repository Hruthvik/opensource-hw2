import json
import yaml
import os
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]
ext = os.path.splitext(file1)[-1].lower()

if ext == ".yml" or ext == ".yaml":
    with open(file1, 'r') as yml_file:
        content = yaml.safe_load(yml_file)
    with open(file2, 'w') as json_file:
        json.dump(content, json_file)
if ext == ".json" or ext == "jsn":
    with open(file1, 'r') as json_file:
        content = json.load(json_file)
    with open(file2, 'w') as yml_file:
        yaml.dump(content,yml_file,default_flow_style=False)
