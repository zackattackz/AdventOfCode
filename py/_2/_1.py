encoding = {
    'A': 'R',
    'B': 'P',
    'C': 'S',
    'X': 'R',
    'Y': 'P',
    'Z': 'S',
}

def parse(f):
    res = []
    for line in f:
        [opponent_throw_enc, _, your_throw_enc] = line.rstrip()
        res.append((encoding[opponent_throw_enc], encoding[your_throw_enc]))
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

outcome_map = {
    'R': {
        'R': 'D',
        'P': 'W',
        'S': 'L'
    },
    'P': {
        'R': 'L',
        'P': 'D',
        'S': 'W'
    },
    'S': {
        'R': 'W',
        'P': 'L',
        'S': 'D'
    }
}

def round_outcome(opp_throw, your_throw):
    return outcome_map[opp_throw][your_throw]

def get_total_score(throws):
    total_score = 0
    for (opp_throw, your_throw) in throws:
        total_score += throw_points[your_throw]
        total_score += outcome_points[round_outcome(opp_throw, your_throw)]
    return total_score

def answer(f):
    return get_total_score(parse(f))