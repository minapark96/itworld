import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton, QPushButton
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5 import QtCore
import random

from PyQt5 import QtGui
import time



class Button(QToolButton):  # 버튼에 대한 것, QToolButton -> QPushButton 이어야 하지 않나? 스택오버플로우 예시들을 보면 괄호안이 저거라서, 근데 그걸로 바꾸면 Abstract 어쩌고 떠서 일단 이걸로 냅뒀어

    def __init__(self, img, callback):
        super().__init__()
        self.img = img # img 받아야 할 것 같아서 만들었어
        self.clicked.connect(callback)

    def getImage(self):
        self.img = QtGui.QImage('ghost.png')
        self.setIcon(QtGui.QIcon('ghost.png'))

    #이거 아닌가 봄 https://lsjsj92.tistory.com/319 이미지 업로드 하려고 넣은 건데ㅠㅠ
    # def image(self):
    #     uploadImage = QtGui.QImage('ghost.png')  # Qmage 이미지 가져오기
    #     sizeControlImage = uploadImage.scaled(QtGui.QSize(100, 100))
    #
    #     # 이미지를 넣기 위한 파레뜨 생성
    #     palette = QtGui.QPalette()
    #     palette.setBrush(10, QtGui.QBrush(sizeControlImage))  # 10 = 윈도우 동작
    #     # 파레뜨 set
    #     self.setPalette(palette)

        """
        
        start = time.time()
        while ((time.time() - start) == 2):  # 7초간 첫째줄과 셋째줄이 변경됨

        GhostLocation = random.randint(0, 8)  # maindriver랑 합쳐서 귀신이 나타날 장소 구하기
        randomGhost = random.choice(['normalGst', 'normalGst', 'normalGst', 'normalGst', 'starGst', 'starGst',
                       'blindGst'])  # maindriver랑 합쳐서 어떤 귀신이 나타날지 구하기
        """
        #self.setIcon(QtGui.QIcon('ghost.png'))
        #random.randint(10, 20)  # normalGst보다 starGst, blindGst가 나타나는 확률이 더 적었으면 좋겠고, blindGst는 한번 나타나서
        # 그에 대한 벌칙이 끝날때까진 다시 나타나지 않았으면 좋겠음


    """
    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size
    """

import threading
class AsyncTask:  # 이미지는 안 뜨지만, init 해서 오류는 안 남  https://1byte.tistory.com/18 시간 랜덤
    def __init__(self):
        pass

    def TaskA(self):
        threading.Timer(4, self.TaskA).start() # 4초 후
        GhostLocation = GhostWarrior.digitButton[random.randint(0, 8)]  # 귀신이 나타날 장소
        GhostLocation.setIcon(QtGui.QIcon('ghost.png'))  # Button 하나를 골라서 ghost.png 이미지 넣기.. 인데 왜 안되지?

        # https://makersweb.net/python/1098 이건 뭔지 잘 모르겟는데 잘하면 도움될듯


class GhostWarrior(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window 06 - 2 계산기 UI 설정
        self.display = QLineEdit('Timer')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        # self.display.setMaxLength

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addWidget(self.display, 0, 0, 1, 1)
        self.setLayout(mainLayout)
        self.setWindowTitle("Ghost Warrior")
        self.move(500, 500)  # 창 위치 500, 500 픽셀으로

        # Digit Buttons
        self.digitButton = [x for x in range(9)]
        for i in range(9):
            self.digitButton[i] = QToolButton() #--> Button 이어야 하지 않나? 버튼클래스랑 연결해줘야 하니까, 버튼이 QToolButton타입이고.. 근데 버튼이라 하면 QtCore 앞에 self. 붙여줘도 오류뜨고 안 돌아감
            self.digitButton[i].setIconSize(QtCore.QSize(150, 150))  # 버튼 사이즈 150X150

        numLayout = QGridLayout()
        numLayout.addWidget(self.digitButton[0], 0, 0)
        self.digitButton[0].setShortcut("Q")  # key랑 버튼이랑 연결!!
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
        """
        def countdown(t):  # 타이머인데 이거 넣으니까 동작이 안돼.. 왜지? while들어가니까 자꾸 동작 안돼
            while t:
                mins, secs = divmod(t, 60)
                timeformat = '{:02d}:{:02d}'.format(mins, secs)
                # print(timeformat)
                self.display = QLineEdit(timeformat)
                time.sleep(1)
                t -= 1
            self.display = QLineEdit('End!')

        countdown(120)
        """
        # 살려내 살려내 살려내 self.GhostLocation.setIcon(QtGui.QIcon('ghost.png'))

        """
        # 2초동안 임의의 버튼 선택해서 귀신 그림 나타나게 하기
        start = time.time()
        while ((time.time() - start) == 2):  # 2초간
            GhostLocation = self.digitButton[random.randint(0, 8)] # 귀신이 나타날 장소
            GhostLocation.setIcon(QtGui.QIcon('ghost.png')) # Button 하나를 골라서 ghost.png 이미지 넣기.. 인데 왜 안되지?
        """
        """
        randomGhost = random.choice(['normalGst', 'normalGst', 'normalGst', 'normalGst', 'starGst', 'starGst',
                                     'blindGst'])  # maindriver랑 합쳐서 어떤 귀신이 나타날지 구하기
        """

        # self.digitButton[0].setIcon(QtGui.QIcon('ghost.png'))

        mainLayout.addLayout(numLayout, 1, 0)
        """

        class AsyncTask():
            def TaskA(self):
                threading.Timer(4, self.TaskA).start()
                GhostLocation = self.digitButton[random.randint(0, 8)]  # 귀신이 나타날 장소
                GhostLocation.setIcon(QtGui.QIcon('ghost.png'))  # Button 하나를 골라서 ghost.png 이미지 넣기.. 인데 왜 안되지?
        """
        """
        randomGhost = random.choice(['normalGst', 'normalGst', 'normalGst', 'normalGst', 'starGst', 'starGst',
                                     'blindGst'])  # maindriver랑 합쳐서 어떤 귀신이 나타날지 구하기
        """

        # self.initUI()

    # def initUI(self):




if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = GhostWarrior()
    game.show()
    sys.exit(app.exec_())