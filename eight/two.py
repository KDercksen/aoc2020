#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("input_one.txt") as f:
    instructions = [x.strip().split(" ") for x in f.readlines()]
changes = [i for i in range(len(instructions)) if instructions[i][0] in ["jmp", "nop"]]
for c in changes:
    instructions[c][0] = "jmp" if instructions[c][0] == "nop" else "nop"
    visited = set()
    accumulator = 0
    idx = 0
    while idx not in visited:
        if idx >= len(instructions):
            print(accumulator)
            break
        elif instructions[idx][0] == "nop":
            visited.add(idx)
            idx += 1
        elif instructions[idx][0] == "acc":
            accumulator += int(instructions[idx][1])
            visited.add(idx)
            idx += 1
        else:
            visited.add(idx)
            idx += int(instructions[idx][1])
    instructions[c][0] = "jmp" if instructions[c][0] == "nop" else "nop"
