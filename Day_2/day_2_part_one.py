with open('Day_2\input.txt', encoding='utf-8') as inp:
    moves_raw = inp.read()

moves = [x[0] + x[2] for x in moves_raw.strip().split('\n')]

weights = {'X': 1, 'Y': 2, 'Z': 3}

scores = {'AX': 3,
          'AY': 6,
          'AZ': 0,
          'BX': 0,
          'BY': 3,
          'BZ': 6,
          'CX': 6,
          'CY': 0,
          'CZ': 3
          }

total_score = 0
for move in moves:
    total_score += weights[move[1]] + scores[move]

print(f"The total score is: {total_score}")
