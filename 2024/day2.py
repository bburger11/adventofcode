#!/usr/bin/env python3

def read_input():
    f = open("input.txt", "r")
    lines = f.read().splitlines()
    f.close()
    return lines

def check_if_safe(report):
    # Check for duplicates
    if len(report) != len(set(report)):
        return False
    # Check if report strictly inc/dec
    strictly_increasing_or_decreasing = True
    inc = False
    dec = False
    for i, level in enumerate(report):
        # Compare the first two to determine if increasing or decreasing
        if i == 0:
            if level < report[i + 1]:
                inc = True
            elif level > report[i + 1]:
                dec = True
        # Search is complete if we reach the last element
        if i == len(report) - 1:
            break
        if inc and level > report[i + 1]:
            strictly_increasing_or_decreasing = False
            break
        if dec and level < report[i + 1]:
            strictly_increasing_or_decreasing = False
            break
    if not strictly_increasing_or_decreasing:
        return False
    # Check for gaps of more than 3
    differ_by_at_most_three = True
    sorted_report = sorted(report)
    for i, level in enumerate(sorted_report):
        # Search is complete if we reach the last element
        if i == len(sorted_report) - 1:
            break
        if sorted_report[i + 1] - level > 3:
            differ_by_at_most_three = False
            break
    if not differ_by_at_most_three:
        return False
    return True

def part1():
    lines = read_input()
    reports = [[int(level) for level in report.split()] for report in lines]
    
    # Count safe reports
    count = 0
    for report in reports:
        if check_if_safe(report): count += 1

    return count

def part2():
    lines = read_input()
    reports = [[int(level) for level in report.split()] for report in lines]
    
    # Count safe reports
    count = 0
    for report in reports:
        # Create a copy of the original report
        original = report.copy()
        # Check if the report is unsafe
        if not check_if_safe(report):
            found = False
            # Try removing each element and checking again
            for i in range(len(report)):
                report.pop(i)
                if check_if_safe(report):
                    found = True
                    break
                # Return the list to its original state
                report = original.copy()
            if found:
                count += 1
        else:
            count += 1
    return count

if __name__ == "__main__":
    result1 = part1()
    print(result1)

    result2 = part2()
    print(result2)
