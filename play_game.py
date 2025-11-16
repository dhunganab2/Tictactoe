"""
Simulated Game Demo - Watch AI Play
For interactive play, run this script directly in your terminal
"""

from game import TicTacToe
from minimax import MinimaxAlphaBetaAgent
import time

def simulate_human_vs_ai():
    """Simulate a game where human makes specific moves."""
    print("\nSimulated Game Demo")
    print("You: X | AI: O\n")
    
    game = TicTacToe()
    ai = MinimaxAlphaBetaAgent(player='O')
    
    # Predefined human moves (simulating a player trying to win)
    human_moves = [
        (1, 1),  # Center
        (0, 0),  # Top-left
        (2, 2),  # Bottom-right
        (0, 2),  # Top-right
        (2, 0),  # Bottom-left
    ]
    
    while not game.is_terminal() and human_moves:
        game.display()
        
        if game.current_player == 'X':
            # Human's turn (simulated)
            move = human_moves.pop(0)
            if move in game.get_valid_moves():
                game.make_move(move[0], move[1])
                print(f"Your turn (X): {move}")
            else:
                # If move is taken, get any valid move
                move = game.get_valid_moves()[0]
                game.make_move(move[0], move[1])
                print(f"Your turn (X): {move}")
        else:
            # AI's turn
            print("AI turn (O)")
            move = ai.get_best_move(game)
            game.make_move(move[0], move[1])
            print(f"AI played: {move} | Analyzed {ai.nodes_explored} possible moves")
        
        print()
        time.sleep(0.3)  # Pause for readability
    
    # Game over
    game.display()
    winner = game.check_winner()
    if winner == 'Draw':
        print("Game Over: Draw")
    elif winner == 'X':
        print("Game Over: You Win!")
    else:
        print("Game Over: AI Wins")
    
    return winner


if __name__ == "__main__":
    # Run simulation
    result = simulate_human_vs_ai()
    
    print("\nTo play interactively: python3 start_game.py")

