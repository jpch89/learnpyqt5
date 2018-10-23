# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('模拟点击')
window.resize(500, 500)

btn = QPushButton(window)
btn.setText('按钮1')
btn.move(200, 200)
btn.pressed.connect(lambda: print('按钮1被点击了！'))

# 模拟点击
# btn.click()

# 模拟动画点击 animateClick(ms)
# btn.animateClick(2000)

btn2 = QPushButton(window)
btn2.setText('按钮2')


def test():
    # 模拟点击
    # btn.click()
    # 动画点击
    btn.animateClick(1000)


btn2.pressed.connect(test)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
