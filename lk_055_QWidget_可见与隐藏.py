# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *


class Window(QWidget):
    def paintEvent(self, evt):
        print('窗口被绘制了')
        return super().paintEvent(evt)


class Button(QPushButton):
    def paintEvent(self, evt):
        print('按钮被绘制了')
        return super().paintEvent(evt)


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = Window()
# 2.2 设置控件
window.setWindowTitle('绘制事件监听')
window.resize(500, 500)

button = Button(window)
button.setText('按钮')
button.pressed.connect(lambda: button.setVisible(False))

# 2.3 展示控件
window.show()  # 注释掉这一句：按钮最终不可见，但是按钮相对于父控件没有被隐藏
print('按钮是否隐藏：', button.isHidden())
print('按钮是否可见：', button.isVisible())

# 父控件 **如果** 显示的时候，子控件是否跟着一起显示
print('按钮相对于窗口是否可见：', button.isVisibleTo(window))

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
