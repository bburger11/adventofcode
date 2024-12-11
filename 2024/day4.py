#!/usr/bin/env python3

def read_input():
    f = open("input.txt", "r")
    lines = f.read().splitlines()
    f.close()
    return lines

def part1():
    lines = read_input()

    # Matrix
    matrix = [list(str) for str in lines]
    x_len = len(lines[1])
    y_len = len(lines)

    count = 0
    for y in range(y_len):
        for x in range(x_len):
            # Find out which directions are even possible
            left  = (x >= 3)
            up    = (y >= 3)
            right = (x_len - x >= 4)
            down  = (y_len - y >= 4)
            
            # Found an X! Check all directions
            if matrix[y][x] == 'X':
                if right:
                    if matrix[y][x+1] == 'M' and matrix[y][x+2] == 'A' and matrix[y][x+3] == 'S':
                        count += 1
                if left:
                    if matrix[y][x-1] == 'M' and matrix[y][x-2] == 'A' and matrix[y][x-3] == 'S':
                        count += 1
                if up:
                    if matrix[y-1][x] == 'M' and matrix[y-2][x] == 'A' and matrix[y-3][x] == 'S':
                        count += 1
                if down:
                    if matrix[y+1][x] == 'M' and matrix[y+2][x] == 'A' and matrix[y+3][x] == 'S':
                        count += 1
                if right and up:
                    if matrix[y-1][x+1] == 'M' and matrix[y-2][x+2] == 'A' and matrix[y-3][x+3] == 'S':
                        count += 1
                if right and down:
                    if matrix[y+1][x+1] == 'M' and matrix[y+2][x+2] == 'A' and matrix[y+3][x+3] == 'S':
                        count += 1
                if left and up:
                    if matrix[y-1][x-1] == 'M' and matrix[y-2][x-2] == 'A' and matrix[y-3][x-3] == 'S':
                        count += 1
                if left and down:
                    if matrix[y+1][x-1] == 'M' and matrix[y+2][x-2] == 'A' and matrix[y+3][x-3] == 'S':
                        count += 1
    return count

def part2():
    lines = read_input()

    # Matrix
    matrix = [list(str) for str in lines]
    x_len = len(lines[1])
    y_len = len(lines)

    count = 0
    for y in range(y_len):
        for x in range(x_len):
            # All directions need to be possible
            left  = (x >= 1)
            up    = (y >= 1)
            right = (x_len - x >= 2)
            down  = (y_len - y >= 2)
            if not all([right, left, up, down]):
                continue
            
            # Found an A, need to check both diagonals
            if matrix[y][x] == 'A':
                nw_to_se = (matrix[y-1][x-1] in 'MS' and matrix[y+1][x+1] in 'MS' and matrix[y-1][x-1] != matrix[y+1][x+1])
                sw_to_ne = (matrix[y+1][x-1] in 'MS' and matrix[y-1][x+1] in 'MS' and matrix[y+1][x-1] != matrix[y-1][x+1])
                if nw_to_se and sw_to_ne:
                    count += 1
    return count

if __name__ == "__main__":
    result1 = part1()
    print(result1)

    result2 = part2()
    print(result2)
