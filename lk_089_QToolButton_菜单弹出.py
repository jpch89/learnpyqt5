# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('菜单弹出')
window.resize(500, 500)

tb = QToolButton(window)
tb.setText('工具')
tb.setArrowType(Qt.RightArrow)
tb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

# 创建菜单
menu = QMenu(tb)
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
# setMenu 是 QToolButton 类的方法
tb.setMenu(menu)

# 设置菜单弹出方式
# 默认是延迟弹出：QToolButton.DelayedPopup
# 菜单按钮弹出：点击右侧向下的箭头才可以弹出菜单
# tb.setPopupMode(QToolButton.MenuButtonPopup)
# 立即弹出：点击整体按钮弹出菜单
tb.setPopupMode(QToolButton.InstantPopup)

# 默认延迟弹出（QToolButton.DelayedPopup）时，长按点击再松开不会发送 clicked 信号
# 菜单按钮弹出（QToolButton.MenuButtonPopup）时，点击左侧发送信号，点击右侧向下箭头不发射
# 立即弹出（QToolButton.InstantPopup）时，不管怎么点都不会发射 clicked 信号
tb.clicked.connect(lambda: print('工具按钮被点击了'))

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
