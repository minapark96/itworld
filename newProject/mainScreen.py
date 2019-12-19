from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout

from last import Thread

class MainDriver(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Socrates Test')


        nextButton = QPushButton("Next")
        hbox = QHBoxLayout()
        hbox.addWidget(nextButton)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        # nextButton 이 클릭 되지 않았을 때 if nextButton.
        # qsRadio 클래스의 1번째 화면으로 연결한다.
        # 클릭되었으면 2번째 화면 >>> 10번째 화면 >>>

    def nextFunc(self):
        questionNum = 0
        if self.nextButton.clicked():
            questionNum += 1

            self.nextButton.clicked(QuestionClass.addScore) # 라디오버튼 별 점수 더하기
            self.nextButton.clicked(QuestionClass.nextQ) # 버튼 눌리면 질문 다음 걸로 보여주기
            self.nextButton.clicked(RadioClass.nextRadio) # 다음 라디오버튼

        if questionNum == 5:
            resultScreen()

    def resultScreen(self):
        self.setWindowTitle('Socrates Test Result')
        sumLabelShow = QLabel()


