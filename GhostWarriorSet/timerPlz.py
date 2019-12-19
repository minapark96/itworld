import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QProgressBar

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal

class Thread(QThread):

    change_value = pyqtSignal(int)

    def __init__(self):
        QThread.__init__(self)
        self.cnt = 100

    def __del__(self):
        self.wait()

    def run(self):
        while True:

            if 0 == self.cnt:
                break

            self.cnt -= 1
            self.change_value.emit(self.cnt)
            self.msleep(10)

        # 100 x 10 msecs = 1 secs count


class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.pgsb = QProgressBar()
        self.th = Thread()

        self.pgsb.setFormat("")
        self.init_widget()
        self.th.start()

    def init_widget(self):
        self.setWindowTitle("Timer")
        form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
        self.setLayout(form_lbx)

        self.th.change_value.connect(self.pgsb.setValue)
        form_lbx.addWidget(self.pgsb)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())