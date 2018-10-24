# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *


class Window(QWidget):
    def contextMenuEvent(self, evt):
        print('默认上下文菜单调用此方法')

        #################################
        # lk_078_QPushButton_菜单 复制开始
        # 创建菜单
        menu = QMenu(self)

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
        # lk_078_QPushButton_菜单.py 复制结束
        #################################

        # exec_ 方法可以展示菜单
        # 要传入一个 QPoint 参数（是相对于整个桌面全局位置）
        menu.exec_(evt.globalPos())
        # 注意没有 localPos() 这个方法！只有 pos()
        # pos() 就是局部位置


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = Window()
# 2.2 设置控件
window.setWindowTitle('右键菜单1')
window.resize(500, 500)

# 控件默认的上下文菜单策略是： Qt.DefaultContextMenu
# 会调用对象的 contextMenuEvent()

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
