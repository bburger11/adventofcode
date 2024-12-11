#!/usr/bin/env python3

def read_input():
    f = open("input.txt", "r")
    lines = f.read().splitlines()
    f.close()
    return lines

def part1():
    lines = read_input()

    # Store the number of IDs (they are equal in each list)
    num_ids = len(lines)

    # Parse the input into two lists
    left = []
    right = []
    for line in lines:
        a, b = line.split()
        left.append(int(a))
        right.append(int(b))

    # Sort the input and combine
    left.sort()
    right.sort()
    full = left + right

    # Calculate the sum of differences
    res = 0
    for i in range(num_ids):
        res += abs(full[i] - full[i + num_ids])
    
    return res

def part2():
    lines = read_input()
    
    # Parse the input into two lists
    left = []
    right = []
    for line in lines:
        a, b = line.split()
        left.append(int(a))
        right.append(int(b))
    
    # Calculate the count of each, perform the multiplication, and add it to result
    memo = {}
    res = 0
    for num in left:
        if num not in memo:
            count = right.count(num)
            memo[num] = count
        res += num * memo[num]
    return res

if __name__ == "__main__":
    result1 = part1()
    print(result1)

    result2 = part2()
    print(result2)
