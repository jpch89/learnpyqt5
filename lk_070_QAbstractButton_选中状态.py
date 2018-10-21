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

# 查看是否可以被选中
print('QPushButton是否可以被选中：', push_button.isCheckable())
print('QRadioButton是否可以被选中：', radio_button.isCheckable())
print('QCheckBox是否可以被选中：', check_box.isCheckable())

# 设置 QPushButton 可以被选中
push_button.setCheckable(True)
print('-' * 50)
print('再次查看QPushButton是否可以被选中：', push_button.isCheckable())

# 设置按钮为选中状态
push_button.setChecked(True)
radio_button.setChecked(True)
check_box.setChecked(True)

# 查看三个按钮的选中状态
print('-' * 50)
print('QPushButton当前选中状态：', push_button.isChecked())
print('QRadioButton当前选中状态：', radio_button.isChecked())
print('QCheckBox当前选中状态：', check_box.isChecked())


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
