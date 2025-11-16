# Tic-Tac-Toe AI Agent

**CSC425 Term Project - Milestone 2**  
**Authors:** Aryan Kafle, Bijay Dhungana

## Project Overview

This project implements an unbeatable Tic-Tac-Toe AI agent using the **Minimax algorithm** with optional **Alpha-Beta pruning**. The agent is designed to never lose by making optimal decisions at every step using adversarial search techniques.

## Features

- ✅ **Complete Tic-Tac-Toe game environment** with state management
- ✅ **Standard Minimax algorithm** implementation
- ✅ **Minimax with Alpha-Beta pruning** for improved efficiency
- ✅ **Human vs AI gameplay** with interactive interface
- ✅ **AI vs AI comparison** mode
- ✅ **Comprehensive testing suite** for validation and performance analysis
- ✅ **Performance comparison** between algorithms

## Project Structure

```
AI_Final_Project/
│
├── game.py              # Tic-Tac-Toe game environment and state representation
├── minimax.py           # Minimax algorithm implementations
├── main.py              # Main game interface for human interaction
├── utils.py             # Testing and analysis utilities
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
```

## Installation

1. **Clone or download the project:**
   ```bash
   cd AI_Final_Project
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   *Note: This project uses only Python standard library, so no external packages are required.*

## Usage

### Playing Against the AI

Run the main interface:

```bash
python main.py
```

**Game Modes:**
1. **Human vs AI (Standard Minimax)** - Play against the AI using basic Minimax
2. **Human vs AI (Alpha-Beta Pruning)** - Play against the optimized AI
3. **AI vs AI** - Watch two AI agents play against each other
4. **Exit** - Quit the program

**How to Play:**
- The board is represented as a 3x3 grid with coordinates (row, col)
- Rows and columns are numbered 0-2
- Enter your move as: `row col` (e.g., `1 1` for center)
- You play as **X**, AI plays as **O**

### Running Tests and Analysis

Run the testing suite:

```bash
python utils.py
```

**Available Tests:**
1. **Test unbeatable agent** - Verify AI never loses over N games
2. **Compare algorithms** - Performance comparison between Minimax variants
3. **First move advantage analysis** - Analyze optimal opening moves
4. **Verbose game trace** - See detailed move-by-move analysis

## Implementation Details

### Game Environment (`game.py`)

The `TicTacToe` class provides:
- **State representation** using a 3x3 array
- **Move generation** to find valid moves
- **Terminal state detection** (win/loss/draw)
- **Utility function** for state evaluation
- **State cloning** for search tree exploration

### Minimax Algorithm (`minimax.py`)

Two implementations are provided:

#### 1. Standard Minimax
```python
MinimaxAgent(player='O')
```
- Explores the entire game tree
- Guarantees optimal play
- No pruning optimizations

#### 2. Alpha-Beta Pruning
```python
MinimaxAlphaBetaAgent(player='O')
```
- Prunes branches that don't affect the final decision
- Significantly reduces nodes explored
- Same optimal results as standard Minimax

**Key Features:**
- Depth-aware utility values (prefer faster wins)
- Node counting for performance analysis
- Support for both maximizing and minimizing players

### Algorithm Pseudocode

**Minimax Algorithm:**
```
function MINIMAX(state, depth, isMaximizing):
    if state is terminal:
        return utility(state, player)
    
    if isMaximizing:
        maxValue = -∞
        for each valid move:
            child = result(state, move)
            value = MINIMAX(child, depth+1, False)
            maxValue = max(maxValue, value)
        return maxValue
    else:
        minValue = +∞
        for each valid move:
            child = result(state, move)
            value = MINIMAX(child, depth+1, True)
            minValue = min(minValue, value)
        return minValue
```

**Alpha-Beta Pruning Enhancement:**
```
function ALPHA-BETA(state, depth, α, β, isMaximizing):
    if state is terminal:
        return utility(state, player)
    
    if isMaximizing:
        maxValue = -∞
        for each valid move:
            child = result(state, move)
            value = ALPHA-BETA(child, depth+1, α, β, False)
            maxValue = max(maxValue, value)
            α = max(α, maxValue)
            if β ≤ α:
                break  # β cutoff
        return maxValue
    else:
        minValue = +∞
        for each valid move:
            child = result(state, move)
            value = ALPHA-BETA(child, depth+1, α, β, True)
            minValue = min(minValue, value)
            β = min(β, minValue)
            if β ≤ α:
                break  # α cutoff
        return minValue
```

## Performance Analysis

### Expected Results

When both algorithms are tested, you should observe:

1. **Unbeatable Performance:**
   - Against perfect play: Always draw
   - Against imperfect play: Win or draw, never lose

2. **Algorithm Comparison:**
   - **Standard Minimax:** ~5,000-10,000 nodes per game (first moves)
   - **Alpha-Beta Pruning:** ~500-2,000 nodes per game (first moves)
   - **Improvement:** 50-80% reduction in nodes explored

3. **Game Theory Results:**
   - Tic-Tac-Toe is a **solved game**
   - With optimal play, game always results in a **draw**
   - First player (X) has no significant advantage

## Testing

To verify the AI is unbeatable:

```bash
python utils.py
# Select option 3 to compare algorithms
```

This will:
- Run 50+ games for each algorithm
- Verify no losses occur
- Compare performance metrics
- Display statistical analysis

## Key Concepts Demonstrated

1. **Adversarial Search**
   - Game tree exploration
   - Minimax decision rule
   - Alpha-Beta pruning optimization

2. **Game Theory**
   - Zero-sum games
   - Perfect information games
   - Optimal strategies

3. **Algorithm Analysis**
   - Time complexity: O(b^m) where b = branching factor, m = max depth
   - Space complexity: O(bm) for depth-first implementation
   - Pruning effectiveness in reducing search space

## Future Enhancements (Milestone 3)

Planned improvements:
- [ ] Iterative deepening for time-limited decisions
- [ ] Transposition tables for state memoization
- [ ] Opening book for faster initial moves
- [ ] Monte Carlo Tree Search (MCTS) comparison
- [ ] GUI interface using Pygame or Tkinter
- [ ] Performance visualization and statistics dashboard

## References

- Russell, S., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.)
- Chapter 5: Adversarial Search and Games
- Minimax Algorithm: Section 5.2
- Alpha-Beta Pruning: Section 5.3

## License

This project is created for educational purposes as part of CSC425 coursework.

## Authors

- **Aryan Kafle**
- **Bijay Dhungana**

**Course:** CSC425 - Artificial Intelligence  
**Institution:** [Your Institution Name]  
**Date:** November 2025

---

For questions or issues, please contact the authors or submit an issue on the project repository.

