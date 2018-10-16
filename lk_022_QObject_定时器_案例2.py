# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *


class MyWindow(QWidget):
    def timerEvent(self, *args, **kwargs):
        current_w = self.width()
        current_h = self.height()
        self.resize(current_w + 1, current_h + 1)


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = MyWindow()
# 2.2 设置控件
window.setWindowTitle('QObject定时器案例2')
window.resize(500, 500)
window.startTimer(100)
# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
