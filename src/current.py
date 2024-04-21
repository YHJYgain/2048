from src import utils
import datetime


class current:
    def __init__(self, scores_file="../assets/scoreRecord.db",
                 script_file="../assets/initScoreRecord.sql", colors=None,
                 store_file="", clear_screen=True,
                 mode=None, azmode=False, **kws):
        """
        Create a new game.
            scores_file: file to use for the best score (default
                         is ~/.term2048.scores)
            colors: dictionnary with colors to use for each tile
            store_file: file that stores game session's snapshot
            mode: color mode. This adjust a few colors and can be 'dark' or
                  'light'. See the adjustColors functions for more info.
            other options are passed to the underlying Board object.
        """
        # self.board = Board(**kws)
        utils.init(script_file, scores_file)
        self.score = 0
        self.scores_file = scores_file
        # self.store_file = store_file
        # self.clear_screen = clear_screen

        self.best_score = 0

        # self.__colors = colors or self.COLORS
        # self.__azmode = azmode

        self.loadBestScore()
        # self.adjustColors(mode)

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
            update the current score by adding it the specified number of points
            """
        self.score += pts
        if self.score > self.best_score:
            self.best_score = self.score

    def getScore(self):
        return self.score

    def getBestScore(self):
        return self.best_score

