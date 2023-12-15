#!/usr/bin/env python3

def read_input():
    f = open('input.txt', 'r')
    lines = f.read().splitlines()
    f.close()
    return lines

def parse_card(card):
    card = card.split(':')
    game_id = card[0].split()[1]
    card = card[1].strip().split('|')
    winning = card[0].strip().split()
    yours = card[1].strip().split()
    return int(game_id), winning, yours

def calculate_winners(winning, yours):
    # Count the number of wins
    num_won = 0
    for num in winning:
        if num in yours:
            num_won += 1
    return num_won

def part1():
    cards = read_input()
    total_points = 0
    for card in cards:
        # Parse the input into two lists
        card_data = parse_card(card)
        winning = card_data[1]
        yours = card_data[2]
        # Count the number of wins
        num_won = calculate_winners(winning, yours)
        # Calculate and track points
        points = 2**(num_won - 1) if num_won != 0 else 0
        total_points += points
    return total_points


def part2():
    cards = read_input()

    # Store the number of cards each card produces in a dict
    card_tracker = {}
    for card in cards:
        card_data = parse_card(card)
        game_id = card_data[0]
        winning = card_data[1]
        yours = card_data[2]
        num_won = calculate_winners(winning, yours)
        card_tracker[game_id] = [num_won, list(range(game_id + 1, game_id + num_won + 1))]
    
    # Start from the back, update the total cards that will be generated subsequently by the rules
    cards.reverse()
    for card in cards:
        card_data = parse_card(card)
        game_id = card_data[0]
        copies = card_tracker[game_id][1]
        for copy in copies:
            card_tracker[game_id][0] += card_tracker[copy][0]
    
    # Sum up all cards, include the original cards in the input
    total_cards = sum([card[0] for card in card_tracker.values()]) + len(cards)
    return total_cards

if __name__ == '__main__':
    result1 = part1()
    print(result1)

    result2 = part2()
    print(result2)