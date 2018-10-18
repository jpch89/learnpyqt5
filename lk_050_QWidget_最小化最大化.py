# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *


# 需求：一旦点击窗口，就最大化
class Window(QWidget):
    def mousePressEvent(self, evt):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = Window()
# 2.2 设置控件
window.setWindowTitle('最小化最大化')
window.resize(500, 500)

# showMaximized() 最大化
# 注意：这样就不用 show() 展示了
# window.showMaximized()

# showFullScreen() 全屏
# window.showFullScreen()

# showMinimized() 最小化
# window.showMinimized()

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
