#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def process(line):
    nums = list(range(2 ** len(line)))
    for c in line:
        if c in ["F", "L"]:
            nums = nums[: len(nums) // 2]
        else:
            nums = nums[len(nums) // 2 :]
    return nums[0]


with open("input_one.txt") as f:
    ids = set(process(line[:7]) * 8 + process(line[7:10]) for line in f)

print(list(ids ^ set(range(96, 912)))[0])
