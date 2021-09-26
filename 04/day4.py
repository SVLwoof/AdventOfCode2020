file_path: str = r"C:\Users\shaha\Documents\VS_Code\AdventOfCode2020\04\day4_input.txt"

passport_count: int = 0
passport_count_part_two: int = 0

hex_letters: set = {'a', 'b', 'c', 'd', 'e', 'f'}
eye_colors: set = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

with open(file_path, 'r') as inp:
    passports: list = inp.read().split('\n\n')
    for passport in passports:
        parameters: dict = dict(map(str.strip, x.split(':')) for x in passport.split())
        if len(parameters.keys()) == 8 or (len(parameters.keys()) == 7 and 'cid' not in parameters.keys()):
            passport_count += 1
            # Birth year [1920 - 2002]
            if int(parameters['byr']) not in range(1920, 2003):
                continue
            # Issue year [2010 - 2020]
            if int(parameters['iyr']) not in range(2010, 2021):
                continue
            # Expiration year [2020 - 2030]
            if int(parameters['eyr']) not in range(2020, 2031):
                continue
            # Height [150 - 193]cm or [59 - 76]in
            height: int = int(''.join(filter(str.isdigit, parameters['hgt'])))
            if 'cm' in parameters['hgt']:
                if height not in range(150, 194):
                    continue
            elif 'in' in parameters['hgt']:
                if height not in range(59, 77):
                    continue
            else:
                continue
            # Hair color, hex with # and 0-9 or a-f
            if parameters['hcl'][0] != '#' or not all(0 <= int(x) <= 9 if x.isdigit() else x in hex_letters for x in parameters['hcl'][1:]):
                continue
            # Eye color, must be from list above
            if parameters['ecl'] not in eye_colors:
                continue
            # Passport ID, nine-digit num, incl. leading zeroes.
            if len(parameters['pid']) != 9 or not parameters['pid'].isnumeric():
                continue

            passport_count_part_two += 1
        

print(passport_count)
print(passport_count_part_two)