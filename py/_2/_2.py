encoding = {
    'A': 'R',
    'B': 'P',
    'C': 'S',
    'X': 'L',
    'Y': 'D',
    'Z': 'W',
}

def parse(f):
    res = []
    for line in f:
        (opponent_throw_enc, _, outcome_enc) = line.rstrip()
        res.append([encoding[opponent_throw_enc], encoding[outcome_enc]])
    return res

# Maps throw type to points obtained from that throw
throw_points = {
    'R': 1,
    'P': 2,
    'S': 3,
}

# Maps outcome to points obtained from that outcome
outcome_points = {
    'L': 0,
    'D': 3,
    'W': 6,
}

throw_map = {
    'R': {
        'L': 'S',
        'D': 'R',
        'W': 'P'
    },
    'P': {
        'L': 'R',
        'D': 'P',
        'W': 'S'
    },
    'S': {
        'L': 'P',
        'D': 'S',
        'W': 'R'
    }
}

def get_your_throw(opp_throw, outcome):
    return throw_map[opp_throw][outcome]

def get_total_score(throws):
    total_score = 0
    for (opp_throw, outcome) in throws:
        total_score += throw_points[get_your_throw(opp_throw, outcome)]
        total_score += outcome_points[outcome]
    return total_score

def answer(f):
    return get_total_score(parse(f))