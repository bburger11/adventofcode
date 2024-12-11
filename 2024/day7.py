#!/usr/bin/env python3

import itertools

def read_input():
    f = open("input.txt", "r")
    lines = f.read().splitlines()
    equations = [[int(x) for x in line.replace(":","").split()] for line in lines]
    f.close()
    return equations

def calculate(operands: list, operators: list) -> int:
    result = 0
    print(operands, operators)
    if operators[0] == '||':
        operators.pop(0)
        left = operands.pop(0)
        right = operands.pop(0)
        
        operands.insert(0, int(str(left) + str(right)))
    print(operands, operators)

    for i in range(len(operators) + 1):
        
        if i == 0:
            result += operands[0]
        else:
            if operators[i - 1] == '*':
                result *= operands[i]
            elif operators[i - 1] == '+':
                result += operands[i]
            elif operators[i - 1] == '||':
                pass
    return result

def part1():
    equations = read_input()
    sum_of_possible_equations = 0
    operators = ["*", "+"]
    for equation in equations:
        correct_result = equation[0]
        operands = equation[1:]
        # Use the cartesian product to get all possible sequences of operators
        for sequence in itertools.product(operators, repeat=len(operands)-1):
            sequence = list(sequence)
            result = calculate(operands.copy(), sequence.copy())
            if result == correct_result:
                sum_of_possible_equations += correct_result
                break
    return sum_of_possible_equations

def part2():
    equations = read_input()
    sum_of_possible_equations = 0
    operators = ["*", "+", "||"]
    for equation in equations:
        correct_result = equation[0]
        operands = equation[1:]
        # Use the cartesian product to get all possible sequences of operators
        for sequence in itertools.product(operators, repeat=len(operands)-1):
            sequence = list(sequence)
            result = calculate(operands.copy(), sequence.copy())
            if result == correct_result:
                sum_of_possible_equations += correct_result
                break
        break
    return sum_of_possible_equations

if __name__ == "__main__":
    result1 = part1()
    print(result1)

    result2 = part2()
    print(result2)
