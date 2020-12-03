#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

with open("input_one.txt") as f:
    lines = list(map(str.strip, f.readlines()))


print(
    math.prod(
        sum(
            lines[r][c % len(lines[r])] == "#"
            for r, c in zip(
                range(row_start, row_end, row_step), range(col_start, col_end, col_step)
            )
        )
        for ((row_start, row_end, row_step), (col_start, col_end, col_step)) in [
            ((0, len(lines), 1), (0, len(lines), 1)),
            ((0, len(lines), 1), (0, len(lines) * 3, 3)),
            ((0, len(lines), 1), (0, len(lines) * 5, 5)),
            ((0, len(lines), 1), (0, len(lines) * 7, 7)),
            ((0, len(lines), 2), (0, len(lines), 1)),
        ]
    )
)
