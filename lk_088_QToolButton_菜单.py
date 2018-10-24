# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('工具按钮的菜单')
window.resize(500, 500)

btn = QPushButton(window)
btn.setText('一般按钮')
btn.move(100, 100)

# 创建菜单
menu = QMenu(btn)
# 添加子菜单
sub_menu = QMenu(menu)
sub_menu.setTitle('新建')
sub_menu.setIcon(QIcon('img/新建.png'))
menu.addMenu(sub_menu)
# 添加分割线
menu.addSeparator()
# 添加行为
action = QAction(QIcon('img/打开.png'), '打开', menu)
menu.addAction(action)
action.triggered.connect(lambda: print('点击了打开！'))

# 设置菜单
btn.setMenu(menu)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
