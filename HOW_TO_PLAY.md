# 🎮 How to Play Tic-Tac-Toe vs Minimax AI

## Quick Start (Easiest Way)

### Option 1: Simple Launcher (Recommended)
```bash
cd /Users/bijaydhungana/Desktop/CSC425/AI_Final_Project
python3 start_game.py
```

### Option 2: Full Menu Interface
```bash
cd /Users/bijaydhungana/Desktop/CSC425/AI_Final_Project
python3 main.py
```

---

## 📋 Game Features

✅ **3x3 Board** - Classic Tic-Tac-Toe grid  
✅ **Human vs AI** - You play against the Minimax algorithm  
✅ **Unbeatable AI** - Uses optimal game theory strategy  
✅ **Two Algorithms**:
   - Standard Minimax
   - Minimax with Alpha-Beta Pruning (faster)

---

## 🎯 How to Play

### Board Coordinates
```
     0   1   2
   0 . | . | .
   1 . | . | .
   2 . | . | .
```

### Making Moves
Enter your move as: `row col`

**Examples:**
- `0 0` → Top-left corner
- `1 1` → Center
- `0 2` → Top-right corner
- `2 2` → Bottom-right corner

### Game Flow
1. Choose who goes first (human or AI)
2. You are **X**, AI is **O**
3. Take turns placing marks
4. First to get 3 in a row wins!
5. If board fills up with no winner → Draw

---

## 🤖 About the AI

The AI uses the **Minimax Algorithm** with **Alpha-Beta Pruning**:

- **Explores all possible moves** ahead of time
- **Chooses optimal strategy** to never lose
- **Guaranteed outcomes:**
  - AI never loses
  - Perfect human play → Draw
  - Any mistake → AI wins

### Algorithm Features
- ✅ Looks ahead to all possible game endings
- ✅ Evaluates best and worst case scenarios
- ✅ Picks moves that maximize AI's chances
- ✅ Prunes unnecessary branches for efficiency

---

## 📊 Expected Results

| Scenario | Result |
|----------|--------|
| You play perfectly | Draw |
| AI plays perfectly | Draw or AI wins |
| Both play perfectly | Always draw |
| You make a mistake | AI wins |

**Challenge:** Can you force a draw? 🏆

---

## 🎮 All Available Programs

### 1. **start_game.py** (Simplest - Play Now!)
```bash
python3 start_game.py
```
- Quick start
- Clean interface
- Best for playing

### 2. **main.py** (Full Featured)
```bash
python3 main.py
```
- Multiple game modes
- Choose algorithm type
- AI vs AI mode

### 3. **demo.py** (Watch AI Play)
```bash
python3 demo.py
```
- Automated demonstrations
- Algorithm comparisons
- No user input needed

### 4. **utils.py** (Testing & Analysis)
```bash
python3 utils.py
```
- Performance testing
- Algorithm comparison
- Statistical analysis

### 5. **play_game.py** (Simulated Game)
```bash
python3 play_game.py
```
- Watch a simulated match
- See AI strategy in action

### 6. **quick_test.py** (Verify It Works)
```bash
python3 quick_test.py
```
- Fast verification
- Shows AI is working

---

## 💡 Pro Tips

### Strategy Tips
1. **Take the center (1,1)** if you go first
2. **Take a corner** if center is taken
3. **Block AI's winning moves** immediately
4. **Create two threats at once** (fork strategy)
5. **Don't make obvious mistakes** - AI will punish!

### To Force a Draw
1. If X: Start with center or corner
2. Always block AI's three-in-a-row
3. Try to create your own threats
4. With perfect play, you can guarantee a draw

---

## 🐛 Troubleshooting

**Problem:** "command not found: python3"
```bash
# Try using python instead
python start_game.py
```

**Problem:** "No module named 'game'"
```bash
# Make sure you're in the right directory
cd /Users/bijaydhungana/Desktop/CSC425/AI_Final_Project
ls  # Should see game.py, minimax.py, etc.
```

**Problem:** Game won't take input
- Make sure you're running in Terminal (not through IDE)
- Use Command+C to quit if stuck

---

## 📚 For Your Project Report

### What to Highlight
1. **Implementation:**
   - 3x3 board representation
   - Minimax algorithm with recursion
   - Alpha-Beta pruning optimization
   
2. **Results:**
   - AI is unbeatable
   - Alpha-Beta is 50-80% more efficient
   - Always draws with perfect play

3. **Game Theory:**
   - Tic-Tac-Toe is a "solved game"
   - Demonstrates zero-sum game strategy
   - Shows perfect information game tree search

---

## 🎓 Educational Value

This project demonstrates:
- ✅ Adversarial search algorithms
- ✅ Game tree exploration
- ✅ Minimax decision making
- ✅ Alpha-Beta pruning optimization
- ✅ Optimal strategy in zero-sum games

---

## 👥 Authors

**Aryan Kafle & Bijay Dhungana**  
CSC425 - Artificial Intelligence  
Term Project - Milestone 2

---

**Have fun playing! Try to beat (or at least tie) the AI! 🎮🤖**

