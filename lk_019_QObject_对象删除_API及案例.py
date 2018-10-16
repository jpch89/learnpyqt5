from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QObject对象删除')
        self.resize(500, 500)
        self.setup_ui()

    def QObject_对象删除(self):
        obj1 = QObject()
        self.obj1 = obj1
        obj2 = QObject()
        obj3 = QObject()
        obj3.setParent(obj2)
        obj2.setParent(obj1)

        obj1.destroyed.connect(lambda: print('obj1被释放了'))
        obj2.destroyed.connect(lambda: print('obj2被释放了'))
        obj3.destroyed.connect(lambda: print('obj3被释放了'))

        # del obj2
        # 这样无法删除 obj2
        # 因为只是解除了 obj2 名字与内存中对象的连接
        # 并没有解除 obj2 的父子对象关系
        # 所以此时 obj2 还是被引用着（它是 obj1 的子对象）

        # 执行完毕消息循环再删除 obj2
        # 这样可以防止后续使用到该对象的时候报错
        obj2.deleteLater()
        print('obj2：', obj2)
        print('obj1 children：', obj1.children())

    def setup_ui(self):
        self.QObject_对象删除()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
