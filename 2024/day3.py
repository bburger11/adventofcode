#!/usr/bin/env python3

import re
import pprint

def read_input():
    f = open("input.txt", "r")
    lines = f.read().splitlines()
    f.close()
    return lines

# e.g. Accepts '(516,484)' and returns (516,484)
def convert_string_tuple_to_tuple(str_tup):
    return (int(str_tup.replace("(", "").replace(")","").split(",")[0]),int(str_tup.replace("(", "").replace(")","").split(",")[1]))

def part1():
    lines = read_input()
    pairs = []
    # Search for all matches
    for line in lines:
        matches = re.findall(r"mul[(]\d+,\d+[)]", line)
        pairs.extend(matches)
    
    # Remove "mul"
    pairs = [pair.replace("mul","") for pair in pairs]

    # Convert all the string tuples to actual tuples
    pairs = [convert_string_tuple_to_tuple(pair) for pair in pairs]

    # Sum it up
    result = 0
    for pair in pairs:
        result += pair[0] * pair[1]
    return result

def part2():
    lines = read_input()
    tokens = []
    # Search for all matches
    for line in lines:
        matches = re.findall(r"(do[(][)])|(don[']t[(][)])|(mul[(]\d+,\d+[)])", line)
        tokens.extend(matches)
    
    # At the beginning of the program, mul instructions are enabled.
    enabled = True
    result = 0
    for token in tokens:
        if token[0] == 'do()':
            enabled = True
            continue
        elif token[1] == 'don\'t()':
            enabled = False
            continue
        if enabled:
            pair = convert_string_tuple_to_tuple(token[2].replace("mul",""))
            result += pair[0] * pair[1]
    return result

if __name__ == "__main__":
    result1 = part1()
    print(result1)

    result2 = part2()
    print(result2)
