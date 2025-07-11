import tkinter as tk
from tkinter import messagebox

class TicTacToe3D:
    def __init__(self, root):
        self.root = root
        self.root.title("3D Tic-Tac-Toe")
        self.board = [[[None for _ in range(3)] for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.current_layer = 0

        self.layer_label = tk.Label(root, text=f"Layer: {self.current_layer}", font=("Arial", 14))
        self.layer_label.pack()

        self.frame = tk.Frame(root)
        self.frame.pack()

        self.buttons = [[[None for _ in range(3)] for _ in range(3)] for _ in range(3)]
        self.create_buttons()

        nav_frame = tk.Frame(root)
        nav_frame.pack(pady=10)

        tk.Button(nav_frame, text="Previous Layer", command=self.prev_layer).pack(side=tk.LEFT, padx=5)
        tk.Button(nav_frame, text="Next Layer", command=self.next_layer).pack(side=tk.LEFT, padx=5)

    def create_buttons(self):
        for y in range(3):
            for x in range(3):
                btn = tk.Button(self.frame, text=" ", width=6, height=3,
                                command=lambda x=x, y=y: self.make_move(self.current_layer, y, x))
                btn.grid(row=y, column=x)
                self.buttons[self.current_layer][y][x] = btn

    def update_buttons(self):
        for y in range(3):
            for x in range(3):
                value = self.board[self.current_layer][y][x]
                self.buttons[self.current_layer][y][x].config(text=value if value else " ")

    def make_move(self, z, y, x):
        if self.board[z][y][x] is None:
            self.board[z][y][x] = self.current_player
            self.update_buttons()
            if self.check_winner(self.current_player):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.root.quit()
            elif self.is_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.root.quit()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def prev_layer(self):
        if self.current_layer > 0:
            self.current_layer -= 1
            self.layer_label.config(text=f"Layer: {self.current_layer}")
            self.update_buttons()

    def next_layer(self):
        if self.current_layer < 2:
            self.current_layer += 1
            self.layer_label.config(text=f"Layer: {self.current_layer}")
            self.update_buttons()

    def is_full(self):
        return all(self.board[z][y][x] is not None for z in range(3) for y in range(3) for x in range(3))

    def check_winner(self, player):
        b = self.board
        for z in range(3):
            for i in range(3):
                if all(b[z][i][j] == player for j in range(3)) or all(b[z][j][i] == player for j in range(3)):
                    return True
        for y in range(3):
            for x in range(3):
                if all(b[z][y][x] == player for z in range(3)):
                    return True
        for z in range(3):
            if all(b[z][i][i] == player for i in range(3)) or all(b[z][i][2 - i] == player for i in range(3)):
                return True
        for x in range(3):
            if all(b[i][i][x] == player for i in range(3)) or all(b[i][2 - i][x] == player for i in range(3)):
                return True
        for y in range(3):
            if all(b[i][y][i] == player for i in range(3)) or all(b[i][y][2 - i] == player for i in range(3)):
                return True
        if all(b[i][i][i] == player for i in range(3)) or \
           all(b[i][i][2 - i] == player for i in range(3)) or \
           all(b[i][2 - i][i] == player for i in range(3)) or \
           all(b[i][2 - i][2 - i] == player for i in range(3)):
            return True
        return False

root = tk.Tk()
game = TicTacToe3D(root)
root.mainloop()
