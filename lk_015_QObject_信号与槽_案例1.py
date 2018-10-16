from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QObject信号与槽')
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        self.QObject信号的操作()

    def QObject信号的操作(self):
        btn = QPushButton(self)
        btn.setText('我是按钮！')

        def slot():
            print('点我干啥？')

        btn.clicked.connect(slot)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
