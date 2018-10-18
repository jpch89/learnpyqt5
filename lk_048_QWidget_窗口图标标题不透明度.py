# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.resize(500, 500)

# 设置窗口图标
icon = QIcon('img/Python.png')
window.setWindowIcon(icon)
# 获取窗口图标
print(window.windowIcon())

# 设置窗口标题
# 如果不写，则默认为 python
# 如果写的是空字符串，也是默认 python
# 设置为空格，相当于清空了标题
window.setWindowTitle('窗口相关操作')
# 获取窗口标题
print(window.windowTitle())

# 设置窗口不透明度
# 浮点类型的数据，0.0 到 1.0
# 1.0 不透明
# 0.0 透明
window.setWindowOpacity(0.9)
# 获取不透明度
# 大概是 0.9，处理的时候有点偏差
print(window.windowOpacity())

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
