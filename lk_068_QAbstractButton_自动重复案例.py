# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('自动重复')
window.resize(500, 500)


def plus_one():
    print('加一')
    num = int(btn.text()) + 1
    btn.setText(str(num))


btn = QPushButton(window)
btn.setText('1')
icon = QIcon('img/Python.png')
btn.setIcon(icon)
size = QSize(100, 100)
btn.setIconSize(size)
# btn.clicked.connect(lambda: print('按钮被点击了！'))
btn.clicked.connect(plus_one)

# 获取自动重复
print('当前是否自动重复：', btn.autoRepeat())
# 设置自动重复
btn.setAutoRepeat(True)
# 获取重复延迟
print('当前重复延迟：', btn.autoRepeatDelay())  # 300 豪秒延迟
# 设置重复延迟为 2000 ms
btn.setAutoRepeatDelay(2000)
# 获取重复间隔
print('当前重复间隔：', btn.autoRepeatInterval())  # 100 豪秒间隔
# 设置重复间隔为 1000 ms
btn.setAutoRepeatInterval(1000)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
