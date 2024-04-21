import sqlite3
import os


def __init__(script_file, db_file='../assets/scoreRecord.db'):
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


def add_record(db_file, score, game_duration):
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
        cursor.execute("INSERT INTO ScoreRecord (Score, GameDuration) VALUES (?, ?)", (score, game_duration))

        # 提交并关闭连接
        conn.commit()
        conn.close()
        print("记录添加成功！")
    except Exception as e:
        print("添加记录失败:", e)


def delete_record(db_file, record_id):
    """
    删除数据库中的一条记录

    参数:
    db_file (str): SQLite数据库文件路径
    record_id (int): 要删除的记录的ID
    """
    try:
        # 连接到SQLite数据库
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # 执行删除记录的SQL语句
        cursor.execute("DELETE FROM ScoreRecord WHERE RecordID = ?", (record_id,))

        # 提交并关闭连接
        conn.commit()
        conn.close()
        print("记录删除成功！")
    except Exception as e:
        print("删除记录失败:", e)


def update_record(db_file, record_id, score, game_duration):
    """
    更新数据库中的一条记录

    参数:
    db_file (str): SQLite数据库文件路径
    record_id (int): 要更新的记录的ID
    score (int): 新的分数
    game_duration (int): 新的游戏持续时间
    """
    try:
        # 连接到SQLite数据库
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # 执行更新记录的SQL语句
        cursor.execute("UPDATE ScoreRecord SET Score = ?, GameDuration = ? WHERE RecordID = ?",
                       (score, game_duration, record_id))

        # 提交并关闭连接
        conn.commit()
        conn.close()
        print("记录更新成功！")
    except Exception as e:
        print("更新记录失败:", e)


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
        records = cursor.fetchall()

        # 关闭连接
        conn.close()

        return records
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


