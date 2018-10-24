# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('移除按钮')
window.resize(500, 500)

# 创建4个单选按钮
# 分别是男、女和是、否
r_male = QRadioButton('男', window)
r_male.move(100, 100)
# 默认选中男
r_male.setChecked(True)
r_female = QRadioButton('女', window)
r_female.move(100, 150)
r_yes = QRadioButton('是', window)
r_yes.move(300, 100)
r_no = QRadioButton('否', window)
r_no.move(300, 150)

# 创建按钮组 QButtonGroup
gender_group = QButtonGroup(window)  # 父对象 window 销毁的时候，子对象也会被销毁
# 添加按钮，并传入 ID
gender_group.addButton(r_male, 1)
gender_group.addButton(r_female, 2)

ans_group = QButtonGroup(window)
ans_group.addButton(r_yes)
ans_group.addButton(r_no)

# 移除女按钮
# 此时女只有一个父控件，没有组
gender_group.removeButton(r_female)
# 查看组内按钮
print('组内成员：', gender_group.buttons())
# 按ID为2查看按钮
print('ID为2的按钮：', gender_group.button(2))

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
