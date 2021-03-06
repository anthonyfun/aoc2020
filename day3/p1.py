import os


def get_input():
    path = f"{os.getcwd()}/input.txt"
    with open(path, "r") as fp:
        input = [row.strip() for row in fp.readlines()]
    return input


def main():
    input = get_input()
    row_index = 0
    column_index = 0
    vector = {"right": 3, "down": 1}
    input_width = len(input[0])
    trees_hit = 0

    print(f'O{input[0][1:]}')
    while True:
        row_index, column_index = get_next_pos(
            row_index, column_index, vector, input_width
        )
        if row_index == len(input):
            break
        current_pos_is_tree = input[row_index][column_index] == '#'
        row = input[row_index]
        if current_pos_is_tree:
            trees_hit += 1
            print(f'{row[:column_index]}X{row[column_index+1:]}')
        else:
            print(f'{row[:column_index]}O{row[column_index+1:]}')

    print(f'trees hit: {trees_hit}')


def get_next_pos(row_index, column_index, vector, input_width):
    next_row_index = row_index + vector['down']
    next_column_index = (column_index + vector['right']) % input_width

    return next_row_index, next_column_index


main()
