# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('状态设置')
window.resize(500, 500)

push_button = QPushButton(window)
push_button.setText('QPushButton')
push_button.move(100, 100)

radio_button = QRadioButton(window)
radio_button.setText('QRadioButton')
radio_button.move(100, 150)

check_box = QCheckBox(window)
check_box.setText('QCheckBox')
check_box.move(100, 200)

# 把三个按钮，都设置为按下状态
push_button.setDown(True)
radio_button.setDown(True)
check_box.setDown(True)

# 通过 qss 设定按下状态的样式
# 注意：我之前写的这一句无法设置背景为红色，多了一个空格
# push_button.setStyleSheet('QPushButton: pressed {background-color: red;}')
push_button.setStyleSheet('QPushButton:pressed {background-color: red;}')

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
