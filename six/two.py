#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("input_one.txt") as f:
    print(
        sum(
            len(set.intersection(*[{x for x in x.strip()} for x in g.split()]))
            for g in f.read().split("\n\n")
        )
    )
