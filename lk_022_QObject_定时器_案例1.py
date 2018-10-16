# 案例需求：
# 制作倒计时标签

# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *


# 这里可以学到：如何**封装**一个控件
class MyLabel(QLabel):
    def __init__(self, *args, **kwargs):
        # 首先要调用父类的初始化方法
        super().__init__(*args, **kwargs)
        self.setText('10')
        self.move(100, 100)
        self.setStyleSheet('font-size: 100px;')

    def timerEvent(self, *args, **kwargs):
        # 使用 text() 方法获取当前标签的内容
        current_sec = int(self.text())
        current_sec -= 1
        self.setText(str(current_sec))

        if current_sec == 0:
            self.killTimer(self.timer_id)

    def setSec(self, sec):
        self.setText(str(sec))

    def startMyTimer(self, ms):
        self.timer_id = self.startTimer(ms)


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('QObject定时器案例1')
window.resize(500, 500)

# 添加标签
label = MyLabel(window)
label.setSec(5)
label.startMyTimer(1000)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
