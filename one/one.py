#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import combinations

with open("input_one.txt") as f:
    nums = list(map(int, f.readlines()))

print([x * y for x, y in combinations(nums, 2) if x + y == 2020][0])
