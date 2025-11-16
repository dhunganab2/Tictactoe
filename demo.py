"""
Quick Demo Script
CSC425 Term Project
Authors: Aryan Kafle, Bijay Dhungana

A quick demonstration of the Minimax algorithm in action.
"""

from game import TicTacToe
from minimax import MinimaxAgent, MinimaxAlphaBetaAgent


def demo_perfect_play():
    """Demonstrate that two perfect players always draw."""
    print("="*60)
    print("DEMO: Perfect Play Always Results in Draw")
    print("="*60)
    
    game = TicTacToe()
    ai_x = MinimaxAlphaBetaAgent(player='X')
    ai_o = MinimaxAlphaBetaAgent(player='O')
    
    print("\nTwo AI agents playing optimally...")
    print("X: Minimax with Alpha-Beta Pruning")
    print("O: Minimax with Alpha-Beta Pruning")
    
    move_num = 0
    total_nodes_x = 0
    total_nodes_o = 0
    
    while not game.is_terminal():
        move_num += 1
        print(f"\n--- Move {move_num} ---")
        
        if game.current_player == 'X':
            move = ai_x.get_best_move(game)
            game.make_move(move[0], move[1])
            total_nodes_x += ai_x.nodes_explored
            print(f"X plays ({move[0]}, {move[1]}) - Explored {ai_x.nodes_explored} nodes")
        else:
            move = ai_o.get_best_move(game)
            game.make_move(move[0], move[1])
            total_nodes_o += ai_o.nodes_explored
            print(f"O plays ({move[0]}, {move[1]}) - Explored {ai_o.nodes_explored} nodes")
        
        game.display()
    
    winner = game.check_winner()
    print("="*60)
    print(f"Result: {winner}")
    print(f"Total nodes explored by X: {total_nodes_x}")
    print(f"Total nodes explored by O: {total_nodes_o}")
    print("="*60)
    print("\nConclusion: With perfect play, Tic-Tac-Toe always ends in a draw!")


def demo_algorithm_comparison():
    """Compare standard Minimax vs Alpha-Beta pruning."""
    print("\n\n")
    print("="*60)
    print("DEMO: Algorithm Efficiency Comparison")
    print("="*60)
    
    game = TicTacToe()
    
    print("\nStarting position:")
    game.display()
    
    # Standard Minimax
    print("Testing Standard Minimax...")
    minimax_agent = MinimaxAgent(player='X')
    move1 = minimax_agent.get_best_move(game)
    nodes_minimax = minimax_agent.nodes_explored
    
    # Alpha-Beta Pruning
    print("Testing Alpha-Beta Pruning...")
    alphabeta_agent = MinimaxAlphaBetaAgent(player='X')
    move2 = alphabeta_agent.get_best_move(game)
    nodes_alphabeta = alphabeta_agent.nodes_explored
    
    print("\n" + "="*60)
    print("RESULTS")
    print("="*60)
    print(f"Standard Minimax:")
    print(f"  - Best move: {move1}")
    print(f"  - Nodes explored: {nodes_minimax}")
    print(f"\nAlpha-Beta Pruning:")
    print(f"  - Best move: {move2}")
    print(f"  - Nodes explored: {nodes_alphabeta}")
    print(f"\nEfficiency Gain: {((nodes_minimax - nodes_alphabeta) / nodes_minimax * 100):.2f}%")
    print("="*60)
    print("\nConclusion: Alpha-Beta pruning finds the same optimal move")
    print("while exploring significantly fewer nodes!")


def demo_smart_agent():
    """Show that the agent can win against sub-optimal play."""
    print("\n\n")
    print("="*60)
    print("DEMO: AI Capitalizing on Opponent's Mistakes")
    print("="*60)
    
    game = TicTacToe()
    ai = MinimaxAlphaBetaAgent(player='O')
    
    print("\nSimulating game where human (X) makes suboptimal moves...")
    print("X will make random moves, O (AI) plays optimally")
    
    # Simulated sub-optimal moves by X
    suboptimal_moves = [(0, 0), (1, 0), (2, 0)]  # X plays left column
    
    move_num = 0
    while not game.is_terminal():
        move_num += 1
        print(f"\n--- Move {move_num} ---")
        
        if game.current_player == 'X':
            if suboptimal_moves:
                move = suboptimal_moves.pop(0)
                game.make_move(move[0], move[1])
                print(f"X (Human) plays: {move}")
            else:
                break
        else:
            move = ai.get_best_move(game)
            game.make_move(move[0], move[1])
            print(f"O (AI) plays: {move}")
        
        game.display()
    
    winner = game.check_winner()
    print("="*60)
    if winner == 'O':
        print("Result: AI (O) WINS!")
        print("\nConclusion: The AI can exploit suboptimal play to win!")
    else:
        print(f"Result: {winner}")
    print("="*60)


if __name__ == "__main__":
    print("\n\n")
    print("╔" + "="*58 + "╗")
    print("║" + " "*15 + "TIC-TAC-TOE AI DEMO" + " "*24 + "║")
    print("║" + " "*12 + "CSC425 Term Project - Milestone 2" + " "*13 + "║")
    print("║" + " "*10 + "Authors: Aryan Kafle, Bijay Dhungana" + " "*11 + "║")
    print("╚" + "="*58 + "╝")
    
    print("\nThis demo will showcase:")
    print("1. Perfect play always results in a draw")
    print("2. Alpha-Beta pruning efficiency")
    print("3. AI winning against suboptimal play")
    
    input("\nPress Enter to start the demo...")
    
    # Run demos
    demo_perfect_play()
    input("\nPress Enter to continue to algorithm comparison...")
    
    demo_algorithm_comparison()
    input("\nPress Enter to continue to smart agent demo...")
    
    demo_smart_agent()
    
    print("\n\n")
    print("="*60)
    print("DEMO COMPLETE!")
    print("="*60)
    print("\nTo play against the AI yourself, run: python main.py")
    print("To run comprehensive tests, run: python utils.py")
    print("="*60)

