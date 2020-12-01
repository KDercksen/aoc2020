#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import combinations

with open("input_one.txt") as f:
    nums = list(map(int, f.readlines()))

print([x * y * z for x, y, z in combinations(nums, 3) if x + y + z == 2020][0])
