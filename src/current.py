from src import utils
import datetime


class current:
    def __init__(self, scores_file="../assets/scoreRecord.db",
                 script_file="../assets/initScoreRecord.sql"):
        """
        Create a new game.
            scores_file: 用于获得最佳分数的文件
            colors: dictionnary with colors to use for each tile
            store_file: file that stores game session's snapshot
            mode: color mode. This adjust a few colors and can be 'dark' or
                  'light'. See the adjustColors functions for more info.
            other options are passed to the underlying Board object.
        """
        utils.init(script_file, scores_file)
        self.score = 0
        self.scores_file = scores_file

        self.best_score = 0

        self.loadBestScore()

    def loadBestScore(self):
        """
        load local best score from the default file
        """
        try:
            self.best_score = utils.get_highest_score_record(self.scores_file)[1]
        except:
            return False
        return True

    def saveScore(self):
        """
            save current best score in the default file
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
