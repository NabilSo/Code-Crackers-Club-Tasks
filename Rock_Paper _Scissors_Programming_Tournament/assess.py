import importlib.util
import sys
from collections import defaultdict
import os



def determine_round_winner(move1, move2):
    """Return 0 for tie, 1 if player1 wins, 2 if player2 wins."""
    rules = {'R': 'S', 'S': 'P', 'P': 'R'}
    if move1 == move2:
        return 0
    return 1 if rules[move1] == move2 else 2

def extract_player_name(file_path):
    """Extract player name from filename (e.g., 'Alice_RPS.py' -> 'Alice')"""
    return os.path.basename(file_path).split('_')[0]

def load_student_module(file_path):
    """Load a student's Python file and return their `make_move` function."""
    module_name = file_path.replace(".py", "").replace("/", ".")
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module.make_move

def run_match(player1_path, player2_path, rounds=1000):
    """Run a match between two students' programs."""
    # Get player names
    player1_name = extract_player_name(player1_path)
    player2_name = extract_player_name(player2_path)
    
    # Load both players' functions
    player1_move = load_student_module(player1_path)
    player2_move = load_student_module(player2_path)

    # Track moves and scores
    p1_prev, p2_prev = [], []
    scores = defaultdict(int)

    # Play initial rounds
    for i in range(rounds):
        try:
            p1_move = player1_move(p2_prev.copy())
        except:
            p1_move = 'R'
        try:
            p2_move = player2_move(p1_prev.copy())
        except:
            p2_move = 'R'

        p1_move = p1_move if p1_move in {'R', 'P', 'S'} else 'R'
        p2_move = p2_move if p2_move in {'R', 'P', 'S'} else 'R'

        result = determine_round_winner(p1_move, p2_move)
        if result == 1:
            scores[player1_name] += 1
        elif result == 2:
            scores[player2_name] += 1

        p1_prev.append(p1_move)
        p2_prev.append(p2_move)

    # Check for tie and start interactive sudden-death
    if scores[player1_name] == scores[player2_name]:
        print(f"\n⚔️  TIE after {rounds} rounds! Starting Sudden Death...")
        sudden_death_round = 1
        while scores[player1_name] == scores[player2_name]:
            # Ask organizer to confirm each round
            input(f"\nPress Enter to play Sudden-Death Round {sudden_death_round}...")
            
            try:
                p1_move = player1_move(p2_prev.copy())
            except:
                p1_move = 'R'
            try:
                p2_move = player2_move(p1_prev.copy())
            except:
                p2_move = 'R'

            p1_move = p1_move if p1_move in {'R', 'P', 'S'} else 'R'
            p2_move = p2_move if p2_move in {'R', 'P', 'S'} else 'R'

            result = determine_round_winner(p1_move, p2_move)
            if result == 1:
                scores[player1_name] += 1
            elif result == 2:
                scores[player2_name] += 1

            print(f"  {player1_name}: {p1_move}  |  {player2_name}: {p2_move}")
            print(f"  Result: {player1_name + ' wins!' if result == 1 else player2_name + ' wins!' if result == 2 else 'Tie!'}")
            
            p1_prev.append(p1_move)
            p2_prev.append(p2_move)
            sudden_death_round += 1

    return scores, player1_name, player2_name

# Example usage:
if __name__ == "__main__":
    player1_path = "opponent_RPS.py"
    player2_path = "YourBeautifulName_RPS.py"
    
    scores, p1_name, p2_name = run_match(player1_path, player2_path)
    print(f"\n🏁 FINAL SCORE: {p1_name} ({scores[p1_name]}) vs {p2_name} ({scores[p2_name]})")
    print("🌟 Winner:", p1_name if scores[p1_name] > scores[p2_name] else p2_name)