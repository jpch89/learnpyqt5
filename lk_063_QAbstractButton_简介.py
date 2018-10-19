# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('QAbstractButton 简介')
window.resize(500, 500)

# 抽象类无法直接被实例化！
# 会报错：
# TypeError: PyQt5.QtWidgets.QAbstractButton represents a C++ abstract class and cannot be instantiated
# 需要进行子类化！
# btn = QAbstractButton(window)


# 子类化抽象类
class Button(QAbstractButton):
    # pass
    # 这样会报错：
    # NotImplementedError: QAbstractButton.paintEvent() is abstract and must be overridden
    # 必须要实现抽象类里面所有的抽象方法
    # 其中很重要的就是 paintEvent() 这个抽象方法

    def paintEvent(self, evt):
        # print('绘制按钮')
        # 绘制按钮上要展示的一个界面内容

        # 画家、笔、纸
        # 要传入一个 QPaintDevice 给 QPainter
        # QPaintDevice 相当于那张纸，在这里就是按钮
        # 注意：所有控件都可以被当成纸
        # 因为所有可视控件都继承自 QWidget
        # 而 QWidget 是多继承的，先继承自 QObject，然后继承自 QPaintDevice
        painter = QPainter(self)

        # 创建笔
        pen = QPen(QColor(111, 200, 20), 5)  # 颜色，粗细
        # 设置笔
        painter.setPen(pen)

        # 画家画画
        # 画笔宽度不适用于文本
        # painter.drawText(20, 20, '画家画画')
        # 获取设置的文本
        painter.drawText(25, 40, self.text())
        painter.drawEllipse(0, 0, 100, 100)


btn = Button(window)
btn.setText('文本内容')
btn.resize(100, 100)

btn.pressed.connect(lambda: print('点击了按钮'))

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
