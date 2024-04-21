import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from src import utils, constant

utils.init(constant.SCRIPT_FILE,constant.DB_FILE)
from menuUi import Game2048

# back_button = ttk.Button(root, text="返回主菜单", command=lambda: Game2048.return_rank())
def show_history(root):
    # 清空原有的所有组件
    for widget in root.winfo_children():
        widget.destroy()

    # 创建返回主菜单按钮
    return_button = ttk.Button(root, text="返回主菜单", command=lambda: return_to_menu(root), style='TButton')
    return_button.place(relx=0.1, rely=0.1, anchor=tk.CENTER)

    # 创建新的样式
    style = ttk.Style()

    # 设置按钮的样式
    style.configure("TButton", background="#ADD8E6", foreground="black")  # 设置按钮的背景色和字体颜色

    # 创建Treeview组件
    tree = ttk.Treeview(root, columns=("Index", "Score"), show="headings")


    # 设置列标题和字体颜色
    tree.heading("Index", text="排序", anchor=tk.CENTER)
    tree.heading("Score", text="得分", anchor=tk.CENTER)

    tree.column("Index", width=70)  # 设置最小宽度和不拉伸
    tree.column("Score", width=120)  # 设置最小宽度和不拉伸

    tree.tag_configure("blue_font", foreground="black")  # 设置字体颜色为黑色
    tree.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
    # 设置行高和背景色
    style.configure("Treeview", rowheight=30, background="#ADD8E6", foreground="black")  # 设置行高、背景色和字体颜色
    style.configure("Treeview.Heading", background="#ADD8E6", foreground="black")  # 设置表头的背景色和字体颜色

    # 模拟查询结果
    sample_scores = utils.query_records_descending(constant.DB_FILE)

    # 添加数据到Treeview
    for index, score in enumerate(sample_scores, start=1):
        tree.insert("", "end", values=(index, score), tags=("blue_font",))

    # 调整Treeview的布局
    tree.pack(expand=False)  # 设置expand为False使Treeview只占据所需空间
def return_to_menu(root):
    import menuUi
    menuUi.Game2048(root)
