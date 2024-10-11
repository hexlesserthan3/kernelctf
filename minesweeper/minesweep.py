#initial code without the special cells
import tkinter as tk
import random

class Minesweeper:
    def __init__(self, master, dim_size=10, num_bombs=10):
        self.master = master
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        self.buttons = {}
        self.board = self.make_new_board()
        self.assign_values_to_board()
        self.dug = set()

        self.create_widgets()

    def make_new_board(self):
        # Set a random seed for consistent bomb placement
        random.seed(42)  # This ensures the bombs are placed the same every time

        # Create a new board with bombs placed randomly
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        bombs_planted = 0

        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*':
                continue

            board[row][col] = '*'
            bombs_planted += 1

        return board

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

    def on_click(self, row, col):
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
            self.buttons[(row, col)].config(text=str(self.board[row][col]), state="disabled")
        else:
            self.buttons[(row, col)].config(state="disabled")

            for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
                for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                    if (r, c) in self.dug:
                        continue
                    self.dig(r, c)

    def game_over(self, won):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    self.buttons[(r, c)].config(text='*', bg='red')
                elif (r, c) in self.dug:
                    self.buttons[(r, c)].config(text=str(self.board[r][c]) if self.board[r][c] > 0 else ' ', state="disabled")

        if won:
            result_text = "You Win!"
        else:
            result_text = "Game Over!"

        result_label = tk.Label(self.master, text=result_text, font=("Helvetica", 20))
        result_label.grid(row=self.dim_size, column=0, columnspan=self.dim_size)

def play_minesweeper(dim_size=10, num_bombs=10):
    root = tk.Tk()
    root.title("Minesweeper")
    game = Minesweeper(root, dim_size, num_bombs)
    root.mainloop()

if __name__ == '__main__':
    play_minesweeper()

