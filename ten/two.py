#!/usr/bin/env python3
# -*- coding: utf-8 -*-


with open("input_one.txt") as f:
    nums = sorted(map(int, f.readlines()))
nums = [0] + nums + [max(nums) + 3]
cache = [0] * len(nums)
cache[0] = 1
for idx in range(1, len(nums)):
    if idx - 1 >= 0 and nums[idx] - nums[idx - 1] <= 3:
        cache[idx] += cache[idx - 1]
    if idx - 2 >= 0 and nums[idx] - nums[idx - 2] <= 3:
        cache[idx] += cache[idx - 2]
    if idx - 3 >= 0 and nums[idx] - nums[idx - 3] <= 3:
        cache[idx] += cache[idx - 3]
print(cache[-1])
