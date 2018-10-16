from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QObject的类型判定')
        self.resize(500, 500)
        self.setup_ui()

    def QObject类型判定API(self):
        # 测试 isWidgetType
        # 判定某一个对象是否是控件
        # 即继承自 QWidget 类
        obj = QObject()
        w = QWidget()
        btn = QPushButton()
        label = QLabel()
        objs = [obj, w, btn, label]
        for o in objs:
            print(o.isWidgetType())

        # 测试 inherits('父类')
        # inherits('QWidget') 等价于 isWidgetType()
        print('-' * 50)
        for o in objs:
            print(o.inherits('QWidget'))

    def setup_ui(self):
        self.QObject类型判定API()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
