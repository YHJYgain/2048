import random
import ui as c
from _global import _current


def new_game(n):
    """
    初始化一个大小为 n x n 的游戏板，并随机添加两个数字 2。
    返回一个表示游戏板的二维列表。
    """
    matrix = []
    for i in range(n):
        matrix.append([0] * n)
    matrix = add_two(matrix)
    matrix = add_two(matrix)
    return matrix


def add_two(mat):
    """
    在游戏板的一个空位置随机添加一个数字 2。
    返回更新后的游戏板。
    """
    a = random.randint(0, len(mat) - 1)
    b = random.randint(0, len(mat) - 1)
    while mat[a][b] != 0:
        a = random.randint(0, len(mat) - 1)
        b = random.randint(0, len(mat) - 1)
    mat[a][b] = 2
    return mat


def game_state(mat):
    """
    检查游戏的状态，返回 'win'、'not over' 或 'lose'。
    """
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 2048:
                return 'win'
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                return 'not over'
    for i in range(len(mat) - 1):
        for j in range(len(mat[0]) - 1):
            if mat[i][j] == mat[i + 1][j] or mat[i][j + 1] == mat[i][j]:
                return 'not over'
    for k in range(len(mat) - 1):
        if mat[len(mat) - 1][k] == mat[len(mat) - 1][k + 1]:
            return 'not over'
    for j in range(len(mat) - 1):
        if mat[j][len(mat) - 1] == mat[j + 1][len(mat) - 1]:
            return 'not over'
    return 'lose'


def reverse(mat):
    """
    反转矩阵的每一行，即将每一行的元素顺序颠倒。
    返回反转后的矩阵。
    """
    new = []
    for i in range(len(mat)):
        new.append([])
        for j in range(len(mat[0])):
            new[i].append(mat[i][len(mat[0]) - j - 1])
    return new


def transpose(mat):
    """
    转置矩阵，即将矩阵的行变为列，列变为行。
    返回转置后的矩阵。
    """
    new = []
    for i in range(len(mat[0])):
        new.append([])
        for j in range(len(mat)):
            new[i].append(mat[j][i])
    return new


def cover_up(mat):
    """
    将矩阵的非零元素向左移动，将所有零元素排在右侧。
    返回移动后的矩阵以及是否有移动操作的标志。
    """
    new = []
    for j in range(c.GRID_LEN):
        partial_new = []
        for i in range(c.GRID_LEN):
            partial_new.append(0)
        new.append(partial_new)
    done = False
    for i in range(c.GRID_LEN):
        count = 0
        for j in range(c.GRID_LEN):
            if mat[i][j] != 0:
                new[i][count] = mat[i][j]
                if j != count:
                    done = True
                count += 1
    return new, done


def merge(mat, done):
    """
    合并矩阵中相邻且相等的元素，并更新分数。
    返回合并后的矩阵以及是否有合并操作的标志。
    """
    for i in range(c.GRID_LEN):
        for j in range(c.GRID_LEN - 1):
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                _current.incScore(mat[i][j] * 2)
                mat[i][j] *= 2
                mat[i][j + 1] = 0
                done = True
    return mat, done


def up(game):
    """
    向上移动游戏板，即先转置为列向上移动，再转置回来。
    返回移动后的游戏板以及是否有移动操作的标志。
    """
    game = transpose(game)
    game, done = cover_up(game)
    game, done = merge(game, done)
    game = cover_up(game)[0]
    game = transpose(game)
    return game, done


def down(game):
    """
    向下移动游戏板，即先转置为列向下移动，再转置回来。
    返回移动后的游戏板以及是否有移动操作的标志。
    """
    game = reverse(transpose(game))
    game, done = cover_up(game)
    game, done = merge(game, done)
    game = cover_up(game)[0]
    game = transpose(reverse(game))
    return game, done


def left(game):
    """
    向左移动游戏板，即先向左移动，再合并相邻相等的元素，再向左移动。
    返回移动后的游戏板以及是否有移动操作的标志。
    """
    game, done = cover_up(game)
    game, done = merge(game, done)
    game = cover_up(game)[0]
    return game, done


def right(game):
    """
    向右移动游戏板，即先向右移动，再合并相邻相等的元素，再向右移动。
    返回移动后的游戏板以及是否有移动操作的标志。
    """
    game = reverse(game)
    game, done = cover_up(game)
    game, done = merge(game, done)
    game = cover_up(game)[0]
    game = reverse(game)
    return game, done
