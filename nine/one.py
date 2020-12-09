#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from itertools import combinations

with open("input_one.txt") as f:
    nums = list(map(int, f.readlines()))
for i in range(25, len(nums)):
    if not any(a + b == nums[i] for a, b in combinations(nums[i - 25 : i], 2)):
        print(nums[i])
