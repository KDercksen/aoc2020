#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("input_one.txt") as f:
    passwords = f.read().split("\n\n")

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
print(sum(all(f in pw for f in fields) for pw in passwords))
