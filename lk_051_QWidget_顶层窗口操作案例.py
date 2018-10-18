# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
# 方法1：在创建的时候设置 flags
# window = QWidget(flags=Qt.FramelessWindowHint)
# 方法2：使用 setWindowFlags()
# 注意：setWindowFlag() 也可以，设置单个标志
window = QWidget()
window.setWindowFlags(Qt.FramelessWindowHint)

# 不透明度设置
window.setWindowOpacity(0.9)

# 2.2 设置控件
window.setWindowTitle('顶层窗口操作案例')
window.resize(500, 500)

# 添加 3 个子控件按钮 - 窗口的右上角
top_margin = 0
btn_w = 40
btn_h = 40

close_btn = QPushButton(window)
close_btn.setText('关闭')
close_btn.resize(btn_w, btn_h)
window_w = window.width()
close_btn_x = window_w - btn_w
close_btn_y = top_margin
close_btn.move(close_btn_x, close_btn_y)

max_btn = QPushButton(window)
max_btn.setText('最大化')
max_btn.resize(btn_w, btn_h)
max_btn_x = close_btn_x - btn_w
max_btn_y = top_margin
max_btn.move(max_btn_x, max_btn_y)

mini_btn = QPushButton(window)
mini_btn.setText('最小化')
mini_btn.resize(btn_w, btn_h)
mini_btn_x = max_btn_x - btn_w
mini_btn_y = top_margin
mini_btn.move(mini_btn_x, mini_btn_y)


def max_normal():
    if window.isMaximized():
        window.showNormal()
        max_btn.setText('最大化')
    else:
        window.showMaximized()
        max_btn.setText('还原')


close_btn.pressed.connect(window.close)
max_btn.pressed.connect(max_normal)
mini_btn.pressed.connect(window.showMinimized)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
