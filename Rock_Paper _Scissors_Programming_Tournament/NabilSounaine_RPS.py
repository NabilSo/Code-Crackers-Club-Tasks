prev_moves = []

moves = ["R", "P", "S"]
counter = {"R": "P", "P": "S", "S": "R"}

def countermost(prev_moves):
    if not prev_moves:
        return moves[2]

    numb = {"R": 0, "P": 0, "S": 0}
    for move in prev_moves:
        numb[move] += 1

    most_common = max(numb, key=numb.get)
    return counter[most_common]

def pattern(prev_moves, pattern_length=3):
    if len(prev_moves) < pattern_length:
        return countermost(prev_moves)

    recent_repeats = prev_moves[-pattern_length:]
    if all(move == recent_repeats[0] for move in recent_repeats):
        return counter[recent_repeats[0]]
    return countermost(prev_moves)


def strat(prev_moves, round_num):
    if round_num < 4:
        return moves[1]  

    numb = {"R": 0, "P": 0, "S": 0}
    for move in prev_moves:
        numb[move] += 1

    total = sum(numb.values())
    most = max(numb.values()) if total > 0 else 0

    det = most / total if total > 0 else 0

    if det > 0.5:
        return countermost(prev_moves)
    return pattern(prev_moves)#,4 pat
    
def make_move(prev_moves):
    round_num = len(prev_moves)
    return strat(prev_moves, round_num)