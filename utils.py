"""
Utility Functions for Testing and Analysis
CSC425 Term Project - Milestone 2
Authors: Aryan Kafle, Bijay Dhungana

This module provides utility functions for testing the AI agent
and analyzing its performance.
"""

from game import TicTacToe
from minimax import MinimaxAgent, MinimaxAlphaBetaAgent
import time
from typing import Dict, List


def test_unbeatable_agent(num_games: int = 100, use_alpha_beta: bool = False) -> Dict:
    """
    Test that the AI agent never loses by playing against itself.
    
    Args:
        num_games: Number of games to simulate
        use_alpha_beta: Whether to use Alpha-Beta pruning
        
    Returns:
        Dict: Statistics about the test results
    """
    print(f"\nTesting AI agent for {num_games} games...")
    print("="*50)
    
    agent_type = "Alpha-Beta" if use_alpha_beta else "Standard Minimax"
    print(f"Using: {agent_type}")
    
    results = {'X_wins': 0, 'O_wins': 0, 'draws': 0}
    total_nodes = 0
    total_time = 0
    
    for i in range(num_games):
        game = TicTacToe()
        
        if use_alpha_beta:
            ai_x = MinimaxAlphaBetaAgent(player='X')
            ai_o = MinimaxAlphaBetaAgent(player='O')
        else:
            ai_x = MinimaxAgent(player='X')
            ai_o = MinimaxAgent(player='O')
        
        start_time = time.time()
        
        while not game.is_terminal():
            if game.current_player == 'X':
                move = ai_x.get_best_move(game)
                total_nodes += ai_x.nodes_explored
            else:
                move = ai_o.get_best_move(game)
                total_nodes += ai_o.nodes_explored
            
            game.make_move(move[0], move[1])
        
        end_time = time.time()
        total_time += (end_time - start_time)
        
        winner = game.check_winner()
        if winner == 'X':
            results['X_wins'] += 1
        elif winner == 'O':
            results['O_wins'] += 1
        else:
            results['draws'] += 1
        
        if (i + 1) % 10 == 0:
            print(f"Completed {i + 1} games...")
    
    # Calculate statistics
    results['total_games'] = num_games
    results['avg_nodes_per_game'] = total_nodes / num_games
    results['avg_time_per_game'] = total_time / num_games
    results['total_time'] = total_time
    
    # Print results
    print("\n" + "="*50)
    print("TEST RESULTS")
    print("="*50)
    print(f"Algorithm: {agent_type}")
    print(f"Total Games: {num_games}")
    print(f"X Wins: {results['X_wins']}")
    print(f"O Wins: {results['O_wins']}")
    print(f"Draws: {results['draws']}")
    print(f"Average Nodes Explored: {results['avg_nodes_per_game']:.2f}")
    print(f"Average Time per Game: {results['avg_time_per_game']*1000:.2f}ms")
    print(f"Total Time: {results['total_time']:.2f}s")
    print("="*50)
    
    return results


def compare_algorithms(num_games: int = 50) -> None:
    """
    Compare performance of standard Minimax vs Alpha-Beta pruning.
    
    Args:
        num_games: Number of games to test for each algorithm
    """
    print("\n" + "="*60)
    print("ALGORITHM COMPARISON")
    print("="*60)
    
    print("\n[1/2] Testing Standard Minimax...")
    minimax_results = test_unbeatable_agent(num_games, use_alpha_beta=False)
    
    print("\n[2/2] Testing Minimax with Alpha-Beta Pruning...")
    alpha_beta_results = test_unbeatable_agent(num_games, use_alpha_beta=True)
    
    # Comparison summary
    print("\n" + "="*60)
    print("COMPARISON SUMMARY")
    print("="*60)
    
    print(f"\n{'Metric':<30} {'Minimax':<15} {'Alpha-Beta':<15} {'Improvement'}")
    print("-"*70)
    
    # Nodes explored
    minimax_nodes = minimax_results['avg_nodes_per_game']
    ab_nodes = alpha_beta_results['avg_nodes_per_game']
    node_improvement = ((minimax_nodes - ab_nodes) / minimax_nodes) * 100
    print(f"{'Avg Nodes Explored':<30} {minimax_nodes:<15.2f} {ab_nodes:<15.2f} {node_improvement:.2f}%")
    
    # Time
    minimax_time = minimax_results['avg_time_per_game'] * 1000
    ab_time = alpha_beta_results['avg_time_per_game'] * 1000
    time_improvement = ((minimax_time - ab_time) / minimax_time) * 100
    print(f"{'Avg Time (ms)':<30} {minimax_time:<15.2f} {ab_time:<15.2f} {time_improvement:.2f}%")
    
    print("\n" + "="*60)


