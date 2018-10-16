from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QObject类型判定-案例')
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        label1 = QLabel(self)
        label1.setText('我是标签1')
        label2 = QLabel(self)
        label2.setText('我是标签2')
        label2.move(50, 50)
        btn = QPushButton(self)
        btn.setText('点我！')
        btn.move(100, 100)

        # 要求：
        # 给所有的标签设置背景颜色为 cyan
        # 知识点：
        # 通过类型判定来实现控件过滤

        # 方法1：用 findChildren 选中所有标签，然后遍历
        # for widget in self.findChildren(QLabel):
        #     print(widget)

        # 方法2：借助类型判定中的 inherits('父类')
        for widget in self.children():
            if widget.inherits('QLabel'):
                widget.setStyleSheet('background-color: cyan;')


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
