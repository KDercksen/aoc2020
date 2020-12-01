#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("input_one.txt") as f:
    nums = list(map(int, f.readlines()))

for i, num1 in enumerate(nums):
    for num2 in nums[i + 1 :]:
        if num1 + num2 == 2020:
            print(num1 * num2)
