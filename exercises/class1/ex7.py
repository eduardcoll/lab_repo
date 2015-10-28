#!/user/bin/env

import yaml
import json
from pprint import pprint

#YAML

with open('my_file.yml') as f:
    my_yaml_list=yaml.load(f)


#JSON
with open('my_file.json') as f:
    my_json_list=json.load(f)

pprint(my_yaml_list)
pprint( my_json_list)
