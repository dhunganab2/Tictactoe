"""
Minimax Algorithm Implementation
CSC425 Term Project - Milestone 2
Authors: Aryan Kafle, Bijay Dhungana

This module implements the Minimax adversarial search algorithm
for optimal decision-making in Tic-Tac-Toe.
"""

from typing import Tuple, Optional
from game import TicTacToe


class MinimaxAgent:
    """
    An unbeatable Tic-Tac-Toe agent using the Minimax algorithm.
    """
    
    def __init__(self, player: str = 'O'):
        """
        Initialize the Minimax agent.
        
        Args:
            player: The player marker ('X' or 'O') for this agent
        """
        self.player = player
        self.opponent = 'X' if player == 'O' else 'O'
        self.nodes_explored = 0
        
    def get_best_move(self, game: TicTacToe) -> Tuple[int, int]:
        """
        Find the best move using the Minimax algorithm.
        
        Args:
            game: Current game state
            
        Returns:
            Tuple[int, int]: Best move as (row, col)
        """
        self.nodes_explored = 0
        best_move = None
        best_value = float('-inf')
        
        for move in game.get_valid_moves():
            # Create a copy of the game to simulate the move
            game_copy = game.clone()
            game_copy.make_move(move[0], move[1])
            
            # Get the value of this move using minimax
            move_value = self.minimax(game_copy, depth=0, is_maximizing=False)
            
            # Update best move if this one is better
            if move_value > best_value:
                best_value = move_value
                best_move = move
        
        return best_move
    
    def minimax(self, game: TicTacToe, depth: int, is_maximizing: bool) -> int:
        """
        Minimax algorithm implementation with depth tracking.
        
        Args:
            game: Current game state
            depth: Current depth in the game tree
            is_maximizing: True if maximizing player's turn, False for minimizing
            
        Returns:
            int: Utility value of the state
        """
        self.nodes_explored += 1
        
        # Check for terminal state
        if game.is_terminal():
            utility = game.get_utility(self.player)
            # Adjust utility based on depth to prefer quicker wins
            if utility == 1:
                return 10 - depth
            elif utility == -1:
                return -10 + depth
            else:
                return 0
        
        if is_maximizing:
            # Maximizing player (AI agent)
            max_value = float('-inf')
            for move in game.get_valid_moves():
                game_copy = game.clone()
                game_copy.make_move(move[0], move[1])
                value = self.minimax(game_copy, depth + 1, False)
                max_value = max(max_value, value)
            return max_value
        else:
            # Minimizing player (opponent)
            min_value = float('inf')
            for move in game.get_valid_moves():
                game_copy = game.clone()
                game_copy.make_move(move[0], move[1])
                value = self.minimax(game_copy, depth + 1, True)
                min_value = min(min_value, value)
            return min_value


class MinimaxAlphaBetaAgent(MinimaxAgent):
    """
    Enhanced Minimax agent with Alpha-Beta pruning for improved efficiency.
    """
    
    def get_best_move(self, game: TicTacToe) -> Tuple[int, int]:
        """
        Find the best move using Minimax with Alpha-Beta pruning.
        
        Args:
            game: Current game state
            
        Returns:
            Tuple[int, int]: Best move as (row, col)
        """
        self.nodes_explored = 0
        best_move = None
        best_value = float('-inf')
        alpha = float('-inf')
        beta = float('inf')
        
        for move in game.get_valid_moves():
            game_copy = game.clone()
            game_copy.make_move(move[0], move[1])
            
            move_value = self.minimax_alpha_beta(game_copy, depth=0, 
                                                  alpha=alpha, beta=beta,
                                                  is_maximizing=False)
            
            if move_value > best_value:
                best_value = move_value
                best_move = move
                
            alpha = max(alpha, best_value)
        
        return best_move
    
    def minimax_alpha_beta(self, game: TicTacToe, depth: int, 
                           alpha: float, beta: float, 
                           is_maximizing: bool) -> int:
        """
        Minimax algorithm with Alpha-Beta pruning.
        
        Args:
            game: Current game state
            depth: Current depth in the game tree
            alpha: Best value for maximizer
            beta: Best value for minimizer
            is_maximizing: True if maximizing player's turn
            
        Returns:
            int: Utility value of the state
        """
        self.nodes_explored += 1
        
        # Check for terminal state
        if game.is_terminal():
            utility = game.get_utility(self.player)
            if utility == 1:
                return 10 - depth
            elif utility == -1:
                return -10 + depth
            else:
                return 0
        
        if is_maximizing:
            max_value = float('-inf')
            for move in game.get_valid_moves():
                game_copy = game.clone()
                game_copy.make_move(move[0], move[1])
                value = self.minimax_alpha_beta(game_copy, depth + 1, 
                                               alpha, beta, False)
                max_value = max(max_value, value)
                alpha = max(alpha, max_value)
                
                # Beta cutoff
                if beta <= alpha:
                    break
                    
            return max_value
        else:
            min_value = float('inf')
            for move in game.get_valid_moves():
                game_copy = game.clone()
                game_copy.make_move(move[0], move[1])
                value = self.minimax_alpha_beta(game_copy, depth + 1, 
                                               alpha, beta, True)
                min_value = min(min_value, value)
                beta = min(beta, min_value)
                
                # Alpha cutoff
                if beta <= alpha:
                    break
                    
            return min_value

