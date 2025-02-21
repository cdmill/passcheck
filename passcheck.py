#!/usr/bin/env python3

import argparse
from enum import StrEnum, auto
import string


class Strength(StrEnum):
    WEAK = auto()
    OK = auto()
    STRONG = auto()


def check(p: str) -> Strength:
    punct = False
    num = False
    size = False

    if len(p) >= 6:
        size = True

    for c in p:
        if c in string.punctuation:
            punct = True
            continue
        if c.isnumeric():
            num = True
            continue

    if punct and num and size:
        return Strength.STRONG
    if (punct + num + size) == 2:
        return Strength.OK
    return Strength.WEAK


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="PassCheck",
        description="A simple automatic passwork strength checker",
        epilog="Password can be one of `weak`, `ok`, `strong`. A strong password is more than 5 characters, contains a number, and contains a special character",
    )
    parser.add_argument("password", type=str, help="password to check")
    args = parser.parse_args()

    if not args.password:
        print(
            "No password provided. Please enter a password to recieve a strength evaluation"
        )

    res = check(args.password)
    print(f"Password strength evaluation: {res}")
