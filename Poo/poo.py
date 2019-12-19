import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QApplication
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QPushButton

class Poo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    # def editCheck(self):
    #     if initUI.lineEdit.isalpha():
    #         continue
    #     else:
    #         errMsg = 'Please write only Alphabet or Hangul'
    #         return errMsg

    def initUI(self):
        friendsList = [QLabel('A'), QLabel('B'), QLabel('C'), QLabel('D'), QLabel('E')]
        editList = [QLineEdit(), QLineEdit(), QLineEdit(), QLineEdit(), QLineEdit()]

        grid = QGridLayout()

        grid.addWidget(friendsList[0], 2, 0)
        grid.addWidget(editList[0], 2, 1)
        grid.addWidget(friendsList[1], 1, 0)
        grid.addWidget(editList[1], 1, 1)
        grid.addWidget(friendsList[2], 0, 2)
        grid.addWidget(editList[2], 0, 3)
        grid.addWidget(friendsList[3], 1, 4)
        grid.addWidget(editList[3], 1, 5)
        grid.addWidget(friendsList[4], 2, 4)
        grid.addWidget(editList[4], 2, 5)
        grid.addWidget(QLabel('me'), 3, 2)

        errMsg = QLabel('문자를 입력해주세요')
        confirm = QPushButton('Confirm')

        hbox1 = QHBoxLayout()
        hbox1.addWidget(errMsg)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(confirm)

        vbox1 = QVBoxLayout()
        vbox1.addLayout(hbox1)
        vbox1.addLayout(hbox2)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(grid)
        mainLayout.addLayout(vbox1)

        self.setGeometry(300, 300, 350, 300)
        self.show()

        """
        friendsList = [QLabel('A'), QLabel('B'), QLabel('C'), QLabel('D'), QLabel('E'), QLabel('me')]
        editList = [QLineEdit(), QLineEdit(), QLineEdit(), QLineEdit(), QLineEdit()]

        errMsg = QLabel('문자를 입력해주세요')
        confirm = QPushButton('Confirm')

        hbox1 = QHBoxLayout() # 가로
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()

        hbox1.addStretch(1)
        hbox2.addStretch(1)
        hbox3.addStretch(1)

        for i in range(5):
            hbox1.addWidget(friendsList[i])

        hbox2.addWidget(errMsg)
        hbox3.addWidget(confirm)

        vbox1 = QVBoxLayout()
        vbox1.addStretch(1)
        vbox1.addLayout(hbox1)
        #vbox1.addWidget(hbox1)

        vbox2 = QVBoxLayout()
        vbox2.addStretch(1)
        vbox2.addLayout(hbox2)
        vbox2.addLayout(hbox3)
        # vbox2.addWidget(hbox2)
        # vbox2.addWidget(hbox3)




        #self.setLayout(vbox)


        # aEdit = QLineEdit()
        # bEdit = QLineEdit()
        # cEdit = QLineEdit()
        # dEdit = QLineEdit()
        # eEdit = QLineEdit()
        # errorMsg = QLineEdit()

        grid = QGridLayout()
        #grid.setSpacing(30)

        grid.addWidget(friendsList[0], 2, 0)
        grid.addWidget(editList[0], 2, 1)

        grid.addWidget(friendsList[1], 1, 0)
        grid.addWidget(editList[1], 1, 1)

        grid.addWidget(friendsList[2], 0, 2)
        grid.addWidget(editList[2], 0, 3)

        grid.addWidget(friendsList[3], 1, 4)
        grid.addWidget(editList[3], 1, 5)

        grid.addWidget(friendsList[4], 2, 4)
        grid.addWidget(editList[4], 2, 5)

        grid.addWidget(friendsList[5], 3, 2)

        #grid.addWidget(confirm, 4, 0)

        self.setLayout(grid)


        self.setGeometry(300, 300, 350, 300)
        self.show()
        """

if __name__ == '__main__':
    app = QApplication(sys.argv)
    poo = Poo()
    sys.exit(app.exec_())