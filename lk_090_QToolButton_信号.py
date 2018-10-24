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
open_action = QAction(QIcon('img/打开.png'), '打开', menu)
menu.addAction(open_action)
open_action.triggered.connect(lambda: print('点击了打开！'))
# 设置数据
open_action.setData([1, 2, 3])

# 再添加一个行为
exit_action = QAction(QIcon('img/退出.png'), '退出', menu)
menu.addAction(exit_action)
# 设置数据
exit_action.setData({'name': '进击的团子'})

# 设置菜单
# setMenu 是 QToolButton 类的方法
tb.setMenu(menu)

# 设置菜单弹出方式
# 默认是延迟弹出：QToolButton.DelayedPopup
# 菜单按钮弹出：点击右侧向下的箭头才可以弹出菜单
# tb.setPopupMode(QToolButton.MenuButtonPopup)
# 立即弹出：点击整体按钮弹出菜单
tb.setPopupMode(QToolButton.InstantPopup)


# 这里可以接受一个参数 QAction
def do_action(act):
    print('点击了行为！', act)
    # 给每个行为绑定不同的数据
    # 可以根据此数据做不同的操作
    print('绑定的数据是：', act.data())


# 打印了两句：
# 有一句是 QAction 自己发射的信号
# 另外一句是 QToolButton 发射的信号
tb.triggered.connect(do_action)
# 用 QToolButton 的信号优点：可以统一汇总，不用每个 QAction 都写一个槽函数


# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
