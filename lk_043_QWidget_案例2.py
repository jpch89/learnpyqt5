# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *


class Label(QLabel):
    def keyPressEvent(self, evt):
        if evt.key() == Qt.Key_Tab:
            print('用户点击了 Tab 键！')
            self.setText('监听到 Tab 键')
        # 修饰键为 Ctrl，普通键为 S
        if evt.modifiers() == Qt.ControlModifier and evt.key() == Qt.Key_S:
            print('用户点击了 Ctrl - S 组合键！')
            self.setText('监听到 Ctrl - S 组合键！')
        # Ctrl - Shift - A
        # 多个修饰键使用按位或！
        # 前面 modifiers() 返回了 8421 码，比如 5, 7, 3 等等
        # 后面的按位或运算的组合键可以求出 8421 码
        # 3 == 2 | 1
        # 10 ---- 2
        # 01 ---- 1
        # 11 ---- 3
        if evt.modifiers() == Qt.ControlModifier | Qt.ShiftModifier and evt.key() == Qt.Key_A:
            print('用户点击了 Ctrl - Shift - A 组合键！')
            self.setText('监听到 Ctrl - Shift - A 组合键！')


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('键盘操作案例')
window.resize(500, 500)

label = Label(window)
label.resize(400, 200)
label.move(50, 100)
label.setStyleSheet('background-color: cyan; font-size: 20px;')
# 让标签捕获键盘
label.grabKeyboard()

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
