# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
window = QWidget()

# 设置父对象
red = QWidget(window)
red.resize(100, 100)
red.setStyleSheet('background-color: red;')

# 顶层窗口不会自动显示，必须调用 show 方法
# 顶层窗口会被包装一个框架
# 外部框架可以通过窗口标志来设置
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
