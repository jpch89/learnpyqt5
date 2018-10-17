import sys
from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('鼠标操作案例')
        self.resize(500, 500)
        # 设置鼠标跟踪
        self.setMouseTracking(True)
        # 自定义鼠标
        pixmap = QPixmap('img/cursor.png').scaled(50, 50)
        cursor = QCursor(pixmap, 0, 0)
        self.setCursor(cursor)
        self.label = QLabel(self)
        self.label.setText('枯藤老树昏鸦')
        self.label.move(100, 100)
        self.label.setStyleSheet('background-color: cyan; font-size: 30px;')

    def mouseMoveEvent(self, mv):
        print('鼠标移动：', mv.localPos())
        self.label.move(mv.localPos().x(), mv.localPos().y())


app = QApplication(sys.argv)

window = MyWindow()
window.show()

sys.exit(app.exec_())
