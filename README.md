AI Tic-Tac-Toe Project

This project implements three different AI strategies for playing Tic-Tac-Toe, ranging from basic heuristic rules to unbeatable algorithms. It also includes a scalable Monte Carlo Tree Search (MCTS) implementation for larger boards.

Files Overview
1. heuristic_tictactoe.py: A rule-based AI (Center > Corner > Edge). Fast but can lose.
2. minimax_tictactoe.py: Uses the Minimax algorithm. Unbeatable but checks every possible move.
3. alphabeta_tictactoe.py: Optimized Minimax with Alpha-Beta pruning. Unbeatable and much faster.
4. mcts_tictactoe.py: Uses Monte Carlo Tree Search. Works for 3x3, 4x4, and 5x5 boards.

How to Run
You can run any file directly using Python.

Example:
python3 alphabeta_tictactoe.py

When running a file, you will see a menu to choose between:
- Play against AI
- Run Simulation (AI vs Random Player)

Performance Comparison
We simulated 100 games for each AI against a random player.

Method          | Win Rate | Loss Rate | Nodes Explored (Approx)
----------------|----------|-----------|------------------------
Heuristic       | 85%      | 15%       | ~25
Minimax         | 100%     | 0%        | ~550,000
Alpha-Beta      | 100%     | 0%        | ~2,000
MCTS (3x3)      | 99%      | 0-1%      | 1000 iterations

Key Findings
- Heuristic is fast but imperfect.
- Minimax is perfect but slow.
- Alpha-Beta is the best for standard 3x3 (Perfect and Fast).
- MCTS is required for larger boards where Minimax is too slow.
