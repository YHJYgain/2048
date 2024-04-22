import random
import ui as c
from _global import _current


# 矩阵元素必须相等但不相同
# 1 标记用于创建正确的矩阵

def new_game(n):
    matrix = []
    for i in range(n):
        matrix.append([0] * n)
    matrix = add_two(matrix)
    matrix = add_two(matrix)
    return matrix


# 任务 1b #
# 必须确保它是在零条目上创建的
# 1 个标记用于创建正确的循环

def add_two(mat):
    a = random.randint(0, len(mat) - 1)
    b = random.randint(0, len(mat) - 1)
    while mat[a][b] != 0:
        a = random.randint(0, len(mat) - 1)
        b = random.randint(0, len(mat) - 1)
    mat[a][b] = 2
    return mat


# 任务 1c #

# 矩阵元素必须相等但不相同
# 完全错误的解决方案得 0 分
# 只答对一个条件得 1 分
# 满足三个条件中的两个则得 2 分
# 正确检查得 3 分

def game_state(mat):
    # check for win cell
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 2048:
                return 'win'
    # check for any zero entries
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                return 'not over'
    # check for same cells that touch each other
    for i in range(len(mat) - 1):
        # intentionally reduced to check the row on the right and below
        # more elegant to use exceptions but most likely this will be their solution
        for j in range(len(mat[0]) - 1):
            if mat[i][j] == mat[i + 1][j] or mat[i][j + 1] == mat[i][j]:
                return 'not over'
    for k in range(len(mat) - 1):  # to check the left/right entries on the last row
        if mat[len(mat) - 1][k] == mat[len(mat) - 1][k + 1]:
            return 'not over'
    for j in range(len(mat) - 1):  # check up/down entries on last column
        if mat[j][len(mat) - 1] == mat[j + 1][len(mat) - 1]:
            return 'not over'
    return 'lose'



# 任务 2a #

# 完全错误的解决方案得 0 分
# 1 分表示具有一般理解的解决方案
# 2 分表示适用于所有大小矩阵的正确解决方案

def reverse(mat):
    new = []
    for i in range(len(mat)):
        new.append([])
        for j in range(len(mat[0])):
            new[i].append(mat[i][len(mat[0]) - j - 1])
    return new


def transpose(mat):
    new = []
    for i in range(len(mat[0])):
        new.append([])
        for j in range(len(mat)):
            new[i].append(mat[j][i])
    return new



# 任务 3 #

# 移动的方式是压缩 -> 合并 -> 再次压缩
# 基本上，如果他们可以解决一侧问题，并正确使用转置和反转，他们应该
# 只需翻转矩阵就能解决整个问题
# 目前不知道如何给这个评分。 我把它固定在 8（这让你喜欢，
# 上/下/左/右各 2 个，但是如果你答对了一个，很可能全部答对
# 检查下一个。 如果顺序错误，则反转/转置将给出错误的结果。

def cover_up(mat):
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
    for i in range(c.GRID_LEN):
        for j in range(c.GRID_LEN - 1):
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                _current.incScore(mat[i][j] * 2)
                mat[i][j] *= 2
                mat[i][j + 1] = 0
                done = True
    return mat, done


def up(game):
    print("up")
    #返回上移后的矩阵
    game = transpose(game)
    game, done = cover_up(game)
    game, done = merge(game, done)
    game = cover_up(game)[0]
    game = transpose(game)
    return game, done


def down(game):
    print("down")
    # 返回下移后的矩阵
    game = reverse(transpose(game))
    game, done = cover_up(game)
    game, done = merge(game, done)
    game = cover_up(game)[0]
    game = transpose(reverse(game))
    return game, done


def left(game):
    print("left")
    # 返回左移后的矩阵
    game, done = cover_up(game)
    game, done = merge(game, done)
    game = cover_up(game)[0]
    return game, done


def right(game):
    print("right")
    # 返回右移后的矩阵
    game = reverse(game)
    game, done = cover_up(game)
    game, done = merge(game, done)
    game = cover_up(game)[0]
    game = reverse(game)
    return game, done
