import os
import re


def valid_password(line):
    raw_range, raw_char, password = line.split(" ")
    char = raw_char[:-1]
    match = re.findall(char, password.strip())
    if match:
        min, max = raw_range.split("-")
        if int(min) <= len(match) <= int(max):
            return True
    return False


filepath = f"{os.getcwd()}/input.txt"
with open(filepath, "r") as fp:
    print(
        len([
            1
            for line in fp.readlines()
            if valid_password(line)
        ])
    )
