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


q = [r for r in rules.keys() if "shiny gold" in rules[r]]
visited = set()
while len(q) > 0:
    color = q.pop(0)
    if color not in visited:
        q.extend([r for r in rules.keys() if color in rules[r]])
    visited.add(color)

print(len(visited))
