#!/usr/bin/env python3

from timeit import default_timer as timer
from datetime import timedelta

def read_input():
    f = open("input.txt", "r")
    lines = f.read().splitlines()
    f.close()
    return lines

def part1() -> int:
    lines = read_input()

    # Matrix
    matrix = [list(str) for str in lines]
    x_len = len(lines[1])
    y_len = len(lines)
    
    # Find the guard's initial position
    for y in range(y_len):
        for x in range(x_len):
            if matrix[x][y] in 'v^<>':
                current_pos = (x, y)
                current_dir = matrix[x][y]
                next_dir = current_dir
    # Calculate the guard's position until he is no longer patrolling (leaves the map)
    # Record the positions in a set (no duplicates)
    positions = set()
    while True:
        positions.add(current_pos)
        
        # Determine the next position
        if current_dir == 'v':
            next_pos = (current_pos[0] + 1, current_pos[1])
        if current_dir == '^':
            next_pos = (current_pos[0] - 1, current_pos[1])
        if current_dir == '<':
            next_pos = (current_pos[0], current_pos[1] - 1)
        if current_dir == '>':
            next_pos = (current_pos[0], current_pos[1] + 1)

        # Check if the guard has left the map
        if next_pos[0] < 0 or next_pos[1] < 0 or next_pos[0] >= x_len or next_pos[1] >= y_len:
            break
        
        # Check for an obstacle, need to change direction but not position
        if matrix[next_pos[0]][next_pos[1]] == '#':
            next_pos = current_pos
            if current_dir == 'v': next_dir = '<'
            elif current_dir == '<': next_dir = '^'
            elif current_dir == '^': next_dir = '>'
            elif current_dir == '>': next_dir = 'v'

        # Update the current position with the next position
        current_pos = next_pos
        current_dir = next_dir
    
    return len(positions)

def part2() -> int:
    lines = read_input()

    # Matrix
    matrix = [list(str) for str in lines]
    x_len = len(lines[1])
    y_len = len(lines)

    # Find the guard's initial position
    for y in range(y_len):
        for x in range(x_len):
            if matrix[x][y] in 'v^<>':
                initial_pos = (x, y)
                initial_dir = matrix[x][y]
                next_dir = initial_dir

    # Look at each position in the matrix, checking what happens when we change empty spaces to an obstacle
    positions_leading_to_cyle = 0
    for y in range(y_len):
        for x in range(x_len):
            # Find each dot and change it to an obstacle. See if this change results in an infinite loop
            if matrix[x][y] != '.':
                continue
            else:
                # Reset the tracked location and direction of the guard
                current_pos = initial_pos
                current_dir = initial_dir
                next_dir = initial_dir

                # Change the point to an obstacle, track all positions that the guard goes in this new scenario
                matrix[x][y] = '#'
                positions = []
                while True:
                    # The condition that determines whether a loop has happened:
                    #   The guard is in the same position and direction twice
                    if current_pos + (current_dir,) in positions:
                        positions_leading_to_cyle += 1
                        break
                    else:
                        positions.append(current_pos + (current_dir,))

                    # Determine the next position
                    if current_dir == 'v':
                        next_pos = (current_pos[0] + 1, current_pos[1])
                    if current_dir == '^':
                        next_pos = (current_pos[0] - 1, current_pos[1])
                    if current_dir == '<':
                        next_pos = (current_pos[0], current_pos[1] - 1)
                    if current_dir == '>':
                        next_pos = (current_pos[0], current_pos[1] + 1)

                    # Check if the guard has left the map, this does not lead to a cycle and we continue
                    if next_pos[0] < 0 or next_pos[1] < 0 or next_pos[0] >= x_len or next_pos[1] >= y_len:
                        break

                    # Check for an obstacle, need to change direction but not position
                    if matrix[next_pos[0]][next_pos[1]] == '#':
                        next_pos = current_pos
                        if current_dir == 'v': next_dir = '<'
                        elif current_dir == '<': next_dir = '^'
                        elif current_dir == '^': next_dir = '>'
                        elif current_dir == '>': next_dir = 'v'

                    # Update the current position with the next position
                    current_pos = next_pos
                    current_dir = next_dir
            # When done checking this position as an obstacle, return the matrix to its original state
            matrix[x][y] = '.'
    
    return positions_leading_to_cyle

if __name__ == "__main__":
    # Part 1
    start = timer()
    result1 = part1()
    print(result1)
    end = timer()
    print(timedelta(seconds=end-start))
    
    # Part 2
    start = timer()
    result2 = part2()
    print(result2)
    end = timer()
    print(timedelta(seconds=end-start))
