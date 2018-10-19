# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *


class Window(QWidget):
    def mousePressEvent(self, evt):
        print(self.focusWidget())

        # 聚焦下一个子控件
        # self.focusNextChild()

        # 聚焦上一个子控件
        # self.focusPreviousChild()

        # 上面两个的函数原型
        # True -- Next -- 下一个
        # False -- Prev -- 上一个
        # self.focusNextPrevChild(True)


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = Window()
# 2.2 设置控件
window.setWindowTitle('焦点控制2')
window.resize(500, 500)

le1 = QLineEdit(window)
le1.move(50, 50)

le2 = QLineEdit(window)
le2.move(50, 100)

le3 = QLineEdit(window)
le3.move(50, 150)

# 静态方法
QWidget.setTabOrder(le1, le3)
QWidget.setTabOrder(le3, le2)

# 2.3 展示控件
window.show()

# 获取当前窗口内部，所有子控件当中获取焦点的那个控件
print(window.focusWidget())  # 结果是 None
# 因为在这一行，界面已经展示出来
# 但是焦点还没有被设置，是后来设置的
# 在这一行，所有子控件都没有获取焦点
# 除非实现用 setFocus() 设置

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
