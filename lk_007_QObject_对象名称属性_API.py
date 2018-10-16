from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QObject的学习')
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        self.QObject对象名称和属性的操作()

    def QObject对象名称和属性的操作(self):
        # 测试 API
        obj = QObject()
        # 唯一名称
        obj.setObjectName('notice')
        print(obj.objectName())

        obj.setProperty('notice_level', 'error')
        obj.setProperty('notice_level2', 'warning')

        print(obj.property('notice_level'))
        print(obj.property('notice_level2'))

        print(obj.dynamicPropertyNames())


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
