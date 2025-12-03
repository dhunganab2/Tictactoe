import random
import math
import sys

class MCTSNode:
    def __init__(self, board, parent=None, move=None, player="X"):
        self.board = board
        self.parent = parent
        self.move = move
        self.player = player  # The player who just moved to create this state
        self.children = []
        self.wins = 0
        self.visits = 0
        self.untried_moves = self.get_available_moves(board)

    def get_available_moves(self, board):
        return [i for i, spot in enumerate(board) if spot == " "]

    def is_fully_expanded(self):
        return len(self.untried_moves) == 0

    def best_child(self, c_param=1.41):
        # Upper Confidence Bound 1 (UCB1) algorithm
        choices_weights = [
            (child.wins / child.visits) + c_param * math.sqrt((2 * math.log(self.visits) / child.visits))
            for child in self.children
        ]
        return self.children[choices_weights.index(max(choices_weights))]

class MCTSTicTacToe:
    def __init__(self, size=3):
        self.size = size
        self.board = [" " for _ in range(size * size)]
        self.human = "O"
        self.ai = "X"
        self.nodes_evaluated = 0 # Actually "Iterations" in MCTS context

    def reset_board(self):
        self.board = [" " for _ in range(self.size * self.size)]

    def print_board(self):
        print("\n")
        for row in range(self.size):
            start = row * self.size
            line = " | ".join(self.board[start:start + self.size])
            print(f" {line} ")
            if row < self.size - 1:
                print("-" * (self.size * 4 - 1))
        print("\n")

    def is_winner(self, player, board):
        # Check Rows
        for row in range(self.size):
            if all(board[row * self.size + col] == player for col in range(self.size)):
                return True
        # Check Cols
        for col in range(self.size):
            if all(board[row * self.size + col] == player for row in range(self.size)):
                return True
        # Check Diagonals
        if all(board[i * self.size + i] == player for i in range(self.size)):
            return True
        if all(board[i * self.size + (self.size - 1 - i)] == player for i in range(self.size)):
            return True
        return False

    def is_full(self, board):
        return " " not in board

    def get_available_moves(self, board):
        return [i for i, spot in enumerate(board) if spot == " "]

    # ---------------------------------------------------------
    # PHASE 4 LOGIC: MONTE CARLO TREE SEARCH (Scalable AI)
    # ---------------------------------------------------------
    
    def get_mcts_move(self, iterations=1000, verbose=True):
        """
        Runs MCTS to find the best move.
        Does NOT search the whole tree. Simulates random games.
        """
        self.nodes_evaluated = 0
        # Root node represents the opponent's last move (current state)
        # So we say the "player" who made the move to get here was 'O' (Human)
        root = MCTSNode(board=self.board[:], player=self.human) 

        for _ in range(iterations):
            self.nodes_evaluated += 1
            node = root
            temp_board = self.board[:]

            # 1. Selection
            # Go down the tree to a leaf node or unexpanded node
            while node.is_fully_expanded() and node.children:
                node = node.best_child()
                temp_board[node.move] = node.player

            # 2. Expansion
            # If we reached a node that isn't terminal and has untried moves, add a child
            if not node.is_fully_expanded() and not self.is_winner("X", temp_board) and not self.is_winner("O", temp_board):
                move = random.choice(node.untried_moves)
                node.untried_moves.remove(move)
                
                player_moving = "X" if node.player == "O" else "O"
                temp_board[move] = player_moving
                
                new_node = MCTSNode(temp_board, parent=node, move=move, player=player_moving)
                node.children.append(new_node)
                node = new_node

            # 3. Simulation (Rollout)
            # Play random moves until game over
            current_player = node.player
            while not self.is_winner("X", temp_board) and not self.is_winner("O", temp_board) and " " in temp_board:
                current_player = "X" if current_player == "O" else "O"
                possible_moves = [i for i, x in enumerate(temp_board) if x == " "]
                if not possible_moves: break
                move = random.choice(possible_moves)
                temp_board[move] = current_player

            # 4. Backpropagation
            # Propagate the result back up the tree
            winner = None
            if self.is_winner("X", temp_board): winner = "X"
            elif self.is_winner("O", temp_board): winner = "O"
            
            while node is not None:
                node.visits += 1
                if winner == self.ai: # AI (X) won
                    # If the node's player is X, that move led to a win for X. Good!
                    if node.player == self.ai: 
                        node.wins += 1
                    # If node's player is O, that means O's move allowed X to win later. Bad for O? 
                    # (Simplified logic: usually we invert score for opponent nodes)
                    # For simplicity here: +1 win for the player who just moved if they won.
                elif winner == self.human: # Human (O) won
                    if node.player == self.human:
                        node.wins += 1 
                node = node.parent

        if not root.children:
            return random.choice(self.get_available_moves(self.board))
            
        # Select the child with the most visits (most robust move)
        best_child = max(root.children, key=lambda c: c.visits)
        
        if verbose:
            print(f"AI chooses spot {best_child.move} (Simulations: {iterations})")
            
        return best_child.move

    def play(self):
        print(f"--- MCTS Tic Tac Toe ({self.size}x{self.size}) ---")
        print("You are 'O'. AI is 'X'.")
        
        while True:
            self.print_board()
            
            # Human Turn
            try:
                move = int(input(f"Enter move (0-{self.size*self.size-1}): "))
                if self.board[move] != " ":
                    print("Invalid move! Spot taken.")
                    continue
            except (ValueError, IndexError):
                print(f"Invalid input! Please enter a number 0-{self.size*self.size-1}.")
                continue

            self.board[move] = self.human
            if self.is_winner(self.human, self.board):
                self.print_board()
                print("Congratulations! You beat the AI!")
                break

            if self.is_full(self.board):
                self.print_board()
                print("It's a Draw!")
                break

            # AI Turn
            print("AI Thinking (MCTS Simulation)...")
            # Increase iterations for larger boards to maintain intelligence
            iters = 1000 if self.size == 3 else 5000 
            ai_move = self.get_mcts_move(iterations=iters)
            self.board[ai_move] = self.ai
            
            if self.is_winner(self.ai, self.board):
                self.print_board()
                print("AI Wins!")
                break
            if self.is_full(self.board):
                self.print_board()
                print("It's a Draw!")
                break

    def simulate(self, max_games=10):
        print(f"\n--- Starting Simulation: MCTS AI ({self.size}x{self.size}) vs Random Player ({max_games} games) ---")
        ai_wins = 0
        random_wins = 0
        draws = 0
        total_iterations = 0

        iters = 1000 if self.size == 3 else 3000

        for game_num in range(1, max_games + 1):
            self.reset_board()
            ai_turn = (game_num % 2 == 1) 
            current_player_name = "AI" if ai_turn else "Random"
            
            print(f"\nGame {game_num}: {current_player_name} starts.")
            
            while True:
                if ai_turn:
                    # AI Turn
                    move = self.get_mcts_move(iterations=iters, verbose=False)
                    total_iterations += iters
                    self.board[move] = self.ai
                    
                    if self.is_winner(self.ai, self.board):
                        ai_wins += 1
                        print(f"  -> AI Wins Game {game_num}")
                        break
                    if self.is_full(self.board):
                        draws += 1
                        print(f"  -> Game {game_num} Draw")
                        break
                    ai_turn = False
                else:
                    # Random Player Turn
                    available = self.get_available_moves(self.board)
                    move = random.choice(available)
                    self.board[move] = self.human
                    
                    if self.is_winner(self.human, self.board):
                        random_wins += 1
                        print(f"  -> Random Player Wins (Lucky!)")
                        break
                    if self.is_full(self.board):
                        draws += 1
                        print(f"  -> Game {game_num} Draw")
                        break
                    ai_turn = True
        
        print("\n" + "=" * 50)
        print(f"📊 SIMULATION RESULTS (MCTS - {self.size}x{self.size})")
        print("=" * 50)
        print(f"Total Games:      {max_games}")
        print(f"AI Wins:          {ai_wins} ({(ai_wins/max_games)*100:.1f}%)")
        print(f"Random Wins:      {random_wins} ({(random_wins/max_games)*100:.1f}%)")
        print(f"Draws:            {draws} ({(draws/max_games)*100:.1f}%)")
        print(f"Iterations/Move:  {iters} (Fixed)")
        print("=" * 50)

if __name__ == "__main__":
    while True:
        print("\n" + "="*30)
        print("   MCTS MENU (SCALABLE AI)")
        print("="*30)
        print("1. Play 3x3 (Standard)")
        print("2. Play 4x4 (Large)")
        print("3. Play 5x5 (Super)")
        print("4. Run Simulation (3x3)")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            game = MCTSTicTacToe(size=3)
            game.play()
        elif choice == "2":
            game = MCTSTicTacToe(size=4)
            game.play()
        elif choice == "3":
            game = MCTSTicTacToe(size=5)
            game.play()
        elif choice == "4":
            game = MCTSTicTacToe(size=3)
            try:
                num = int(input("Games to simulate: "))
                game.simulate(max_games=num)
            except ValueError:
                pass
        elif choice == "5":
            sys.exit()

