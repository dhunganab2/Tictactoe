import random
import sys


class MinimaxTicTacToe:

    def __init__(self):
        # A list of 9 items representing the 3x3 board
        self.board = [" " for _ in range(9)]
        self.human = "O"
        self.ai = "X"

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
        # All winning combinations (rows, cols, diagonals)
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
    # PHASE 2 LOGIC: MINIMAX ALGORITHM (The Improvement)
    # ---------------------------------------------------------
    
    def minimax(self, board, depth, is_maximizing):
        """
        Recursive function to determine the value of a board state.
        Scores: +10 for AI win, -10 for Human win, 0 for Draw.
        Depth is used to prefer winning sooner or losing later.
        """
        
        # 1. Base Cases (Terminal States)
        if self.is_winner(self.ai, board):
            return 10 - depth  # Win sooner is better
        if self.is_winner(self.human, board):
            return -10 + depth # Lose later is better
        if self.is_full(board):
            return 0           # Draw

        # 2. Recursive Step
        if is_maximizing:
            best_score = -float('inf')
            for move in self.get_available_moves(board):
                board[move] = self.ai
                score = self.minimax(board, depth + 1, False)
                board[move] = " " # Undo move (backtrack)
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for move in self.get_available_moves(board):
                board[move] = self.human
                score = self.minimax(board, depth + 1, True)
                board[move] = " " # Undo move (backtrack)
                best_score = min(score, best_score)
            return best_score

    def get_minimax_move(self, verbose=True):
        """
        Entry point for the AI to find the best move using Minimax.
        """
        best_score = -float('inf')
        best_move = None
        
        available_moves = self.get_available_moves(self.board)
        
        if verbose:
            print("AI Thinking (Minimax Recursion)...")

        for move in available_moves:
            # Make the move tentatively
            self.board[move] = self.ai
            
            # Calculate score for this move using Minimax
            score = self.minimax(self.board, 0, False)
            
            # Undo the move
            self.board[move] = " "

            if verbose:
                print(f"  Spot {move}: Minimax Score {score}")

            if score > best_score:
                best_score = score
                best_move = move
        
        if verbose:
            print(f"AI chooses spot {best_move} with optimal score {best_score}")

        return best_move

    # ---------------------------------------------------------
    # GAME LOOP (Same as Heuristic, just uses Minimax)
    # ---------------------------------------------------------

    def play(self):
        self.reset_board()
        print("--- Minimax Tic Tac Toe (Unbeatable) ---")
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
                print("Congratulations! You beat Minimax! (This shouldn't happen...)")
                break

            if self.is_full(self.board):
                self.print_board()
                print("It's a Draw!")
                break

            # AI Turn
            print("AI is calculating...")
            ai_move = self.get_minimax_move(verbose=True)
            self.board[ai_move] = self.ai
            
            if self.is_winner(self.ai, self.board):
                self.print_board()
                print("AI Wins! (Minimax is invincible)")
                break
            if self.is_full(self.board):
                self.print_board()
                print("It's a Draw!")
                break

    def simulate(self, max_games=10):
        """
        Simulates AI (Minimax) vs Random Player for benchmarking.
        """
        print(f"\n--- Starting Simulation: Minimax AI vs Random Player ({max_games} games) ---")
        ai_wins = 0
        random_wins = 0
        draws = 0
        total_moves = 0

        for game_num in range(1, max_games + 1):
            self.reset_board()
            ai_turn = (game_num % 2 == 1) 
            current_player_name = "AI" if ai_turn else "Random"
            
            print(f"\nGame {game_num}: {current_player_name} starts.")
            
            while True:
                if ai_turn:
                    # AI Turn - Minimax (silent)
                    move = self.get_minimax_move(verbose=False)
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
                        print(f"  -> Random Player Wins Game {game_num} (Impossible?)")
                        break
                    if self.is_full(self.board):
                        draws += 1
                        print(f"  -> Game {game_num} Draw")
                        break
                    ai_turn = True
        
        print("\n" + "=" * 40)
        print("📊 SIMULATION RESULTS (Minimax)")
        print("=" * 40)
        print(f"Total Games: {max_games}")
        print(f"AI Wins:     {ai_wins} ({(ai_wins/max_games)*100:.1f}%)")
        print(f"Random Wins: {random_wins} ({(random_wins/max_games)*100:.1f}%)")
        print(f"Draws:       {draws} ({(draws/max_games)*100:.1f}%)")
        print("=" * 40)


if __name__ == "__main__":
    game = MinimaxTicTacToe()
    
    while True:
        print("\n" + "="*30)
        print("   MINIMAX MENU (UNBEATABLE)")
        print("="*30)
        print("1. Play against Minimax AI")
        print("2. Run Simulation (Minimax vs Random)")
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