def analyze_first_move_advantage() -> None:
    """
    Analyze whether going first provides an advantage in Tic-Tac-Toe.
    """
    print("\n" + "="*50)
    print("FIRST MOVE ADVANTAGE ANALYSIS")
    print("="*50)
    
    game = TicTacToe()
    ai_x = MinimaxAgent(player='X')
    
    # Analyze all possible first moves
    print("\nAnalyzing all possible first moves for X...")
    print("\nPosition values (X's perspective):")
    print("  0   1   2")
    
    values = []
    for i in range(3):
        row_values = []
        for j in range(3):
            game_copy = game.clone()
            game_copy.make_move(i, j)
            
            # Get the minimax value
            value = ai_x.minimax(game_copy, depth=1, is_maximizing=False)
            row_values.append(value)
        values.append(row_values)
    
    for i in range(3):
        print(f"{i} {values[i][0]:3} | {values[i][1]:3} | {values[i][2]:3}")
        if i < 2:
            print(" -----------")
    
    print("\nConclusion:")
    print("- Positive values favor X")
    print("- Zero values lead to draws with optimal play")
    print("- All positions lead to draws when both players play optimally")


def test_single_game_verbose() -> None:
    """
    Play a single game with verbose output for educational purposes.
    """
    print("\n" + "="*50)
    print("VERBOSE GAME TRACE")
    print("="*50)
    
    game = TicTacToe()
    ai_x = MinimaxAlphaBetaAgent(player='X')
    ai_o = MinimaxAlphaBetaAgent(player='O')
    
    move_count = 0
    
    while not game.is_terminal():
        move_count += 1
        print(f"\n--- Move {move_count} ---")
        game.display()
        
        if game.current_player == 'X':
            print("X's turn (AI)...")
            move = ai_x.get_best_move(game)
            game.make_move(move[0], move[1])
            print(f"X played: ({move[0]}, {move[1]})")
            print(f"Nodes explored: {ai_x.nodes_explored}")
        else:
            print("O's turn (AI)...")
            move = ai_o.get_best_move(game)
            game.make_move(move[0], move[1])
            print(f"O played: ({move[0]}, {move[1]})")
            print(f"Nodes explored: {ai_o.nodes_explored}")
    
    print("\n--- Final State ---")
    game.display()
    
    winner = game.check_winner()
    if winner == 'Draw':
        print("Result: Draw")
    else:
        print(f"Result: {winner} wins")


if __name__ == "__main__":
    """Run various tests and analyses."""
    print("\nTIC-TAC-TOE AI TESTING SUITE")
    print("CSC425 Term Project")
    print("Authors: Aryan Kafle, Bijay Dhungana")
    
    while True:
        print("\n" + "="*50)
        print("TEST MENU")
        print("="*50)
        print("1. Test unbeatable agent (Standard Minimax)")
        print("2. Test unbeatable agent (Alpha-Beta Pruning)")
        print("3. Compare algorithms (Minimax vs Alpha-Beta)")
        print("4. Analyze first move advantage")
        print("5. Run verbose single game")
        print("6. Exit")
        
        try:
            choice = input("\nSelect a test (1-6): ").strip()
            
            if choice == '1':
                num = int(input("Number of games to test (default 100): ").strip() or "100")
                test_unbeatable_agent(num_games=num, use_alpha_beta=False)
            elif choice == '2':
                num = int(input("Number of games to test (default 100): ").strip() or "100")
                test_unbeatable_agent(num_games=num, use_alpha_beta=True)
            elif choice == '3':
                num = int(input("Number of games per algorithm (default 50): ").strip() or "50")
                compare_algorithms(num_games=num)
            elif choice == '4':
                analyze_first_move_advantage()
            elif choice == '5':
                test_single_game_verbose()
            elif choice == '6':
                print("\nExiting test suite. Goodbye!")
                break
            else:
                print("Invalid choice! Please select 1-6.")
        except KeyboardInterrupt:
            print("\n\nExiting test suite. Goodbye!")
            break
        except ValueError:
            print("Invalid input! Please enter a number.")

