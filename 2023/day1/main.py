#!/usr/bin/env python3

import re
import math

match_string = "(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)"
word_to_num = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def read_input():
    f = open('input.txt', 'r')
    lines = f.read().splitlines()
    f.close()
    return lines

if __name__ == '__main__':
    lines = read_input()
    calibration_values = []
    for line in lines:
        # Find the first digit
        first = re.search(match_string, line).group()

        # Find the last digit by building the string up from the end
        for i in range(len(line), -1, -1):
            result = re.search(f"{match_string}", line[i:])
            if result:
                last = result.group()
                break

        # Convert words to digits
        if not first.isdigit():
            first = word_to_num[first]
        if not last.isdigit():
            last = word_to_num[last]
        
        calibration_values.append(int(f"{first}{last}"))

    # Sum em up
    result = str(sum(calibration_values))
    print(result)