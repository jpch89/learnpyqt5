# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('菜单的设置')
window.resize(500, 500)

# 创建按钮
btn = QPushButton(QIcon('img/Python.png'), '菜单', window)

# 创建菜单
menu = QMenu()

# 子菜单：最近打开
open_recent_menu = QMenu()
open_recent_menu.setTitle('最近打开')
# 也可以设置图标：setIcon
# 一次性设置：QMenu('标题', 父控件)
# 添加到父菜单，它不会自动添加
# open_recent_menu = QMenu(父控件) 这样不可以

# 子菜单中的行为
file_action = QAction('Python-GUI编程-PyQt5')
# 添加行为
open_recent_menu.addAction(file_action)

# 行为动作（命令）：新建，打开，分割线，退出
# 新建
new_action = QAction()
new_action.setText('新建')
new_action.setIcon(QIcon('img/新建.png'))
new_action.triggered.connect(lambda: print('新建文件'))

# 打开
# QAction的四种构造函数
# QAction()
# QAction(父对象)
# QAction(文本, 父对象)
# QAction(图标, 文本, 父对象)
# 注意：父对象写了，还是要使用 addAction！
open_action = QAction(QIcon('img/打开.png'), '打开', menu)
open_action.triggered.connect(lambda: print('打开文件'))

# 退出
exit_action = QAction(QIcon('img/退出.png'), '退出', menu)
exit_action.triggered.connect(lambda: print('退出程序'))

# 添加动作
menu.addAction(new_action)
menu.addAction(open_action)
# 添加子菜单
menu.addMenu(open_recent_menu)
# 添加分割线
menu.addSeparator()
menu.addAction(exit_action)

# 给按钮设置菜单
# 设置菜单之后，按钮右边会出现下拉菜单的箭头
btn.setMenu(menu)

# 在这里展示菜单的话会跑到左上角
# 因为整个窗口还没有展示，都不知道按钮被放在那里
# 而且 QMenu 继承于 QWidget，自己是可以独立存在的
# 所以展示菜单需要放到 window.show() 的后面
# btn.showMenu()

# 获取菜单，是一个 QMenu 对象
print(btn.menu())

# 2.3 展示控件
window.show()
# 展示菜单
btn.showMenu()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
