#!/usr/bin/env python3
"""
Simple Game Launcher - Play Tic-Tac-Toe vs Minimax AI
CSC425 Term Project
"""

from game import TicTacToe
from minimax import MinimaxAlphaBetaAgent

def play_game():
    """Play a simple game of Tic-Tac-Toe against the AI."""
    print("\nTic-Tac-Toe Game")
    print("You: X | AI: O")
    print("Enter moves as: row col (e.g., 1 1 for center)\n")
    
    # Initialize game
    game = TicTacToe()
    ai = MinimaxAlphaBetaAgent(player='O')
    
    # Ask who goes first
    while True:
        first = input("Who goes first? (human/ai): ").strip().lower()
        if first in ['human', 'ai', 'h', 'a']:
            if first in ['ai', 'a']:
                game.current_player = 'O'
            break
        print("Please enter 'human' or 'ai'")
    
    # Game loop
    while not game.is_terminal():
        game.display()
        
        if game.current_player == 'X':
            # Human player's turn
            print("Your turn (X)")
            while True:
                try:
                    move_input = input("Enter move (row col): ").strip()
                    
                    # Handle quit
                    if move_input.lower() in ['quit', 'exit', 'q']:
                        print("\nThanks for playing!")
                        return
                    
                    row, col = map(int, move_input.split())
                    
                    if (row, col) in game.get_valid_moves():
                        game.make_move(row, col)
                        break
                    else:
                        print("Invalid move! Cell occupied or out of bounds.")
                except (ValueError, IndexError):
                    print("Invalid input! Enter as: row col")
                except KeyboardInterrupt:
                    print("\n\nGame interrupted.")
                    return
        else:
            # AI player's turn
            print("AI turn (O)")
            move = ai.get_best_move(game)
            game.make_move(move[0], move[1])
            print(f"AI played: ({move[0]}, {move[1]}) | Analyzed {ai.nodes_explored} possible moves")
        
        print()
    
    # Game over - show final board
    game.display()
    
    winner = game.check_winner()
    if winner == 'Draw':
        print("Game Over: Draw")
    elif winner == 'X':
        print("Game Over: You Win!")
    else:
        print("Game Over: AI Wins")


def main():
    """Main function with replay option."""
    while True:
        play_game()
        
        print()
        replay = input("Play again? (yes/no): ").strip().lower()
        if replay not in ['yes', 'y']:
            print("\nThanks for playing!")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame ended.")

