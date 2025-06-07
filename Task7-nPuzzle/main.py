import tkinter as tk
from Astar import astar

class PuzzleGUI:   # making the main visual window
    def __init__(self, root):
        self.root = root
        self.root.title("Your A* 15-puzzle solver")

        self.grid_frame = tk.Frame(root)
        self.grid_frame.pack()

        self.instruction = tk.Label(root, text="Shuffle and then hit START")
        self.instruction.pack(pady=5)

        self.start_button = tk.Button(root, text="START", command=self.solve_puzzle)
        self.start_button.pack(pady=5)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=5)

        self.tiles = list(range(1, 16)) + [0]
        self.buttons = [[None for _ in range(4)] for _ in range(4)]

        self.create_buttons()
        self.update_buttons()

    def create_buttons(self):   # creating buttons for the 4by4 grid
        for i in range(4):
            for j in range(4):
                btn = tk.Button(self.grid_frame, width=4, height=2, font=('Arial', 18),
                                command=lambda row=i, col=j: self.button_click(row, col))
                btn.grid(row=i, column=j, padx=2, pady=2)
                self.buttons[i][j] = btn

    def update_buttons(self, tiles=None):   # updating buttons after user clicks
        if tiles is None:
            tiles = self.tiles
        for i in range(4):
            for j in range(4):
                val = tiles[i * 4 + j]
                if val == 0:
                    self.buttons[i][j].config(text="", state="disabled", bg="lightgray")
                else:
                    self.buttons[i][j].config(text=str(val), state="normal", bg="SystemButtonFace")

    def button_click(self, row, col):   # action to take when user clicks buttons to shuffle them
        index = row * 4 + col
        zero_index = self.tiles.index(0)
        zr, zc = divmod(zero_index, 4)

        if abs(zr - row) + abs(zc - col) == 1:
            self.tiles[zero_index], self.tiles[index] = self.tiles[index], self.tiles[zero_index]
            self.update_buttons()

    def solve_puzzle(self):   # calling the "astar" function to solve for the puzzle and report results
        initial_state = tuple(self.tiles)
        result = astar(initial_state)

        if result["path"]:
            self.result_label.config(
                text=f"Puzzle solved with {result['moves']} moves in {result['time']:.4f} seconds."
            )
            self.animate_solution(result["path"])
        else:
            self.result_label.config(text="Unsolvable")

    def animate_solution(self, path):   # showing each step to animate the solution
        def show_step(index):
            if index < len(path):
                self.update_buttons(path[index])
                self.root.after(500, lambda: show_step(index + 1))

        show_step(0)

if __name__ == "__main__":
    root = tk.Tk()
    gui = PuzzleGUI(root)
    root.mainloop()