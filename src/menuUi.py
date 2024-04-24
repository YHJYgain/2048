import tkinter as tk
from tkinter import ttk


class Game2048:
    def __init__(self, master):
        for widget in master.winfo_children():
            widget.destroy()
        self.master = master
        self.master.title("2048 Game")
        self.master.geometry("800x600")  # 设置窗口大小为 800x600 像素
        self.master.configure(bg="#98FB98")  # 设置窗口背景色为浅绿色

        # 自定义样式设置主题
        self.style = ttk.Style()

        # 设置主题为浅绿色
        self.style.configure('.', background='#98FB98')

        # 设置按钮颜色为浅紫色，选中时为浅黄色
        self.style.map('TButton', background=[('active', '#FFD700'), ('!disabled', '#D8BFD8')],
                       foreground=[('!disabled', '#008000')])  # 设置为葱绿色

        # 添加 2048 标题，设置字体颜色为葱绿色，并放大两倍
        self.title_label = ttk.Label(self.master, text="2048", font=("Arial", 96, "bold"),
                                     foreground="#008000")  # 字体大小放大到 96
        self.title_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        # 创建开始游戏按钮
        self.start_button = ttk.Button(self.master, text="开始游戏", command=self.start_game, style='TButton')
        self.start_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        self.style.configure('TButton', font=("Arial", 24))  # 设置按钮字体大小为 24

        # 创建查看历史分数按钮
        self.history_button = ttk.Button(self.master, text="查看历史分数", command=self.show_history, style='TButton')
        self.history_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.root1 = self.master

    def start_game(self):
        from puzzle import GameGrid
        GameGrid(self.master)

    def show_history(self):
        import rankUi
        rankUi.show_history(self.master)


if __name__ == "__main__":
    root = tk.Tk()
    game = Game2048(root)
    root.mainloop()
