from tkinter import Tk, Frame, Label, Button, CENTER
import tkinter.font as tkFont
from _global import _current
import logic
import ui as c


class GameOverUI:
    def __init__(self, master):
        self.master = master

        # 清空主界面
        for widget in self.master.winfo_children():
            widget.destroy()

        # 窗口大小
        self.master.geometry("800x600")

        # 显示分数
        self.score_label = Label(

            text="当前分数: " + str(_current.getScore()),
            font=tkFont.Font(family="Arial", size=24),
            justify=CENTER
        )
        self.score_label.place(relx=0.5, rely=0.4, anchor=CENTER)

        # 显示按钮
        self.return_button = Button(
            text="返回主菜单",
            font=tkFont.Font(family="Arial", size=20),
            command=self.return_to_menu
        )
        self.return_button.place(relx=0.35, rely=0.6, anchor=CENTER)

        self.restart_button = Button(
            text="重新开始",
            font=tkFont.Font(family="Arial", size=20),
            command=self.restart_game
        )
        self.restart_button.place(relx=0.65, rely=0.6, anchor=CENTER)

    def return_to_menu(self):
        # 返回主菜单
        import menuUi
        menuUi.Game2048(self.master)

    def restart_game(self):
        # 重新开始游戏
        import puzzle
        puzzle.GameGrid(self.master)
