"""
Tic-Tac-Toe Game Environment
CSC425 Term Project - Milestone 2
Authors: Aryan Kafle, Bijay Dhungana

This module defines the Tic-Tac-Toe game board, state representation,
and basic game mechanics.
"""

from typing import List, Tuple, Optional
from copy import deepcopy


class TicTacToe:
    """
    Tic-Tac-Toe game environment with state management and move validation.
    """
    
    def __init__(self):
        """Initialize an empty 3x3 Tic-Tac-Toe board."""
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'  # X always starts
        
    def reset(self):
        """Reset the board to initial empty state."""
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        
    def clone(self) -> 'TicTacToe':
        """
        Create a deep copy of the current game state.
        
        Returns:
            TicTacToe: A new independent instance with the same state
        """
        new_game = TicTacToe()
        new_game.board = deepcopy(self.board)
        new_game.current_player = self.current_player
        return new_game
        
    def get_valid_moves(self) -> List[Tuple[int, int]]:
        """
        Get all valid moves (empty cells) on the current board.
        
        Returns:
            List[Tuple[int, int]]: List of (row, col) tuples representing valid moves
        """
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    moves.append((i, j))
        return moves
    
    def make_move(self, row: int, col: int) -> bool:
        """
        Make a move on the board for the current player.
        
        Args:
            row: Row index (0-2)
            col: Column index (0-2)
            
        Returns:
            bool: True if move was valid and made, False otherwise
        """
        if row < 0 or row > 2 or col < 0 or col > 2:
            return False
            
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False
    
    def check_winner(self) -> Optional[str]:
        """
        Check if there is a winner on the current board.
        
        Returns:
            Optional[str]: 'X' if X wins, 'O' if O wins, 'Draw' if board is full,
                          None if game is still ongoing
        """
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
        
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        
        # Check for draw (board full)
        if all(self.board[i][j] != ' ' for i in range(3) for j in range(3)):
            return 'Draw'
        
        return None
    
    def is_terminal(self) -> bool:
        """
        Check if the game has reached a terminal state.
        
        Returns:
            bool: True if game is over, False otherwise
        """
        return self.check_winner() is not None
    
    def get_utility(self, player: str) -> int:
        """
        Get the utility value of the current state from the perspective of the given player.
        
        Args:
            player: The player ('X' or 'O') for whom to evaluate utility
            
        Returns:
            int: +1 if player wins, -1 if player loses, 0 for draw or ongoing game
        """
        winner = self.check_winner()
        if winner == player:
            return 1
        elif winner == 'Draw':
            return 0
        elif winner is not None:  # Opponent wins
            return -1
        return 0
    
    def display(self):
        """Display the current board state in a readable format."""
        print("\n  0   1   2")
        for i, row in enumerate(self.board):
            print(f"{i} {row[0]} | {row[1]} | {row[2]}")
            if i < 2:
                print(" -----------")
        print()
    
    def __str__(self) -> str:
        """String representation of the board."""
        result = "\n  0   1   2\n"
        for i, row in enumerate(self.board):
            result += f"{i} {row[0]} | {row[1]} | {row[2]}\n"
            if i < 2:
                result += " -----------\n"
        return result

