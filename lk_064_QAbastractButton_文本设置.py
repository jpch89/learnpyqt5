# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('文本设置')
window.resize(500, 500)

btn = QPushButton(window)
# 不设置文本的话是一个空白的小方块
btn.setText('1')


def plus_one():
    print('加一')
    num = int(btn.text()) + 1
    btn.setText(str(num))


btn.pressed.connect(plus_one)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
