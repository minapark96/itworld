class Score:
    def __init__(self):
        self.score = "0"

    def plusFiveScore(self):
        self.score = eval(self.score + "5")
        return str(self.score)

    def plusTenScore(self):
        self.score = eval(self.score + "10")
        return str(self.score)

    def minusFiveScore(self):
        self.score = eval(self.score - "5")
        return str(self.score)