#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("input_one.txt") as f:
    nums = list(map(int, f.readlines()))

for i, num1 in enumerate(nums):
    for j, num2 in enumerate(nums[i + 1 :], start=i + 1):
        for num3 in nums[j + 1 :]:
            if num1 + num2 + num3 == 2020:
                print(num1 * num2 * num3)
