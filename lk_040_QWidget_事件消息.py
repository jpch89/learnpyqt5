from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('事件消息的学习')
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        pass

    def showEvent(self, QShowEvent):
        print('窗口被展示了！')

    def closeEvent(self, QCloseEvent):
        print('窗口被关闭了！')

    def moveEvent(self, QMoveEvent):
        print('窗口被移动了！')

    def resizeEvent(self, QResizeEvent):
        print('窗口大小被调整了！')

    def enterEvent(self, QEvent):
        print('鼠标进来了！')
        self.setStyleSheet('background-color: yellow;')

    def leaveEvent(self, QEvent):
        print('鼠标离开了！')
        self.setStyleSheet('background-color: green;')

    def mousePressEvent(self, QMouseEvent):
        # 可以通过 QMouseEvent 这个事件对象获取到底是左键还是右键被点击
        print('鼠标被按下了！')

    def mouseReleaseEvent(self, QMouseEvent):
        print('鼠标被释放了！')

    def mouseDoubleClickEvent(self, QMouseEvent):
        print('鼠标双击！')

    def mouseMoveEvent(self, QMouseEvent):
        # 必须要按下鼠标左键或者右键才会响应
        # 如果在不按键的时候追踪鼠标
        # 需要设置
        # self.setMouseTracking(True)
        print('鼠标被移动了！')

    # 单击信号：必须是在控件范围内被按下，在控件范围内被释放才算

    def keyPressEvent(self, QKeyEvent):
        # 在 QKeyEvent 这个事件对象可以找到具体是哪个键被按下了
        print('键盘被按下！')

    def keyReleaseEvent(self, QKeyEvent):
        print('键盘被释放！')


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
