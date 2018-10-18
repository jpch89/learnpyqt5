from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('窗口移动案例')
        self.resize(500, 500)
        self.setup_ui()
        self.move_flag = False

    def setup_ui(self):
        pass

    def mousePressEvent(self, evt):
        # 只让鼠标左键点击的时候移动
        if evt.button() == Qt.LeftButton:
            self.move_flag = True
        # print('鼠标按下！')
        # 确定两个点
        # 1) 鼠标第一次按下的点
        self.mouse_x = evt.globalX()
        self.mouse_y = evt.globalY()
        # 2) 窗口当前所在的原始点
        self.origin_x = self.x()
        self.origin_y = self.y()

    def mouseMoveEvent(self, evt):
        # print('鼠标移动！')
        if self.move_flag:
            # 每次移动，都能获取最新的 globalX 和 globalY
            self.move_x = evt.globalX() - self.mouse_x
            self.move_y = evt.globalY() - self.mouse_y
            self.dest_x = self.move_x + self.origin_x
            self.dest_y = self.move_y + self.origin_y
            self.move(self.dest_x, self.dest_y)

    def mouseReleaseEvent(self, evt):
        # print('鼠标释放！')
        # 在这里移动就不会实时移动了！
        # self.move(self.origin_x + self.move_x, self.origin_y + self.move_y)

        self.move_flag = False


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()
    # 这样程序就崩了！
    # 因为直接就进入了 mouseMoveEvent
    # 而没有经过 mousePressEvent
    # 所以要在 mousePressEvent 里面加入 self.move_flag 标记
    window.setMouseTracking(True)
    sys.exit(app.exec_())
