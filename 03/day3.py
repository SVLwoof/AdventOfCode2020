file_path: str = r"C:\Users\shaha\Documents\VS_Code\AdventOfCode2020\03\day3_input.txt"

tree_char: str = '#'

tree_count_1: int = 0
tree_count_3: int = 0
tree_count_5: int = 0
tree_count_7: int = 0
tree_count_2: int = 0

with open(file_path, 'r') as inp:
    lines: list = [line.strip() for line in inp.readlines()]

    row: int = 0
    col_1 = col_3 = col_5 = col_7 = col_2 = 0
    while row + 1 < len(lines):
        if col_1 >= len(lines[row]):
            col_1 -= len(lines[row])
        if col_3 >= len(lines[row]):
            col_3 -= len(lines[row])
        if col_5 >= len(lines[row]):
            col_5 -= len(lines[row])
        if col_7 >= len(lines[row]):
            col_7 -= len(lines[row])
        if lines[row][col_1] == tree_char:
            tree_count_1 += 1
        if lines[row][col_3] == tree_char:
            tree_count_3 += 1
        if lines[row][col_5] == tree_char:
            tree_count_5 += 1
        if lines[row][col_7] == tree_char:
            tree_count_7 += 1

        if row % 2 == 0:
            if col_2 >= len(lines[row]):
                col_2 -= len(lines[row])
            if lines[row][col_2] == tree_char:
                tree_count_2 += 1
            col_2 += 1
        col_1 += 1
        col_3 += 3
        col_5 += 5
        col_7 += 7

        row += 1


print(tree_count_3)
print()
print(tree_count_1 * tree_count_3 * tree_count_5 * tree_count_7 * tree_count_2)