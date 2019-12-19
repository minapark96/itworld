# 질문 1 되고 점수 더한다음에 버튼 누르면 del 이용해서 질문 1 버리고 새로운 질문 2 띄워주기
#


import sys
from PyQt5.QtWidgets import *

class WindowClass(QMainWindow) :
    def __init__(self) :
        super().__init__()

        questionList = ["하루 중에서 기분이 제일 좋을 때는?", "길을 걸을 때 나의 걸음을?", "사람들과 이야기할 때 나는?"
                                                                   "편안하게 쉴 때 나는?", "재밌는 일이 생겼을 때 나는?"]

        questionShow = QLabel(questionList[0], self)
        questionShow.move(15, 10)

        #GroupBox안에 있는 RadioButton들을 연결합니다.
        #GroupBox의 자세한 설명은 02.14 GroupBox를 참고하세요.
        self.groupBox_rad1.clicked.connect(self.groupboxRadFunction)
        self.groupBox_rad2.clicked.connect(self.groupboxRadFunction)
        self.groupBox_rad3.clicked.connect(self.groupboxRadFunction)
        self.groupBox_rad4.clicked.connect(self.groupboxRadFunction)

    def groupboxRadFunction(self) :
        if self.groupBox_rad1.isChecked() : print("GroupBox_rad1 Chekced")
        elif self.groupBox_rad2.isChecked() : print("GroupBox_rad2 Checked")
        elif self.groupBox_rad3.isChecked() : print("GroupBox_rad3 Checked")
        elif self.groupBox_rad4.isChecked() : print("GroupBox_rad4 Checked")

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()