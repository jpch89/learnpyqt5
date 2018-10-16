# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *


class MyObject(QObject):
    def timerEvent(self, evt):
        print(evt, '我是定时器事件')


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('QObject定时器的使用')
window.resize(500, 500)

obj = MyObject()
# startTimer 开启定时器
# 传入毫秒整数和 TimerType
# 接收 timer_id
timer_id = obj.startTimer(1000)

# killTimer 关闭定时器
# 注意要传入定时器 id
# 因为有可能有多个定时器，所以要进行区分
obj.killTimer(timer_id)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
