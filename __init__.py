"""
Tic-Tac-Toe AI Agent Package
CSC425 Term Project
Authors: Aryan Kafle, Bijay Dhungana

An unbeatable Tic-Tac-Toe AI agent using Minimax algorithm
with optional Alpha-Beta pruning optimization.
"""

__version__ = "1.0.0"
__authors__ = ["Aryan Kafle", "Bijay Dhungana"]
__course__ = "CSC425 - Artificial Intelligence"

from .game import TicTacToe
from .minimax import MinimaxAgent, MinimaxAlphaBetaAgent

__all__ = [
    'TicTacToe',
    'MinimaxAgent',
    'MinimaxAlphaBetaAgent',
]

