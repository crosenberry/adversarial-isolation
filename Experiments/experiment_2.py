# Heuristic vs Heuristic
from AI.decision_maker import DecisionMaker
from Game_Logic.board import IsolationGame

def run_experiment(num_games=100):
    # Track wins
    h1_wins = 0
    h2_wins = 0
    draws = 0

    for _ in range(num_games):
        game = IsolationGame()
        decision_maker = DecisionMaker(game)

        while not game.is_over():
            if game.current_player() == "H1":
                best_move = decision_maker.choose_move(game.get_board_state(), max_depth=3, heuristic_type="heuristic_1")
                game.make_move(best_move)
            else:  # H2's turn
                best_move = decision_maker.choose_move(game.get_board_state(), max_depth=3, heuristic_type="heuristic_2")
                game.make_move(best_move)

        winner = game.get_winner()
        if winner == "H1":
            h1_wins += 1
        elif winner == "H2":
            h2_wins += 1
        else:  # Draw
            draws += 1

    print(f"After {num_games} games:")
    print(f"H1 wins: {h1_wins}")
    print(f"H2 wins: {h2_wins}")
    print(f"Draws: {draws}")

if __name__ == "__main__":
    run_experiment()
