# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('窗口1')
window.resize(500, 500)

# windowState() 获取窗口状态
# 默认无状态 Qt.WindowNoState
print(window.windowState() == Qt.WindowNoState)

# setWindowState 设置窗口状态
# 最小化
# window.setWindowState(Qt.WindowMinimized)
# 最大化
# window.setWindowState(Qt.WindowMaximized)
# 全屏
# window.setWindowState(Qt.WindowFullScreen)

window2 = QWidget()
window2.setWindowTitle('窗口2')

# 2.3 展示控件
# 谁后显示，谁离我们更近！
window.show()
window2.show()
# 或者控制窗口活跃状态
# setWindowState(Qt.WindowActive)
window.setWindowState(Qt.WindowActive)

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
