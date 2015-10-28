#!/usr/bin/env

from ciscoconfparse import CiscoConfParse

cfg = CiscoConfParse("config.txt")

crypto_map = cfg.find_objects(r"^crypto map")

for i in crypto_map:
    print i.text
    for j in i.all_children:
        print j.text

