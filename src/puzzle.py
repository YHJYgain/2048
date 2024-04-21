from tkinter import Frame, Label, CENTER
import random
import logic
import ui as c
import tkinter as tk
from tkinter import ttk

def gen():
    return random.randint(0, c.GRID_LEN - 1)

class GameGrid:
    def __init__(self, master):
        self.master = master
        for widget in self.master.winfo_children():
            widget.destroy()
            # 创建返回主菜单按钮

        self.master.bind("<Key>", self.key_down)
        self.master.configure(bg="#00FFFF")  # 设置主窗口背景色为蓝绿色
        self.commands = {
            c.KEY_UP: logic.up,
            c.KEY_DOWN: logic.down,
            c.KEY_LEFT: logic.left,
            c.KEY_RIGHT: logic.right,
            c.KEY_UP_ALT1: logic.up,
            c.KEY_DOWN_ALT1: logic.down,
            c.KEY_LEFT_ALT1: logic.left,
            c.KEY_RIGHT_ALT1: logic.right,
            c.KEY_UP_ALT2: logic.up,
            c.KEY_DOWN_ALT2: logic.down,
            c.KEY_LEFT_ALT2: logic.left,
            c.KEY_RIGHT_ALT2: logic.right,
        }

        self.grid_cells = []
        self.matrix = logic.new_game(c.GRID_LEN)
        self.history_matrixs = []

        self.init_grid()
        self.update_grid_cells()

    def init_grid(self):
        # 创建返回主菜单按钮
        return_button = ttk.Button(self.master, text="返回主菜单", command=lambda:return_to_menu(self.master),
                                   style='TButton')
        return_button.grid(row=0, column=0, columnspan=c.GRID_LEN, pady=10, sticky="ew")

        # 创建分数和历史最高分数的标签
        score_label = ttk.Label(self.master, text="当前分数: 0", font=("Arial", 24), foreground="#008000")
        score_label.grid(row=1, column=0, columnspan=c.GRID_LEN, pady=5, sticky="ew")

        high_score_label = ttk.Label(self.master, text="历史最高分数:", font=("Arial", 24), foreground="#008000")
        high_score_label.grid(row=2, column=0, columnspan=c.GRID_LEN, pady=5, sticky="ew")

        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                cell = Frame(
                    self.master,
                    bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                    width=c.SIZE / c.GRID_LEN,
                    height=c.SIZE / c.GRID_LEN
                )
                cell.grid(
                    row=i + 3,  # 从第三行开始放置游戏网格
                    column=j,
                    padx=c.GRID_PADDING,
                    pady=c.GRID_PADDING,
                    sticky="nsew"  # 设置网格单元格填充整个空间
                )
                t = Label(
                    master=cell,
                    text="",
                    bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                    justify=CENTER,
                    font=c.FONT,
                    width=5,
                    height=2)
                t.grid(sticky="nsew")  # 设置标签填充整个网格单元格
                grid_row.append(t)
            self.grid_cells.append(grid_row)
            # 更新窗口大小以适应内容
            self.master.update_idletasks()
            width = self.master.winfo_reqwidth()
            height = self.master.winfo_reqheight()
            x = (self.master.winfo_screenwidth() // 2) - (width // 2)
            y = (self.master.winfo_screenheight() // 2) - (height // 2)
            self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(text="", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(
                        text=str(new_number),
                        bg=c.BACKGROUND_COLOR_DICT[new_number],
                        fg=c.CELL_COLOR_DICT[new_number]
                    )
        self.master.update_idletasks()

    def key_down(self, event):
        key = event.keysym
        if key == c.KEY_QUIT:
            exit()
        if key == c.KEY_BACK and len(self.history_matrixs) > 1:
            self.matrix = self.history_matrixs.pop()
            self.update_grid_cells()
        elif key in self.commands:
            self.matrix, done = self.commands[key](self.matrix)
            if done:
                self.matrix = logic.add_two(self.matrix)
                self.history_matrixs.append(self.matrix)
                self.update_grid_cells()
                if logic.game_state(self.matrix) == 'win':
                    self.grid_cells[1][1].configure(text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Win!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                if logic.game_state(self.matrix) == 'lose':
                    self.grid_cells[1][1].configure(text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Lose!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    import gameoverUi
                    gameoverUi.GameOverUI(self.master)
def return_to_menu(root):
    import menuUi
    menuUi.Game2048(root)
