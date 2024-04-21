import tkinter as tk
from tkinter import messagebox
from tkinter import ttk



def start_game(root):
    # 清空原有的所有组件
    for widget in root.winfo_children():
        widget.destroy()

    print("Cleared old widgets")
    # 创建返回主菜单按钮
    return_button = ttk.Button(root, text="返回主菜单", command=lambda: return_to_menu(root), style='TButton')
    return_button.place(relx=0.1, rely=0.1, anchor=tk.CENTER)
    # 创建分数和历史最高分数的标签
    score_label = ttk.Label(root, text="当前分数: 0", font=("Arial", 24), foreground="#008000")
    score_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    print("Added score label")

    high_score_label = ttk.Label(root, text="历史最高分数: 2048", font=("Arial", 24), foreground="#008000")
    high_score_label.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
    print("Added high score label")

    cells = []
    for i in range(4):
        for j in range(4):
            cell = ttk.Label(root, text="", font=("Arial", 24), width=5, relief="ridge")
            cell.place(relx=(j + 0.5) / 4, rely=(i + 2.5) / 6, anchor=tk.CENTER)
            cells.append(cell)

    print("Added cells")

def return_to_menu(root):
    import menuUi
    menuUi.Game2048(root)