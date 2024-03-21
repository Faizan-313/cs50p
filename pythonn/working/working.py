import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    is_correct = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$",s)
    if is_correct:
        g = is_correct.groups()
        if int(g[1]) > 12 or int(g[5]) > 12:
            raise ValueError
        else:
            first_time = new_format(g[1], g[2], g[3])
            second_time = new_format(g[5], g[6], g[7])
            return first_time + ' to ' + second_time
    else:
        raise ValueError

def new_format(hour, min, am_pm):
    if am_pm == 'PM':
        if int(hour) == 12:
            new_hr = 12
        else:
            new_hr = int(hour) + 12
    else:
        if int(hour) == 12:
            new_hr = 0
        else:
            new_hr = int(hour)
    if min == None:
        new_min = ':00'
        new_time = f"{new_hr:02}" + new_min
    else:
        new_time = f"{new_hr:02}" + ":" + min
    return new_time


if __name__ == "__main__":
    main()
