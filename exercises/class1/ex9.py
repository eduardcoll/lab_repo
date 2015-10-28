#!/usr/bin/env

from ciscoconfparse import CiscoConfParse

cfg = CiscoConfParse("config.txt")

crypto_map = cfg.find_objects_w_child(parentspec=r"^crypto map",childspec="pfs group2")

for i in crypto_map:
    print i.text
    for j in i.all_children:
        print j.text

