file_path: str = r"C:\Users\shaha\Documents\VS_Code\AdventOfCode2020\05\day5_input.txt"


def get_seat_location(st: str) -> tuple:
    row_bin_str: str = st[:7].replace('B', '1').replace('F', '0')
    col_bin_str: str = st[7:].replace('R', '1').replace('L', '0')
    row_num: int = int(row_bin_str, base=2)
    col_num: int = int(col_bin_str, base=2)
    return row_num, col_num

def get_seat_id(row: int, col: int) -> int:
    return row * 8 + col




with open(file_path, 'r') as inp:
    seats: list = [x.strip() for x in inp.readlines()]
    max_seat: str = max(seats, key=lambda x: get_seat_id(*get_seat_location(x)), default=0)
    max_seat_id: int = get_seat_id(*get_seat_location(max_seat))
    print(max_seat_id)