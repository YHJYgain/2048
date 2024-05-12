from src import utils


class current:
    def __init__(self, scores_file="../assets/scoreRecord.db",
                 script_file="../assets/initScoreRecord.sql"):
        """
        创造一个新游戏实例。
            scores_file: 用于获得最佳分数的文件
            store_file: 存储游戏会话的文件
        """
        utils.init(script_file, scores_file)
        self.score = 0
        self.scores_file = scores_file

        self.best_score = 0

        self.loadBestScore()

    def loadBestScore(self):
        """
        从默认文件加载本地最佳分数
        """
        try:
            self.best_score = utils.get_highest_score_record(self.scores_file)[1]
        except:
            return False
        return True

    def saveScore(self):
        """
        在游戏结束时调用该函数保存分数
        """
        try:
            utils.add_record(self.scores_file, self.score)
        except:
            return False
        return True

    def incScore(self, pts):
        """
        通过添加指定的点数来更新当前分数
        """
        self.score += pts
        if self.score > self.best_score:
            self.best_score = self.score

    def getScore(self):
        return self.score

    def getBestScore(self):
        return self.best_score
