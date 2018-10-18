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
# button.pressed.connect(lambda: print('点击了按钮！'))
# button.pressed.connect(lambda: button.hide())
button.pressed.connect(lambda: button.setVisible(False))
# 隐藏按钮
# button.setVisible(False)

# 2.3 展示控件
# 不写这一句，就不会调用 paintEvent
# window.show()
# 最根本的方法就是 setVisible，其他都是马甲
# window.setVisible(True)
# 不隐藏就是显示
window.setHidden(False)

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
