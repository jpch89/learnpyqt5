# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('构造函数')
window.resize(500, 500)

# 不设置父控件的时候，就是顶层窗口，默认不显示
# 需要使用 show 或者 setVisible(True) 才行
# btn = QPushButton()
# btn.show()
# btn.setVisible(True)

# 设置父控件
# btn = QPushButton(window)
# 或者：
# btn = QPushButton()
# btn.setParent(window)
# 设置文本
# btn.setText('按钮')

# 同时设置文本和父控件
# btn = QPushButton('按钮', window)
# 设置图标
# btn.setIcon(QIcon('img/Python.png'))

# 同时设置图标，文本和父控件
btn = QPushButton(QIcon('img/Python.png'), '按钮', window)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
