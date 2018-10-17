# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *


class MyWindow(QWidget):
    # 参数类型是 QMouseEvent
    def mouseMoveEvent(self, me):
        # QMouseEvent 对象
        # 可以获取到是鼠标左键、右键、还是多个键被点击
        # globalPos：鼠标相对整个电脑屏幕左上角的位置
        print('globalPos：', me.globalPos())
        # globalX
        # globalY
        # localPos：鼠标相对于父控件左上角的位置（不包括窗体框架）
        print('localPos：', me.localPos())
        print('鼠标移动了')


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = MyWindow()
# 2.2 设置控件
window.setWindowTitle('鼠标跟踪')
window.resize(500, 500)
# hasMouseTracking 查看鼠标跟踪状态
print('鼠标跟踪：', window.hasMouseTracking())
# setMouseTracking(bool) 设置鼠标跟踪
window.setMouseTracking(True)
print('鼠标跟踪：', window.hasMouseTracking())

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
