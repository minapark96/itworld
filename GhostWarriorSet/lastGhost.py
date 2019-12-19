import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QToolButton, QLabel
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5 import QtCore
import random
#from gstScore import Score

from qtpy import QtGui

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
            #time.sleep(1)
            self.t -= 1  # 1초가 줄어든다.
            self.display.setText(timeformat)  # label에 1초 줄어든 시간을 적는다.
        #self.display.setText('End!')  # 120초가 지나면 end! 를 띄운다.

        # 메인 창 설정
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addWidget(self.display, 0, 0, 1, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle("Ghost Warrior")
        self.move(500, 500)

        # Digit Buttons
        #버튼을 만들고 버튼 사이즈를 조정한다.
        self.digitButton = [x for x in range(9)]
        for i in range(9):
            self.digitButton[i] = QToolButton()
            self.digitButton[i].setIconSize(QtCore.QSize(150, 150))  # 버튼 사이즈 150X150

        numLayout = QGridLayout() # QGridLayout을 만들어 버튼들을 배열함

        keyPad = ['Q', 'W', 'E', 'A', 'S', 'D', 'Z', 'X', 'C']

        for i in range(9):
            self.digitButton[i].setShortcut(keyPad[i])  # key와 버튼을 연결
            if i // 3 == 0:
                numLayout.addWidget(self.digitButton[i], 0, i)
            elif i // 3 == 1:
                numLayout.addWidget(self.digitButton[i], 1, i - 3)
            else:
                numLayout.addWidget(self.digitButton[i], 2, i - 6)

        # 귀신 나타나게 하기 이 부분은 나중에 수정하도록 한다.
        GhostLocation = self.digitButton[random.randint(0, 8)]  # 귀신이 나타날 장소 랜덤으로 정하기

        originalEye = QtGui.QIcon('ghost.png')
        greenEye = QtGui.QIcon('greenEye.png')
        bigEye = QtGui.QIcon('bigEye.png')

        GhostLocation.setIcon(originalEye)
        GhostLocation.setIcon(greenEye)
        GhostLocation.setIcon(bigEye)

        ghostType = [originalEye, originalEye, originalEye, originalEye, greenEye, greenEye, greenEye, bigEye, bigEye]
        random.shuffle(ghostType)  # ghostType 의 리스트 원소를 섞는 역할
        for i in range(9):
            self.digitButton[i].setIcon(ghostType[i])

        mainLayout.addLayout(numLayout, 1, 0)

        # scr = QLabel()
        # scr.setText('')
        #
        # if originalEye.clicked():
        #     originalEye.clicked.connect(Score().plusFiveScore())
        #     scr.setText(Score.score)
        #
        # elif greenEye.clicked():
        #     greenEye.clicked.connect(Score().plusTenScore())
        #     scr.setText(Score.score)
        #
        # elif bigEye.clicked():
        #     bigEye.clicked.connect(Score().minusFiveScore())
        #     scr.setText(Score.score)
        #
        # else:
        #     scr.setText("Input 오류 입니다")
        # mainLayout.addWidget(scr, 2, 0)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = GhostWarrior(1)
    game.show()
    sys.exit(app.exec_())