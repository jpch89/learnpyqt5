from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QObject的学习')
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        self.QObject继承结构测试()

    def QObject继承结构测试(self):
        # 打印所有子类
        # print(QObject.__subclasses__())
        # 打印所有父类
        mros = QObject.mro()
        for mro in mros:
            print(mro)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
