from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QObject的学习')
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        self.Qt内存管理机制()

    def Qt内存管理机制(self):
        # obj1 在本方法被调用完毕后会被自动释放
        obj1 = QObject()
        # 但是如果加了这一句
        # 本方法执行完毕之后，仍然有指针指向 obj1
        # 所以 obj1 不会被释放
        self.obj1 = obj1
        obj2 = QObject()

        obj2.setParent(obj1)

        # 监听 obj2 对象被释放
        obj2.destroyed.connect(lambda: print('obj2 对象被释放了'))

        del self.obj1


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
