#!/usr/bin/env python3

import re
import pprint

def read_input():
    f = open('input.txt', 'r')
    lines = f.read().splitlines()
    f.close()
    return lines



def part1():
    # BIG assumption that two symbols cannot be next to one number
    # But it still works..
    scheme_lines = read_input()
    prev_nums = []
    prev_syms = []
    parts_sum = 0
    for i, scheme_line in enumerate(scheme_lines):
        nums = [(m.group(), m.start(0), m.end(0)) for m in re.finditer(r'(\d+)', scheme_line)]
        syms = [m.start(0) for m in re.finditer(r'[^\d\.]', scheme_line)]

        # Check symbols against previous numbers
        for sym in syms:
            for num in prev_nums:
                if num[1] - 1 <= sym <= num[2]:
                    parts_sum += int(num[0])
        
        # Check numbers against previous symbols
        for num in nums:
            for sym in prev_syms:
                if num[1] - 1 <= sym <= num[2]:
                    parts_sum += int(num[0])
        
        # Check numbers against symbols in the same line
        for num in nums:
            for sym in syms:
                # Check for symbol before
                if num[1] == sym + 1:
                    parts_sum += int(num[0])
                # Check for symbol after
                if num[2] == sym:
                    parts_sum += int(num[0])

        prev_nums = nums
        prev_syms = syms

    return parts_sum

def part2():
    scheme_lines = read_input()
    prev_nums = []
    prev_syms = []
    sym_states = {}
    for i, scheme_line in enumerate(scheme_lines):
        nums = [(m.group(), m.start(0), m.end(0)) for m in re.finditer(r'(\d+)', scheme_line)]
        syms = [(m.start(0), i) for m in re.finditer(r'[\*]', scheme_line)]
        for sym in syms:
            sym_states[sym] = []

        # Check symbols against previous numbers
        for sym in syms:
            for num in prev_nums:
                if num[1] - 1 <= sym[0] <= num[2]:
                    sym_states[sym].append(int(num[0]))
        
        # Check numbers against previous symbols
        for num in nums:
            for sym in prev_syms:
                if num[1] - 1 <= sym[0] <= num[2]:
                    sym_states[sym].append(int(num[0]))
        
        # Check numbers against symbols in the same line
        for num in nums:
            for sym in syms:
                # Check for symbol before
                if num[1] == sym[0] + 1:
                    sym_states[sym].append(int(num[0]))
                # Check for symbol after
                if num[2] == sym[0]:
                    sym_states[sym].append(int(num[0]))

        prev_nums = nums
        prev_syms = syms

    # Get the sum of gear_ratios
    ratio_sum = 0
    for product in list(sym_states.values()):
        if len(product) == 1:
            continue
        ratio = product[0] * product[1]
        ratio_sum += ratio


    return ratio_sum

if __name__ == '__main__':
    result1 = part1()
    print(result1)

    result2 = part2()
    print(result2)