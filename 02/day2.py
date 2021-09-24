file_path: str = r"C:\Users\shaha\Documents\VS_Code\AdventOfCode2020\02\day2_input.txt"

count_part_one: int = 0
count_part_two: int = 0


with open(file_path, 'r') as inp:
    lines: list = inp.readlines()
    for line in lines:
        num_range, ch, password = line.split()
        low, high = [int(x) for x in num_range.split('-')]
        ch = ch[0]
        if low <= password.count(ch) <= high:
            count_part_one += 1
        if bool(password[low - 1] == ch) ^ bool(password[high - 1] == ch): # XOR
            count_part_two += 1

print(count_part_one)
print(count_part_two)