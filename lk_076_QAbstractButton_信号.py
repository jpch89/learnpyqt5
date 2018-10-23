# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('信号')
window.resize(500, 500)

btn = QPushButton(window)
btn.move(100, 100)
btn.setText('按钮')

btn.pressed.connect(lambda: print('按钮被按下了'))

# released 信号何时发射：
# 1. 控件内松开鼠标
# 2. 鼠标移出控件范围后松开
btn.released.connect(lambda: print('按钮被释放了'))

# clicked 信号何时发射：
# 鼠标在按钮有效区域按下并松开，才会发射
# 如果移出来了之后再松开，是不会发射这个信号的
# btn.clicked.connect(lambda: print('按钮被点击了'))
# 接收传过来的值，并打印
btn.clicked.connect(lambda value: print('按钮被点击了', value))
# 该值为 False，代表该按钮点击之后，是否处于被选中的状态
# 现在设置按钮为可以被选中
btn.setCheckable(True)

# toggled：选中状态发生改变时发射的信号
# 得到的值是当前按钮的选中状态
btn.toggled.connect(lambda value: print('按钮选中状态发生了改变', value))
# 假如按钮不可选中，那么该信号不会被触发
# btn.setCheckable(False)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
