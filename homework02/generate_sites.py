#!/usr/bin/env python3
import json
import random


with open('meteorites.json', 'w') as out:

    compositionsList = ['stony', 'iron', 'stony-iron']
    sites = []
    for i in range(5):
        site = {}
        site['site_id'] = i
        site['latitude'] = (random.random()*2)+16
        site['longitude'] = (random.random()*2) + 82
        site['composition'] = random.choice(compositionsList)
        sites.append(site)
    dict = {'sites' : sites }
    json.dump(dict, out, indent=2)
        
