#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("input_one.txt") as f:
    passwords = f.read().split("\n\n")
    pwdict = [dict([p.split(":") for p in pw.split()]) for pw in passwords]  # type: ignore

validate = {
    "byr": lambda x: len(x) == 4 and x.isdigit() and (1920 <= int(x) <= 2002),
    "iyr": lambda x: len(x) == 4 and x.isdigit() and (2010 <= int(x) <= 2020),
    "eyr": lambda x: len(x) == 4 and x.isdigit() and (2020 <= int(x) <= 2030),
    "hgt": lambda x: x[-2:] in ["cm", "in"]
    and x[:-2].isdigit()
    and (150 <= int(x[:-2]) <= 193 if x[-2:] == "cm" else 59 <= int(x[:-2]) <= 76),
    "hcl": lambda x: x[0] == "#"
    and len(x) == 7
    and all(
        a in ["a", "b", "c", "d", "e", "f"] + list(map(str, range(10))) for a in x[1:]
    ),
    "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda x: len(x) == 9 and x.isdigit(),
}

print(
    sum(
        len((pw.keys() - {"cid"}) ^ validate.keys()) == 0
        and all(validate[key](val) for key, val in pw.items() if key != "cid")
        for pw in pwdict
    )
)
