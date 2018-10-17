# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('重置和获取鼠标')
window.resize(500, 500)

window.setCursor(Qt.BusyCursor)
# 重置鼠标 unsetCursor
window.unsetCursor()
# 获取鼠标 cursor，返回 QCursor 对象
# print(window.cursor())
current_cursor = window.cursor()
# pos() 是相对于整个电脑屏幕的位置
print(current_cursor.pos())
# setPos() 设置位置
current_cursor.setPos(0, 0)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
