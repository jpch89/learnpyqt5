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

w2 = QWidget()
w2.setWindowTitle('窗口2')

# 2.3 展示控件
window.show()
w2.show()

print('窗口1是否活跃：', window.isActiveWindow())
# 后展示的是活跃窗口！
print('窗口2是否活跃：', w2.isActiveWindow())
# 窗口是否活跃跟z轴层级没有关系
window.raise_()
print('窗口1是否活跃：', window.isActiveWindow())


# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
