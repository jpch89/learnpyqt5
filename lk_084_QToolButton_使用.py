# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('QToolButton使用')
window.resize(500, 500)

# 构造函数 QToolButton(父控件)
tb = QToolButton(window)

# 设置文本
# 注意：如果同时设置了文本和图标，则不显示文本！
tb.setText('工具')

# 设置图标
tb.setIcon(QIcon('img/打开.png'))
tb.setIconSize(QSize(60, 60))

# 设置工具提示文本
# setToolTip 属于 QWidget
tb.setToolTip('打开文件')

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
