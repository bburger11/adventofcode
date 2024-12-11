#!/usr/bin/env python3

def read_input():
    f = open('input.txt', 'r')
    lines = f.read().splitlines()
    f.close()
    return lines

# Builds a dictionary to represent the cubes in a drawing
# Follows the form
# cubes = {
#   'red': 1,
#   'green': 2,
#   'blue': 3
# }
def parse_cubes(line):
    cubes = {}
    for cube in line:
        cube = cube.strip().split(' ')
        color = cube[1]
        val = int(cube[0])
        cubes[color] = val
    return cubes

def part1():
    games = read_input()
    # Only 12 red cubes, 13 green cubes, and 14 blue cubes available
    available_cubes = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    result = 0
    for game in games:
        # Assume a game is possible until it's not
        possible = True
        # Separate the Game ID and Drawings
        game_id = game.split(":")[0].split(' ')[1]
        drawings = [drawing.strip() for drawing in game.split(":")[1].strip().split(";")]
        for drawing in drawings:
            # Parse the drawing into a dictionary of cubes
            cubes = parse_cubes(drawing.split(','))
            # Check if any cube values are in both and the drawing's cube amounts are greater than is possible
            invalid_colors = {k: cubes[k] for k in cubes if k in available_cubes and cubes[k] > available_cubes[k]}
            if invalid_colors:
                possible = False
                break
        if possible:
            result += int(game_id)

    return result

def part2():
    games = read_input()
    result = 0
    for game in games:
        drawings = [drawing.strip() for drawing in game.split(":")[1].strip().split(";")]
        required_cubes = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        for drawing in drawings:
            # Parse the drawing into a dictionary of cubes
            cubes = parse_cubes(drawing.split(','))
            min_cubes = {k: cubes[k] for k in cubes if k in required_cubes and cubes[k] > required_cubes[k]}
            
            # Update required cubes
            for k in min_cubes:
                required_cubes[k] = min_cubes[k]
        
        # Remove colors that were not needed (don't know if this is necessary)
        required_cubes = {k:v for k,v in required_cubes.items() if v != 0}

        # Caulculate power
        power = 1
        for x in list(required_cubes.values()):
            power = power * x
        result += power

    return result

if __name__ == '__main__':
    result1 = part1()
    print(result1)

    result2 = part2()
    print(result2)