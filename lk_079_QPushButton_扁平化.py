# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('扁平化')
window.resize(500, 500)

button = QPushButton(window)
button.setText('按钮')
button.move(200, 200)
print('当前按钮是否扁平：', button.isFlat())
# 设置为扁平化
button.setFlat(True)
print('当前按钮是否扁平：', button.isFlat())
# 不点击按钮的话，设置背景颜色会没有
button.setStyleSheet('background-color: red')

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
