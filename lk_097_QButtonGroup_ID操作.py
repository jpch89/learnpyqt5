# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('ID操作')
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

# 设置是为1，否为2
ans_group.setId(r_yes, 1)
ans_group.setId(r_no, 2)
# 查看 ID
print('是按钮的ID：', ans_group.id(r_yes))
print('否按钮的ID：', ans_group.id(r_no))
# 查看选中的按钮对应的 ID 是多少
# 如果没有选中的按钮，结果为 -1
# 注意：所以千万不要把 ID 设置为 -1 ！！！
print('回答组选中按钮的ID为：', ans_group.checkedId())
# 设置否被选中
r_no.setChecked(True)
print('再次查看回答组选中的按钮ID为：', ans_group.checkedId())

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
