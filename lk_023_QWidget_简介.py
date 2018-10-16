# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
window = QWidget()
window.setWindowTitle('QWidget简介')
window.resize(500, 500)

# 控件由其父控件裁剪
red = QWidget(window)
red.resize(100, 100)
red.setStyleSheet('background-color: red;')
red.move(450, 0)

# 控件被它前面的控件裁剪
green = QWidget(window)
green.resize(100, 100)
green.setStyleSheet('background-color: green;')
green.move(450, 50)

window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
