import re
from lib import get_input


def convert_input(data):
    passports = []
    raw_passport = ''
    for line in data:
        raw_passport += line.strip() + ' '
        if len(line) != 0:
            continue
        pairs = [pair.split(':')
                 for pair in raw_passport.strip().split(' ') if ':' in pair]
        passport = {pair[0]: pair[1] for pair in pairs}
        passports.append(passport)
        raw_passport = ''

    return passports


def is_passport_valid(passport):
    fields = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
        # 'cid'
    ]
    return all(field in passport.keys() for field in fields)


def count_of_valid_fields_passports(passports):
    return sum([1 if is_passport_valid(passport) else 0 for passport in passports])


def is_integer_num(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


def count_of_valid_passports(passports):
    count = 0
    for passport in passports:
        if not is_passport_valid(passport):
            continue
        byr = int(passport['byr'].strip())
        iyr = int(passport['iyr'].strip())
        eyr = int(passport['eyr'].strip())
        hgt = passport['hgt'].strip()
        hcl = passport['hcl'].strip()
        ecl = passport['ecl'].strip()
        pid = passport['pid'].strip()

        checks = [
            1920 <= byr and byr <= 2002,
            2010 <= iyr and iyr <= 2020,
            2020 <= eyr and eyr <= 2030,
            'cm' in hgt and 150 <= int(hgt[0:-2]) <= 193 or
            'in' in hgt and 59 <= int(hgt[0:-2]) <= 76,
            True if re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hcl) else False,
            ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
            is_integer_num(pid)
        ]
        if not all(checks):
            print({
                'byr': checks[0],
                'iyr': checks[1],
                'eyr': checks[2],
                'hgt': checks[3],
                'hcl': checks[4],
                'ecl': checks[5],
                'pid': checks[6],
            })
            print(passport)
            print(' ')
        if all(checks):
            count += 1
    return count


def part1():
    data = get_input('./input/input04.txt', '\n')
    passports = convert_input(data)
    print(count_of_valid_fields_passports(passports))


def part2():
    data = get_input('./input/input04.txt', '\n')
    passports = convert_input(data)
    print(count_of_valid_passports(passports))


if __name__ == "__main__":
    part1()
    part2()
