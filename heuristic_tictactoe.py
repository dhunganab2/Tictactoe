import random
import sys


class HeuristicTicTacToe:

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

    def is_full(self):
        return " " not in self.board

    def get_available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def get_heuristic_move(self, verbose=True):
        """
        Phase 1 Logic: Score every empty spot and pick the highest score.
        Returns best_move.
        """
        best_score = -1
        best_move = None
        scores = {}

        # Get all empty spots indices
        available_moves = self.get_available_moves()
        if verbose:
            print("AI Thinking (Heuristic Scores):")

        for move in available_moves:
            score = 0

            # Create a temporary copy of the board to test the move
            temp_board = self.board[:]

            # 1. CHECK FOR WIN (Highest Priority)
            temp_board[move] = self.ai
            if self.is_winner(self.ai, temp_board):
                score = 100
                reason = "WIN"
            else:
                # 2. CHECK FOR BLOCK (High Priority)
                # See if opponent would win if they took this spot
                temp_board[move] = self.human
                if self.is_winner(self.human, temp_board):
                    score = 50
                    reason = "BLOCK"
                else:
                    # 3. STRATEGIC POSITIONING
                    if move == 4:  # Center
                        score = 5
                        reason = "CENTER"
                    elif move in [0, 2, 6, 8]:  # Corners
                        score = 3
                        reason = "CORNER"
                    else:  # Edges
                        score = 1
                        reason = "EDGE"
            
            scores[move] = (score, reason)

            if verbose:
                print(f"  Spot {move}: Score {score} ({reason})")
            
            # If this move is better than what we found so far, keep it
            if score > best_score:
                best_score = score
                best_move = move

        if verbose:
            print(f"AI chooses spot {best_move} with score {best_score}")
            
        return best_move

    def play(self):
        self.reset_board()
        print("--- Heuristic Tic Tac Toe ---")
        print("You are 'O'. AI is 'X'.")
        print("Positions are 0-8 (0 is top-left, 8 is bottom-right).")

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
                print("Congratulations! You beat the Heuristic AI!")
                break

            if self.is_full():
                self.print_board()
                print("It's a Draw!")
                break

            # AI Turn
            print("AI is calculating...")
            ai_move = self.get_heuristic_move(verbose=True)
            self.board[ai_move] = self.ai
            if self.is_winner(self.ai, self.board):
                self.print_board()
                print("AI Wins! (Heuristic logic prevailed)")
                break
            if self.is_full():
                self.print_board()
                print("It's a Draw!")
                break

    def simulate(self, max_games=10):
        """
        Simulates AI (X) vs Random Player (O) for a number of games.
        Use this to benchmark improvement.
        """
        print(f"\n--- Starting Simulation: Heuristic AI vs Random Player ({max_games} games) ---")
        ai_wins = 0
        random_wins = 0
        draws = 0
        total_moves = 0

        for game_num in range(1, max_games + 1):
            self.reset_board()
            # Alternate starting player
            ai_turn = (game_num % 2 == 1) 
            current_player_name = "AI" if ai_turn else "Random"
            
            print(f"\nGame {game_num}: {current_player_name} starts.")
            
            while True:
                if ai_turn:
                    # AI Turn - Use Heuristic but suppress detailed logs for speed
                    move = self.get_heuristic_move(verbose=False)
                    self.board[move] = self.ai
                    total_moves += 1
                    
                    if self.is_winner(self.ai, self.board):
                        ai_wins += 1
                        print(f"  -> AI Wins Game {game_num}")
                        break
                    if self.is_full():
                        draws += 1
                        print(f"  -> Game {game_num} Draw")
                        break
                    ai_turn = False
                else:
                    # Random Player Turn
                    available = self.get_available_moves()
                    move = random.choice(available)
                    self.board[move] = self.human
                    total_moves += 1
                    
                    if self.is_winner(self.human, self.board):
                        random_wins += 1
                        print(f"  -> Random Player Wins Game {game_num} (Lucky!)")
                        break
                    if self.is_full():
                        draws += 1
                        print(f"  -> Game {game_num} Draw")
                        break
                    ai_turn = True
        
        print("\n" + "=" * 40)
        print(" SIMULATION RESULTS (Heuristic)")
        print("=" * 40)
        print(f"Total Games: {max_games}")
        print(f"AI Wins:     {ai_wins} ({(ai_wins/max_games)*100:.1f}%)")
        print(f"Random Wins: {random_wins} ({(random_wins/max_games)*100:.1f}%)")
        print(f"Draws:       {draws} ({(draws/max_games)*100:.1f}%)")
        print("=" * 40)


if __name__ == "__main__":
    game = HeuristicTicTacToe()
    
    while True:
        print("\n" + "="*30)
        print("   MAIN MENU")
        print("="*30)
        print("1. Play against AI")
        print("2. Run Simulation (AI vs Random)")
        print("3. Exit")
        
        choice = input("Enter 1, 2, or 3: ")
        
        if choice == "1":
            game.play()
        elif choice == "2":
            try:
                num_games = int(input("How many games to simulate? (e.g. 20): "))
                game.simulate(max_games=num_games)
            except ValueError:
                print("Invalid number! Please enter an integer.")
        elif choice == "3":
            print("Thanks for playing! Goodbye.")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")
