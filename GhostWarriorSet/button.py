from PyQt5.QtWidgets import QToolButton

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