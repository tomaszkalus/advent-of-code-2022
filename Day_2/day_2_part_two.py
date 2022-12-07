with open('Day_2\input.txt', encoding='utf-8') as inp:
    moves_raw = inp.read()

# Get the list of two-character strings with the moves, removing the space in between
moves = [x[0] + x[2] for x in moves_raw.strip().split('\n')]

# Dictionary for mapping the points you get from choosing rock (1), paper (2) or scissors (3)
weights = {'X': 0, 'Y': 3, 'Z': 6}

# Dictionary for mapping all the possible outcomes with the points you get from playing that way
scores = {'AX': 3,
          'AY': 1,
          'AZ': 2,
          'BX': 1,
          'BY': 2,
          'BZ': 3,
          'CX': 2,
          'CY': 3,
          'CZ': 1
          }

total_score = 0
for move in moves:
    total_score += weights[move[1]] + scores[move]

print(f"The total score is: {total_score}")
