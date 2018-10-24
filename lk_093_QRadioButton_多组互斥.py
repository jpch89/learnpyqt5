# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('多组互斥')
window.resize(500, 500)

# 多组互斥解决方案1：放在两个父控件里面
red = QWidget(window)
red.resize(200, 200)
red.setStyleSheet('background-color: red;')
red.move(50, 50)

green = QWidget(window)
green.resize(200, 200)
green.setStyleSheet('background-color: green;')
green.move(250, 50)

rb_male = QRadioButton('男-&Male', red)
rb_male.move(20, 20)
rb_male.setIcon(QIcon('img/male.png'))
rb_male.setIconSize(QSize(40, 40))
rb_male.setChecked(True)

rb_female = QRadioButton('女-Female', red)
rb_female.move(20, 120)
rb_female.setIcon(QIcon('img/female.png'))
rb_female.setIconSize(QSize(40, 40))
rb_female.setShortcut('Alt+F')

rb_yes = QRadioButton('yes', green)
rb_yes.move(20, 30)

rb_no = QRadioButton('no', green)
rb_no.move(20, 130)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
