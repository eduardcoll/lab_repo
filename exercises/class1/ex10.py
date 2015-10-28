#!/usr/bin/env

from ciscoconfparse import CiscoConfParse

cfg = CiscoConfParse("config.txt")

crypto_map = cfg.find_objects_wo_child(parentspec=r"^crypto map",childspec="transform-set AES")

for i in crypto_map:
    print i.text
    for j in i.children:
        print j.text

