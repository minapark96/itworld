import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QToolButton, QLabel
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QProgressBar, QPushButton

import random

from qtpy import QtGui

import time


# 버튼 기능 설정



class GhostWarrior(QWidget):

    def __init__(self, t, parent=None):
        super().__init__(parent)
        self.t = t

        # Display Window 06 - 2 계산기 UI 설정
        self.display = QLabel("", self)

        # 타이머인데 자꾸 내 의도와는 다르게 2분 있다가 ui가 뜨고, 뜨고나면 이미 end!라고 적힌 상태이다. 왜이럴까?
        mins, secs = divmod(self.t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        self.display.setText(timeformat)
        while self.t > 0:
            self.display.setText('')  # label에 적혀있던 시간을 지운다.
            # time.sleep(1)
            self.t -= 1  # 1초가 줄어든다.
            self.display.setText(timeformat)  # label에 1초 줄어든 시간을 적는다.
            # self.display.setText('End!') # 120초가 지나면 end! 를 띄운다.

        # 메인 창 설정
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addWidget(self.display, 0, 0, 1, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle("Ghost Warrior")
        self.move(500, 500)

        # Digit Buttons
        # 버튼을 만들고 버튼 사이즈를 조정한다.
        self.digitButton = [x for x in range(0, 9)]
        for i in range(9):
            self.digitButton[i] = QToolButton()
            self.digitButton[i].setIconSize(QtCore.QSize(150, 150))  # 버튼 사이즈 150X150

        numLayout = QGridLayout()  # QGridLayout을 만들어 버튼들을 배열함

        numLayout.addWidget(self.digitButton[0], 0, 0)
        self.digitButton[0].setShortcut("Q")  # setShortcut을 이용해 해당 key랑 버튼이랑 연결시킴
        numLayout.addWidget(self.digitButton[1], 0, 1)
        self.digitButton[1].setShortcut("W")
        numLayout.addWidget(self.digitButton[2], 0, 2)
        self.digitButton[2].setShortcut("E")
        numLayout.addWidget(self.digitButton[3], 1, 0)
        self.digitButton[3].setShortcut("A")
        numLayout.addWidget(self.digitButton[4], 1, 1)
        self.digitButton[4].setShortcut("S")
        numLayout.addWidget(self.digitButton[5], 1, 2)
        self.digitButton[5].setShortcut("D")
        numLayout.addWidget(self.digitButton[6], 2, 0)
        self.digitButton[6].setShortcut("Z")
        numLayout.addWidget(self.digitButton[7], 2, 1)
        self.digitButton[7].setShortcut("X")
        numLayout.addWidget(self.digitButton[8], 2, 2)
        self.digitButton[8].setShortcut("C")

        # 귀신 나타나게 하기 이 부분은 나중에 수정하도록 한다.
        GhostLocation = self.digitButton[random.randint(0, 8)]  # 귀신이 나타날 장소 랜덤으로 정하기

        a = QtGui.QIcon('ghost.png')
        b = QtGui.QIcon('greenEye.png')
        c = QtGui.QIcon('bigEye.png')

        GhostLocation.setIcon(a)
        GhostLocation.setIcon(b)
        GhostLocation.setIcon(c)

        ghostType = [a, a, a, a, b, b, b, c, c]
        random.shuffle(ghostType)  # ghostType 의 리스트 원소를 섞는 역할
        self.digitButton[0].setIcon(ghostType[0])
        self.digitButton[1].setIcon(ghostType[1])
        self.digitButton[2].setIcon(ghostType[2])
        self.digitButton[3].setIcon(ghostType[3])
        self.digitButton[4].setIcon(ghostType[4])
        self.digitButton[5].setIcon(ghostType[5])
        self.digitButton[6].setIcon(ghostType[6])
        self.digitButton[7].setIcon(ghostType[7])
        self.digitButton[8].setIcon(ghostType[8])

        mainLayout.addLayout(numLayout, 1, 0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = GhostWarrior(1)
    game.show()
    sys.exit(app.exec_())

"""
import sys
import time

from PyQt5.QtWidgets import (QApplication, QDialog,
                             QProgressBar, QPushButton)

TIME_LIMIT = 0


class Actions(QDialog): # https://riptutorial.com/pyqt5/example/29500/basic-pyqt-progress-bar


    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('GhostWarrior')
        self.progress = QProgressBar(self)
        self.progress.setGeometry(0, 0, 300, 25)
        #self.progress.setMaximum(100)
        self.progress.setMinimum(0)
        self.button = QPushButton('Start', self)
        self.button.move(0, 30)
        self.show()

        self.button.clicked.connect(self.onButtonClick)

    def onButtonClick(self):
        count = 100
        while count > TIME_LIMIT:
            count -= 1
            time.sleep(1)
            self.progress.setValue(count)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Actions()
    sys.exit(app.exec_())

"""