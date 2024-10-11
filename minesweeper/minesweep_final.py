import tkinter as tk
import random

class Minesweeper:
    def __init__(self, master, dim_size=10, num_bombs=10):
        self.master = master
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        self.buttons = {}
        self.board = None
        self.dug = set()
        self.create_widgets()
        
        self.start_new_game()

    def start_new_game(self):
        random.seed(42)  # Set a seed for consistent bomb placement, remove for random placement every time
        self.dug.clear()

        # Create a new board with bombs placed randomly
        self.board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        bombs_planted = 0   

        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if self.board[row][col] == '*':
                continue

            self.board[row][col] = '*'
            bombs_planted += 1
            
        self.board[4][8] = 6
        self.board[8][0] = 2
        self.board[9][0] = 1
        self.board[7][2] = 4
        self.board[9][9] = 5
        self.board[4][1] = 0
        self.board[5][2] = 9
        self.board[7][5] = 3
        self.board[8][4] = 8
        self.board[9][5] = 7
            
        print("Bomb placements:")
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    print(f"Bomb at: ({r}, {c})")

        # Assign values to cells based on the number of neighboring bombs
        self.assign_values_to_board()

    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
        num_neighboring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1
        return num_neighboring_bombs

    def create_widgets(self):
        # Create a grid of buttons
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                button = tk.Button(self.master, width=3, height=1, command=lambda row=r, col=c: self.on_click(row, col))
                button.grid(row=r, column=c)
                self.buttons[(r, c)] = button
    
    def update_square(self, row, col, new_value):
        self.board[row][col] = new_value
        self.buttons[(row, col)].config(text=str(new_value))

    def on_click(self, row, col):
        if row == 4 and col == 8:
            self.update_square(row, col, 6)
            return?
        if row == 8 and col == 0:
            self.update_square(row, col, 2)
            return
        if row == 9 and col == 0:
            self.update_square(row, col, 1)
            return
        if row == 7 and col == 2:
            self.update_square(row, col, 4)
            return
        if row == 9 and col == 9:
            self.update_square(row, col, 5)
            return
        if row == 4 and col == 1:
            self.update_square(row, col, 0)
            return
        if row == 5 and col == 2:
            self.update_square(row, col, 9)
            return
        if row == 7 and col == 5:
            self.update_square(row, col, 3)
            return
        if row == 8 and col == 4:
            self.update_square(row, col, 8)
            return
        if row == 9 and col == 5:
            self.update_square(row, col, 7)
            return
            
        # If player digs a bomb, end the game
        if self.board[row][col] == '*':
            self.game_over(False)
        else:
            self.dig(row, col)
            if len(self.dug) == self.dim_size**2 - self.num_bombs:
                self.game_over(True)

    def dig(self, row, col):
        if (row, col) in self.dug:
            return
        self.dug.add((row, col))

        if self.board[row][col] > 0:
            # Customize the numbers displayed around bombs
            number = self.board[row][col]
            custom_number = f"({number})"  # Example customization: wrap the number in parentheses
            self.buttons[(row, col)].config(text=custom_number, state="disabled")
        else:
            self.buttons[(row, col)].config(state="disabled")

            for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
                for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                    if (r, c) in self.dug:
                        continue
                    self.dig(r, c)

    def game_over(self, won):
        # Reveal all bombs and disable buttons
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    self.buttons[(r, c)].config(text='*', bg='red')
                elif (r, c) in self.dug:
                    self.buttons[(r, c)].config(text=str(self.board[r][c]) if self.board[r][c] > 0 else ' ', state="disabled")

        result_text = "You Win!" if won else "Game Over!"
        result_label = tk.Label(self.master, text=result_text, font=("Helvetica", 20))
        result_label.grid(row=self.dim_size + 1, column=0, columnspan=self.dim_size)

def play_minesweeper(dim_size=10, num_bombs=10):
    root = tk.Tk()
    root.title("Minesweeper")
    game = Minesweeper(root, dim_size, num_bombs)
    root.mainloop()

if __name__ == '__main__':
    play_minesweeper()

