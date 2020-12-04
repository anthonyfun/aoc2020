import os
import re


def valid_password(line):
    raw_pos, raw_char, password = line.split(" ")
    char = raw_char[:-1]
    password = password.strip()
    match = re.findall(char, password)
    if match:
        raw_pos1, raw_pos2 = raw_pos.split("-")
        pos1 = int(raw_pos1)-1
        pos2 = int(raw_pos2)-1
        pos1_is_match = password[pos1] == char
        pos2_is_match = (
            pos2 < len(password) and password[pos2] == char
        )
        if pos1_is_match and not pos2_is_match:
            return True
        if pos2_is_match and not pos1_is_match:
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
