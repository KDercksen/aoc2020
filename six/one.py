#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("input_one.txt") as f:
    print(
        sum(len({x for x in group if x.isalpha()}) for group in f.read().split("\n\n"))
    )
