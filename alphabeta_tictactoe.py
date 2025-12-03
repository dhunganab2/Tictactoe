import random
import sys


class AlphaBetaTicTacToe:

    def __init__(self):
        # A list of 9 items representing the 3x3 board
        self.board = [" " for _ in range(9)]
        self.human = "O"
        self.ai = "X"
        self.states_evaluated = 0  # Counter to show efficiency

    def reset_board(self):
        self.board = [" " for _ in range(9)]

    def print_board(self):
        print("\n")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print("\n")

    def is_winner(self, player, board_state):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Cols
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]
        for a, b, c in win_conditions:
            if board_state[a] == board_state[b] == board_state[c] == player:
                return True
        return False

    def is_full(self, board_state):
        return " " not in board_state

    def get_available_moves(self, board_state):
        return [i for i, spot in enumerate(board_state) if spot == " "]

    # ---------------------------------------------------------
    # PHASE 3 LOGIC: ALPHA-BETA PRUNING (The Optimization)
    # ---------------------------------------------------------
    
    def minimax_alphabeta(self, board, depth, is_maximizing, alpha, beta):
        """
        Optimized Minimax.
        alpha: Best value that the maximizer (AI) can guarantee at that level or above.
        beta: Best value that the minimizer (Human) can guarantee at that level or above.
        """
        self.states_evaluated += 1
        
        # 1. Base Cases
        if self.is_winner(self.ai, board):
            return 10 - depth
        if self.is_winner(self.human, board):
            return -10 + depth
        if self.is_full(board):
            return 0

        # 2. Recursive Step with Pruning
        if is_maximizing:
            best_score = -float('inf')
            for move in self.get_available_moves(board):
                board[move] = self.ai
                score = self.minimax_alphabeta(board, depth + 1, False, alpha, beta)
                board[move] = " " # Undo
                best_score = max(score, best_score)
                
                # Update Alpha
                alpha = max(alpha, best_score)
                
                # Pruning: If alpha >= beta, the minimizer will never allow this branch
                if beta <= alpha:
                    break 
            return best_score
        else:
            best_score = float('inf')
            for move in self.get_available_moves(board):
                board[move] = self.human
                score = self.minimax_alphabeta(board, depth + 1, True, alpha, beta)
                board[move] = " " # Undo
                best_score = min(score, best_score)
                
                # Update Beta
                beta = min(beta, best_score)
                
                # Pruning
                if beta <= alpha:
                    break
            return best_score

    def get_best_move(self, verbose=True):
        """
        Entry point for Alpha-Beta Search.
        """
        self.states_evaluated = 0 # Reset counter
        best_score = -float('inf')
        best_move = None
        
        available_moves = self.get_available_moves(self.board)
        
        # Optional: Shuffle moves to add randomness if scores are equal (makes AI less predictable)
        random.shuffle(available_moves)
        
        if verbose:
            print("AI Thinking (Alpha-Beta Search)...")

        alpha = -float('inf')
        beta = float('inf')

        for move in available_moves:
            self.board[move] = self.ai
            
            # Call optimized minimax
            score = self.minimax_alphabeta(self.board, 0, False, alpha, beta)
            
            self.board[move] = " "
            
            if verbose:
                print(f"  Spot {move}: Score {score}")

            if score > best_score:
                best_score = score
                best_move = move
            
            # Update alpha at the root level too
            alpha = max(alpha, best_score)
        
        if verbose:
            print(f"AI chooses spot {best_move} (States evaluated: {self.states_evaluated})")

        return best_move

    # ---------------------------------------------------------
    # GAME LOOP
    # ---------------------------------------------------------

    def play(self):
        self.reset_board()
        print("--- Alpha-Beta Tic Tac Toe (Optimized & Unbeatable) ---")
        print("You are 'O'. AI is 'X'.")
        
        while True:
            self.print_board()
            
            # Human Turn
            try:
                move = int(input("Enter your move (0-8): "))
                if self.board[move] != " ":
                    print("Invalid move! Spot taken.")
                    continue
            except (ValueError, IndexError):
                print("Invalid input! Please enter a number 0-8.")
                continue

            self.board[move] = self.human
            if self.is_winner(self.human, self.board):
                self.print_board()
                print("Congratulations! You beat the AI! (Impossible!)")
                break

            if self.is_full(self.board):
                self.print_board()
                print("It's a Draw!")
                break

            # AI Turn
            print("AI is calculating...")
            ai_move = self.get_best_move(verbose=True)
            self.board[ai_move] = self.ai
            
            if self.is_winner(self.ai, self.board):
                self.print_board()
                print("AI Wins! (Alpha-Beta logic prevailed)")
                break
            if self.is_full(self.board):
                self.print_board()
                print("It's a Draw!")
                break

    def simulate(self, max_games=10):
        print(f"\n--- Starting Simulation: Alpha-Beta AI vs Random Player ({max_games} games) ---")
        ai_wins = 0
        random_wins = 0
        draws = 0
        total_states = 0

        for game_num in range(1, max_games + 1):
            self.reset_board()
            ai_turn = (game_num % 2 == 1) 
            current_player_name = "AI" if ai_turn else "Random"
            
            print(f"\nGame {game_num}: {current_player_name} starts.")
            
            while True:
                if ai_turn:
                    # AI Turn
                    move = self.get_best_move(verbose=False)
                    total_states += self.states_evaluated # Track efficiency
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
                        print(f"  -> Random Player Wins (Impossible?)")
                        break
                    if self.is_full(self.board):
                        draws += 1
                        print(f"  -> Game {game_num} Draw")
                        break
                    ai_turn = True
        
        print("\n" + "=" * 50)
        print(" SIMULATION RESULTS (Alpha-Beta Optimized)")
        print("=" * 50)
        print(f"Total Games:      {max_games}")
        print(f"AI Wins:          {ai_wins} ({(ai_wins/max_games)*100:.1f}%)")
        print(f"Random Wins:      {random_wins} ({(random_wins/max_games)*100:.1f}%)")
        print(f"Draws:            {draws} ({(draws/max_games)*100:.1f}%)")
        print(f"Avg Nodes Explored: {total_states // max(1, ai_wins + draws + random_wins)} per game")
        print("=" * 50)


if __name__ == "__main__":
    game = AlphaBetaTicTacToe()
    
    while True:
        print("\n" + "="*30)
        print("   ALPHA-BETA MENU")
        print("="*30)
        print("1. Play against Alpha-Beta AI")
        print("2. Run Simulation (Benchmark)")
        print("3. Exit")
        
        choice = input("Enter 1, 2, or 3: ")
        
        if choice == "1":
            game.play()
        elif choice == "2":
            try:
                num_games = int(input("How many games to simulate? (e.g. 20): "))
                game.simulate(max_games=num_games)
            except ValueError:
                print("Invalid number!")
        elif choice == "3":
            print("Goodbye.")
            sys.exit()
        else:
            print("Invalid choice.")

