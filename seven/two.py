#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

rule_pattern = r"(\w+\s\w+) bags contain (\d.*)\n"
content_pattern = r"(\d\s\w+\s\w+)"
rules = {}

with open("input_one.txt") as f:
    for rule in f:
        m = re.match(rule_pattern, rule)
        if m:
            rules[m.group(1)] = {
                x[2:]: int(x[0]) for x in re.findall(content_pattern, m.group(2))
            }


q = ["shiny gold"]
bags = []
total = 0
while len(q) > 0:
    color = q.pop(0)
    bags.append(color)
    if color in rules.keys():
        for bag, count in rules[color].items():
            q.extend([bag] * count)
print(len(bags) - 1)
