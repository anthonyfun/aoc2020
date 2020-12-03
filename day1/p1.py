import os
cwd = os.getcwd()
filepath = f"{cwd}/input.txt"

with open(filepath, 'r') as fp:
    entries = [int(entry) for entry in fp.readlines()]

    for index, entry in enumerate(entries):
        other_entries = entries[:index] + entries[-index:]
        for other_entry in other_entries:
            if (entry + other_entry) == 2020:
                print(entry*other_entry)
                exit()
