import sys
from PyQt5.Qt import *


class MyWindow(QWidget):
    def mouseMoveEvent(self, mv):
        print('鼠标移动：', mv.localPos())
        # 这一句也可以不用
        label = self.findChild(QLabel)
        label.move(mv.localPos().x(), mv.localPos().y())


app = QApplication(sys.argv)

window = MyWindow()
window.setWindowTitle('鼠标操作案例')
window.resize(500, 500)

# 设置鼠标跟踪
window.setMouseTracking(True)
# 自定义鼠标
pixmap = QPixmap('img/cursor.png').scaled(50, 50)
cursor = QCursor(pixmap, 0, 0)
window.setCursor(cursor)

label = QLabel(window)
label.setText('枯藤老树昏鸦')
label.move(100, 100)
label.setStyleSheet('background-color: cyan; font-size: 30px;')



window.show()

sys.exit(app.exec_())
