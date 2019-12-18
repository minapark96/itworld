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