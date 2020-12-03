#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("input_one.txt") as f:
    lines = list(map(str.strip, f.readlines()))


print(
    sum(
        lines[r][c % len(lines[r])] == "#"
        for r, c in zip(range(len(lines)), range(0, len(lines) * 4, 3))
    )
)
