"""
Tic-Tac-Toe Game Interface
CSC425 Term Project - Milestone 2
Authors: Aryan Kafle, Bijay Dhungana

Main interface for playing Tic-Tac-Toe against the AI agent.
"""

from game import TicTacToe
from minimax import MinimaxAgent, MinimaxAlphaBetaAgent
from typing import Optional


def get_player_move(game: TicTacToe) -> tuple[int, int]:
    """
    Get a valid move from the human player.
    
    Args:
        game: Current game state
        
    Returns:
        tuple[int, int]: Valid move as (row, col)
    """
    while True:
        try:
            move_input = input("Enter your move (row col, e.g., '0 1'): ").strip()
            row, col = map(int, move_input.split())
            
            if (row, col) in game.get_valid_moves():
                return row, col
            else:
                print("Invalid move! Cell is already occupied or out of bounds.")
        except (ValueError, IndexError):
            print("Invalid input! Please enter row and column as two numbers (0-2).")
        except KeyboardInterrupt:
            print("\nGame interrupted by user.")
            exit(0)


def play_human_vs_ai(use_alpha_beta: bool = False):
    """
    Play a game of Tic-Tac-Toe: Human vs AI.
    
    Args:
        use_alpha_beta: If True, use Alpha-Beta pruning, else use standard Minimax
    """
    game = TicTacToe()
    
    # Ask who goes first
    print("\n" + "="*50)
    print("Welcome to Tic-Tac-Toe!")
    print("="*50)
    print("\nYou are 'X' and the AI is 'O'")
    
    while True:
        first = input("\nWho should go first? (human/ai): ").strip().lower()
        if first in ['human', 'ai']:
            break
        print("Please enter 'human' or 'ai'")
    
    # Initialize AI agent
    if use_alpha_beta:
        ai_agent = MinimaxAlphaBetaAgent(player='O')
        print("AI using: Minimax with Alpha-Beta Pruning")
    else:
        ai_agent = MinimaxAgent(player='O')
        print("AI using: Standard Minimax")
    
    # Set starting player
    if first == 'ai':
        game.current_player = 'O'
    
    # Game loop
    while not game.is_terminal():
        game.display()
        
        if game.current_player == 'X':
            # Human player
            print("Your turn (X)")
            row, col = get_player_move(game)
            game.make_move(row, col)
        else:
            # AI player
            print("AI's turn (O)...")
            move = ai_agent.get_best_move(game)
            game.make_move(move[0], move[1])
            print(f"AI played: ({move[0]}, {move[1]})")
            print(f"Nodes explored: {ai_agent.nodes_explored}")
    
    # Game over
    game.display()
    winner = game.check_winner()
    
    if winner == 'Draw':
        print("🤝 Game ended in a draw!")
    elif winner == 'X':
        print("🎉 Congratulations! You won!")
    else:
        print("🤖 AI wins! Better luck next time!")


def play_ai_vs_ai(use_alpha_beta_1: bool = False, use_alpha_beta_2: bool = False):
    """
    Play a game of Tic-Tac-Toe: AI vs AI.
    
    Args:
        use_alpha_beta_1: If True, first AI uses Alpha-Beta pruning
        use_alpha_beta_2: If True, second AI uses Alpha-Beta pruning
    """
    game = TicTacToe()
    
    print("\n" + "="*50)
    print("AI vs AI Game")
    print("="*50)
    
    # Initialize AI agents
    if use_alpha_beta_1:
        ai_1 = MinimaxAlphaBetaAgent(player='X')
        print("AI 1 (X): Minimax with Alpha-Beta Pruning")
    else:
        ai_1 = MinimaxAgent(player='X')
        print("AI 1 (X): Standard Minimax")
    
    if use_alpha_beta_2:
        ai_2 = MinimaxAlphaBetaAgent(player='O')
        print("AI 2 (O): Minimax with Alpha-Beta Pruning")
    else:
        ai_2 = MinimaxAgent(player='O')
        print("AI 2 (O): Standard Minimax")
    
    move_count = 0
    
    # Game loop
    while not game.is_terminal():
        move_count += 1
        print(f"\n--- Move {move_count} ---")
        
        if game.current_player == 'X':
            move = ai_1.get_best_move(game)
            game.make_move(move[0], move[1])
            print(f"AI 1 (X) played: ({move[0]}, {move[1]}) - Nodes: {ai_1.nodes_explored}")
        else:
            move = ai_2.get_best_move(game)
            game.make_move(move[0], move[1])
            print(f"AI 2 (O) played: ({move[0]}, {move[1]}) - Nodes: {ai_2.nodes_explored}")
        
        game.display()
    
    # Game over
    winner = game.check_winner()
    print("\n" + "="*50)
    if winner == 'Draw':
        print("Game ended in a draw!")
    else:
        print(f"AI playing '{winner}' wins!")
    print("="*50)


def main_menu():
    """Display main menu and handle game mode selection."""
    while True:
        print("\n" + "="*50)
        print("TIC-TAC-TOE - AI PROJECT")
        print("CSC425 Term Project")
        print("Authors: Aryan Kafle, Bijay Dhungana")
        print("="*50)
        print("\nGame Modes:")
        print("1. Human vs AI (Standard Minimax)")
        print("2. Human vs AI (Minimax with Alpha-Beta Pruning)")
        print("3. AI vs AI (Compare both algorithms)")
        print("4. Exit")
        
        try:
            choice = input("\nSelect a game mode (1-4): ").strip()
            
            if choice == '1':
                play_human_vs_ai(use_alpha_beta=False)
            elif choice == '2':
                play_human_vs_ai(use_alpha_beta=True)
            elif choice == '3':
                play_ai_vs_ai(use_alpha_beta_1=False, use_alpha_beta_2=True)
            elif choice == '4':
                print("\nThank you for playing! Goodbye!")
                break
            else:
                print("Invalid choice! Please select 1-4.")
        except KeyboardInterrupt:
            print("\n\nThank you for playing! Goodbye!")
            break


if __name__ == "__main__":
    main_menu()

