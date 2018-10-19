# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('图标设置')
window.resize(500, 500)

btn = QPushButton(window)
# 假如有文本，默认在文本左侧显示图标
# 即先图标，再文本
icon = QIcon('img/Python.png')
btn.setIcon(icon)
size = QSize(100, 100)
btn.setIconSize(size)
# 获取图标对象
print(btn.icon())
# 获取图标大小
print(btn.iconSize())

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
