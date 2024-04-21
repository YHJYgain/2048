import sqlite3
import os

from src import constant


def init(script_file=constant.SCRIPT_FILE, db_file="../assets/scoreRecord.db"):
    """
    初始化ScoreRecord表

    参数:
    db_file (str): SQLite数据库文件路径
    script_file (str): 包含SQL初始化脚本的文件路径
    """
    if not os.path.exists(db_file):
        try:
            # 连接到SQLite数据库
            conn = sqlite3.connect(db_file)
            cursor = conn.cursor()

            # 打开并执行SQL脚本文件
            with open(script_file, 'r') as script:
                cursor.executescript(script.read())

            # 提交并关闭连接
            conn.commit()
            conn.close()
            print("数据库初始化成功！")
        except Exception as e:
            print("数据库初始化失败:", e)
    else:
        print("数据库文件已存在，无需初始化。")


def add_record(db_file, score):
    """
    向ScoreRecord表中添加一条记录

    参数:
    db_file (str): SQLite数据库文件路径
    score (int): 分数
    game_duration (int): 游戏持续时间
    """
    try:
        # 连接到SQLite数据库
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # 执行插入记录的SQL语句
        cursor.execute("INSERT INTO ScoreRecord (Score) VALUES (?)", (score,))

        # 提交并关闭连接
        conn.commit()
        conn.close()
        print("记录添加成功！")
    except Exception as e:
        print("添加记录失败:", e)








def query_records(db_file):
    """
    查询数据库中的所有记录

    参数:
    db_file (str): SQLite数据库文件路径
    """
    try:
        # 连接到SQLite数据库
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # 执行查询所有记录的SQL语句
        cursor.execute("SELECT * FROM ScoreRecord")

        # 获取并打印查询结果
        records = cursor.fetchall()
        for record in records:
            print(record)

        # 关闭连接
        conn.close()
    except Exception as e:
        print("查询记录失败:", e)


def query_records_descending(db_file):
    """
    查询数据库中的所有记录，并按分数降序排列返回结果

    参数:
    db_file (str): SQLite数据库文件路径

    返回:
    list: 按分数降序排列的记录列表
    """
    try:
        # 连接到SQLite数据库
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # 执行查询所有记录的SQL语句，并按分数降序排列
        cursor.execute("SELECT * FROM ScoreRecord ORDER BY Score DESC")

        # 获取查询结果
        scores = [row[1] for row in cursor.fetchall()]
        # 关闭连接
        conn.close()

        return scores
    except Exception as e:
        print("查询记录失败:", e)
        return []


def get_highest_score_record(db_file):
    """
    获取数据库中分数最高的记录

    参数:
    db_file (str): SQLite数据库文件路径

    返回:
    tuple: 分数最高的记录，如果数据库为空则返回 None
    """
    try:
        # 连接到SQLite数据库
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # 执行查询分数最高的记录的SQL语句
        cursor.execute("SELECT * FROM ScoreRecord ORDER BY Score DESC LIMIT 1")

        # 获取查询结果
        highest_score_record = cursor.fetchone()

        # 关闭连接
        conn.close()

        return highest_score_record
    except Exception as e:
        print("获取分数最高记录失败:", e)
        return None


