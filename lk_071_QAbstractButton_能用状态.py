# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('能用状态')
window.resize(500, 500)

btn = QPushButton(window)
btn.setIcon(QIcon('img/Python.png'))
btn.setIconSize(QSize(80, 80))

push_button = QPushButton(window)
push_button.setText('QPushButton')
push_button.move(100, 100)

radio_button = QRadioButton(window)
radio_button.setText('QRadioButton')
radio_button.move(100, 150)

check_box = QCheckBox(window)
check_box.setText('QCheckBox')
check_box.move(100, 200)

# 注意 setEnabled 是从 QWidget 继承而来的方法
# 而不是 QAbstractButton 的方法
# 虽然控件不可用，但还是可以通过代码来更改它们的状态
# 注意：QPushButton可能看不出来状态的变化
# 是因为它的不可用状态有一个特定样式，造成我们看不出由于状态更改而带来的样式区别
push_button.setEnabled(False)
radio_button.setEnabled(False)
check_box.setEnabled(False)


# 使用 toggle() 切换选中状态
def slot():
    push_button.toggle()
    radio_button.toggle()
    check_box.toggle()

    # 另外一种写法：
    # push_button.setChecked(not push_button.isChecked())
    # radio_button.setChecked(not radio_button.isChecked())
    # check_box.setChecked(not check_box.isChecked())


btn.pressed.connect(slot)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
