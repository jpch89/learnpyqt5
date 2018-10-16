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
        self.obj = QObject()

        # QObject 里面自带了两个信号
        # obj.destroyed
        # obj.objectNameChanged

        # 测试信号 obj.destroyed
        # def destroy_槽(obj):
        #     print(obj, '对象被释放了')
        #
        # self.obj.destroyed.connect(destroy_槽)
        # del self.obj

        # 测试信号 obj.objectNameChanged
        def objectNameChanged_槽1(name):
            print(name, '对象名称发生了改变【槽1】')
        def objectNameChanged_槽2(name):
            print(name, '对象名称发生了改变【槽2】')
        self.obj.objectNameChanged.connect(objectNameChanged_槽1)
        self.obj.setObjectName('敲敲敲')

        # 测试 disconnect
        self.obj.objectNameChanged.disconnect()
        # 因为取消了连接，虽然 objectNameChanged 信号依然会发射
        # 但是就没有槽函数处理这个信号了
        self.obj.setObjectName('谁谁谁')

        # 测试 blockSignals(self, bool)
        self.obj.objectNameChanged.connect(objectNameChanged_槽1)
        self.obj.blockSignals(True)
        # 不显示是因为 blockSignals(True) 阻断了信号与槽的连接
        self.obj.setObjectName('我我我')
        # blockSignals(False) 恢复连接
        self.obj.blockSignals(False)
        self.obj.setObjectName('你是谁')

        # 测试 signalsBlocked
        print('-' * 50)
        print('信号阻断情况：', self.obj.signalsBlocked())
        self.obj.blockSignals(True)
        print('信号阻断情况：', self.obj.signalsBlocked())

        # 测试 receivers(信号)
        # 返回连接到信号的接收器的数量（即槽函数的数量）
        print('-' * 50)
        self.obj2 = QObject()
        print('连接到 obj2 对象的 objectNameChanged 信号的接收器数量：',
              self.obj2.receivers(self.obj2.objectNameChanged))
        self.obj2.objectNameChanged.connect(objectNameChanged_槽1)
        print('连接到 obj2 对象的 objectNameChanged 信号的接收器数量：',
              self.obj2.receivers(self.obj2.objectNameChanged))
        self.obj2.objectNameChanged.connect(objectNameChanged_槽2)
        print('连接到 obj2 对象的 objectNameChanged 信号的接收器数量：',
              self.obj2.receivers(self.obj2.objectNameChanged))
        # 一个信号可以连接多个槽函数
        self.obj2.setObjectName('马冬梅')


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
