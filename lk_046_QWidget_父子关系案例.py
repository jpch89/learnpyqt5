# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *


# 方案1：自定义 QLabel
# 这个方法的弊端：
# 一开始有很多标签并没有使用自定义的 Label 创建
# 后期要全部改过来比较复杂
# class Label(QLabel):
#     def mousePressEvent(self, evt):
#         self.setStyleSheet('background-color: red;')


# 方案2：自定义 QWidget 父控件
# 如果 QLabel 的点击事件没有被处理
# 则会传递到父控件
class Window(QWidget):
    def mousePressEvent(self, evt):
        # 这里要取局部坐标，因为 childAt 使用的就是相对于窗口的坐标
        local_x = evt.x()
        local_y = evt.y()
        sub_widget = self.childAt(local_x, local_y)
        # 如果不加判定，会崩溃
        # 因为假如没有获取到子控件（比如点击窗口空白部分）
        # 那么就是一个 None
        # 对 None 使用 setStyleSheet 显然是不行的
        # if sub_widget:
        if sub_widget is not None:
            sub_widget.setStyleSheet('background-color: red;')


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = Window()
# 2.2 设置控件
window.setWindowTitle('父子关系案例')
window.resize(500, 500)

for i in range(10):
    label = QLabel(window)
    label.setText('标签' + str(i + 1))
    label.move((i + 1) * 40, (i + 1) * 40)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
