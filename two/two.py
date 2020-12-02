#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

with open("input_one.txt") as f:
    valid = 0
    for line in f:
        lower, upper, letter, passwd = re.match(  # type: ignore
            r"(\d+)-(\d+) (\w): (\w+)", line
        ).groups()
        valid += (passwd[int(lower) - 1] == letter) ^ (passwd[int(upper) - 1] == letter)

print(valid)
