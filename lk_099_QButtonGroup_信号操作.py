# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('信号操作')
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


# 信号操作
def test(val):
    print(val)
    # 如果不使用 signal_name[type] 格式
    # 可以根据按钮来获取ID
    print('被点击的按钮ID是：', gender_group.id(val))


# 按钮状态改变信号 buttonToggled
# gender_group.buttonToggled.connect(test)

# 按钮点击信号 buttonClicked
gender_group.buttonClicked.connect(test)
# 默认是这样的，跟上面一样，打印了按钮对象
# gender_group.buttonClicked[QAbstractButton].connect(test)
# 让信号发射 ID，而不是 QAbstractButton 对象
# 需要使用 signal_name[type] 格式
# gender_group.buttonClicked[int].connect(test)


# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
