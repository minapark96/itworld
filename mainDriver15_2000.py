import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QToolButton, QLabel
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5 import QtCore
import random

from qtpy import QtGui
from PyQt5.QtCore import QTimer, QTime # 추가
from PyQt5.QtWidgets import QPushButton # 추가
import time

#버튼 기능 설정
class Button(QToolButton):
    def __init__(self, image, callback):
        super().__init__()
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class GhostWarrior(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window 06 - 2 계산기 UI 설정
        self.display = QLabel("", self)

        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.timeout)

        self.btnStart = QPushButton("시작")
        self.btnStart.clicked.connect(self.onStartButtonClicked)

        self.bntStop = QPushButton("종료")
        self.btnStop.clicked.connect(self.onStopButtonClicked)
        # mins, secs = divmod(t, 60)
        # timeformat = '{:02d}:{:02d}'.format(mins, secs)
        # self.display.setText(timeformat)
        # while t:
        #     self.display.setText('')  # label에 적혀있던 시간을 지운다.
        #     time.sleep(1)
        #     t -= 1  # 1초가 줄어든다.
        #     self.display.setText(timeformat)  # label에 1초 줄어든 시간을 적는다.
        # self.display.setText('End!')  # 120초가 지나면 end! 를 띄운다.

        # 메인 창 설정
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addWidget(self.display, 0, 0, 1, 1)
        mainLayout.addWidget(self.btnStart, 0, 0, 2, 1) # 추가
        mainLayout.addWidget(self.btnStop, 0, 0, 2, 2) # 추가

        self.setLayout(mainLayout)
        self.setWindowTitle("Ghost Warrior")
        self.move(500, 500)

        # Digit Buttons
        #버튼을 만들고 버튼 사이즈를 조정한다.
        self.digitButton = [x for x in range(0, 9)]
        for i in range(9):
            self.digitButton[i] = QToolButton()
            self.digitButton[i].setIconSize(QtCore.QSize(150, 150))  # 버튼 사이즈 150X150

        numLayout = QGridLayout() # QGridLayout을 만들어 버튼들을 배열함

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
        GhostLocation.setIcon(QtGui.QIcon('ghost.png'))  # Button 하나를 골라서 ghost.png 이미지 넣기

        self.digitButton[0].setIcon(QtGui.QIcon('ghost.png'))

        mainLayout.addLayout(numLayout, 1, 0)

        #타이머인데 자꾸 내 의도와는 다르게 2분 있다가 ui가 뜨고, 뜨고나면 이미 end!라고 적힌 상태이다. 왜이럴까?

    def timeout(self):
        sender = self.sender()
        currentTime = QTime.currentTime().toString("mm:ss")

        if id(sender) == id(self.timer):
            self.display(currentTime)

        if currentTime == 0:
            self.display("Time Over")

    def printTime(self):
        time = 0
        time += 1
        print(time)
    timeVar = QTimer()
    timeVar.setInterval(10)
    timeVar.timeout.connect(printTime)
    timeVar.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = GhostWarrior()
    game.show()
    sys.exit(app.exec_())