#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("input_one.txt") as f:
    nums = list(map(int, f.readlines()))
for i in range(len(nums)):
    for j in range(i + 2, len(nums)):
        s = sum(nums[i:j])
        if s > 138879426:
            break
        if s == 138879426:
            print(min(nums[i:j]) + max(nums[i:j]))
