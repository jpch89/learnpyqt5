# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *


class Label(QLabel):
    def enterEvent(self, *args, **kwargs):
        self.setText('欢迎光临！')
        print('鼠标进入')

    def leaveEvent(self, *args, **kwargs):
        self.setText('谢谢惠顾！')
        print('鼠标离开')


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('鼠标操作案例1')
window.resize(500, 500)

label = Label(window)
label.resize(200, 200)
label.move(100, 100)
label.setStyleSheet('background-color: cyan;')


# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
