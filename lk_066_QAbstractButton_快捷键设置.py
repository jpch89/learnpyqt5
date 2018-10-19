# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('快捷键设置')
window.resize(500, 500)

btn = QPushButton(window)

# 设置快捷键
# 方式1：有提示文本
# btn.setText('&button')  # Alt - b 触发
# 带中文可以这么写
# btn.setText('按钮(&b)')

# 方式2：setShortcut 直接设置快捷方式
# 适用于整个按钮只展示图标，没有任何文本
btn.setShortcut('Alt+b')


def slot():
    print('按钮被点击了！')


btn.clicked.connect(slot)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
