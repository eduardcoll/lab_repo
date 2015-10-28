#!/usr/bin/env python

import yaml
import json

my_list = [range(3),{'elem1':'one','elem2':'two'}]

#YAML

with open("my_file.yml","w") as f:
    f.write(yaml.dump(my_list,default_flow_style=False))


#JSON

with open("my_file.json","w") as f:
    json.dump(my_list,f)


