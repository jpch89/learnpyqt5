# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *


# 需求：点谁谁上来
# 方法1：自定义标签控件，检测鼠标点击事件
# class Label(QLabel):
#     def mousePressEvent(self, evt):
#         self.raise_()


# 方法2：父控件查找子控件的方式
class Window(QWidget):
    def mousePressEvent(self, evt):
        widget = self.childAt(evt.x(), evt.y())
        if widget is not None:
            widget.raise_()


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = Window()
# 2.2 设置控件
window.setWindowTitle('层级关系调整')
window.resize(500, 500)

label1 = QLabel(window)
label1.setText('标签1')
label1.resize(200, 200)
label1.setStyleSheet('background-color: red;')

# 默认情况，后添加的在上面
label2 = QLabel(window)
label2.setText('标签2')
label2.resize(200, 200)
label2.setStyleSheet('background-color: green;')
label2.move(100, 100)

# 想让红色的 label1 在上面
# 方法1：使用 lower
# label2.lower()

# 方法2：使用 raise_
# label1.raise_()

# 方法3：使用 a.stackUnder(b)
# label2.stackUnder(label1)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
