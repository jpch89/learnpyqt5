from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QObject的学习')
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        self.QObject对象的父子关系操作()

    def QObject对象的父子关系操作(self):
        obj0 = QObject()
        obj1 = QObject()
        obj2 = QObject()
        obj3 = QObject()
        obj4 = QObject()
        obj5 = QObject()
        print('obj0', obj0)
        print('obj1', obj1)
        print('obj2', obj2)
        print('obj3', obj3)
        print('obj4', obj4)
        print('obj5', obj5)

        # 一个对象只能有一个父对象
        # 后设置的父对象会覆盖先设置的父对象
        obj1.setParent(obj0)
        obj2.setParent(obj0)
        obj2.setObjectName('2')

        # 这两句会报错
        # 因为对于 QLabel 这样一个具体的控件
        # setParent(self, QWidget) 的第二个参数必须也是一个具体的控件
        # 不能是 QObject
        # label = QLabel()
        # label.setParent(obj0)

        obj3.setParent(obj1)
        obj3.setObjectName('3')

        obj4.setParent(obj2)
        obj5.setParent(obj2)

        # print(obj4.parent())

        # children() 方法获取所有直接子对象
        # print(obj0.children())

        # findChild 方法
        # 参数1：控件类型，可以是元组
        # 参数2：控件的对象名称 object name，可以省略
        # 参数3：Qt.FindChildrenRecursively 默认递归查找（即包括所有子对象）
        #       Qt.FindDirectChildrenOnly 只查找直接子对象
        # print(obj0.findChild(QObject, '3', Qt.FindDirectChildrenOnly))

        # findChildren 方法
        # 默认查找所有子对象，返回一个列表
        print(obj0.findChildren(QObject))


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
