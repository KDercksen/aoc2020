#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("input_one.txt") as f:
    nums = sorted(map(int, f.readlines()))
nums = [0] + nums + [max(nums) + 3]
x = [0, 0]
for num1, num2 in zip(nums, nums[1:]):
    if num2 - num1 == 1:
        x[0] += 1
    elif num2 - num1 == 3:
        x[1] += 1
print(x[0] * x[1])
