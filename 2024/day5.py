#!/usr/bin/env python3
import pprint
import time

def read_input():
    f = open("input.txt", "r")
    lines = f.read().splitlines()
    rules = []
    pages = []
    for line in lines:
        if '|' in line:
            rules.append((int(line.split('|')[0]),int(line.split('|')[1])))
        elif ',' in line:
            pages.append([int(x) for x in line.split(',')])
    f.close()
    return rules, pages

def part1():
    # Create a rulebook to track all rules
    rules, pages = read_input()
    rulebook = {}
    for rule in rules:
        if rule[1] in rulebook:
            rulebook[rule[1]].append(rule[0])
        else:
            rulebook[rule[1]] = [rule[0]]

    # Iterate through pages and compare it to rules
    total = 0
    for page in pages:
        valid = True
        for i, num in enumerate(page):
            # Do any of the page numbers in rulebook[num] exist in the remainder of page[i+1:] ?
            if num in rulebook:
                if [x for x in rulebook[num] if x in page[i+1:]]:
                    valid = False
                    break
        # If we reach the final element and it is still valid, add the middle element
        if valid:
            total += page[len(page) // 2]

    return total


def part2():
    # Create a rulebook to track all rules
    rules, pages = read_input()
    rulebook = {}
    for rule in rules:
        if rule[1] in rulebook:
            rulebook[rule[1]].append(rule[0])
        else:
            rulebook[rule[1]] = [rule[0]]

    # Iterate through pages and compare it to rules
    total = 0
    for page in pages:
        # Check the initial page ordering and record the rules that are violated
        violated_rules = []
        for i, num in enumerate(page):
            # Do any of the page numbers in rulebook[num] exist in the remainder of page[i+1:] ?
            if num in rulebook:
                matches = [x for x in rulebook[num] if x in page[i+1:]]
                if matches:
                    violated_rules.append({
                        num: matches
                    })
        # Loop until a valid page is found (end the loop when violated rules is empty)
        while violated_rules:
            # Start with the first violated rule, and swap the elements in the list
            violated_rule = violated_rules.pop(0)
            (key, values), = violated_rule.items()            
            a, b = page.index(key), page.index(values[0])
            page[b], page[a] = page[a], page[b]
            # Assume the list is now correct, reset violated_rules
            violated_rules = []
            # Begin the check again
            for i, num in enumerate(page):
                if num in rulebook:
                    matches = [x for x in rulebook[num] if x in page[i+1:]]
                    if matches:
                        violated_rules.append({
                            num: matches
                        })
            # Found the valid configuration
            if not violated_rules:
                total += page[len(page) // 2]

    return total

if __name__ == "__main__":
    result1 = part1()
    print(result1)

    result2 = part2()
    print(result2)
