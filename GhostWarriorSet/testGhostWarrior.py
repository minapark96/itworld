import unittest
from gstScore import Score

class TestGhostWarrior(unittest.TestCase):
    def test_GhostWarrior(self):
        # GhostWarrrior 가 메소드가 없고,
        # 검증이 필요할 만한 부분은
        #         for i in range(9):
#             self.digitButton[i].setShortcut(keyPad[i])  # key와 버튼을 연결
#             if i // 3 == 0:
#                 numLayout.addWidget(self.digitButton[i], 0, i)
#             elif i // 3 == 1:
#                 numLayout.addWidget(self.digitButton[i], 1, i - 3)
#             else:
#                 numLayout.addWidget(self.digitButton[i], 2, i - 6)
        # 을 하는 방법을 도저히 모르겠습니다.

    def testPlusFiveScore(self):
        self.score1 = gstScore("100")
        score1.plusFiveScore
        self.assertTrue(self.score1.plusFiveScore())

    def testPlusTenScore(self):
        self.score2 = gstScore("200")
        score2.plusTenScore
        self.assertTrue(self.score2.plusTenScore())

    def testMinusScore(self):
        self.score3 = gstScore("300")
        score3.MinusFiveScore
        self.assertTrue(self.score3.minusFiveScore())



if__name__ == '__main__':
    unittest.main()