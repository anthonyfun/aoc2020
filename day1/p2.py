import os
cwd = os.getcwd()
filepath = f"{cwd}/input.txt"

with open(filepath, 'r') as fp:
    entries = [int(entry) for entry in fp.readlines()]


def entry_popper(index, entries):
    other_entries = list(entries)
    entry = other_entries.pop(index)
    return entry, other_entries


for i, _ in enumerate(entries):
    first_entry, second_entries = entry_popper(i, entries)
    for j, _ in enumerate(second_entries):
        second_entry, third_entries = entry_popper(j, second_entries)
        for third_entry in third_entries:
            if (first_entry + second_entry + third_entry) == 2020:
                print(first_entry * second_entry * third_entry)
                exit()
