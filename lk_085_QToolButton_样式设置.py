# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('')
window.resize(500, 500)

tb = QToolButton(window)
tb.setText('打开')
tb.setIcon(QIcon('img/打开.png'))
tb.setIconSize(QSize(60, 60))
tb.setToolTip('打开文件')

# 设置工具按钮样式
# Qt.ToolButtonIconOnly 仅显示图标
# Qt.ToolButtonTextOnly 仅显示文字
# Qt.ToolButtonTextBesideIcon 文本显示在图标旁边
# Qt.ToolButtonTextUnderIcon 文本显示在图标下方
# Qt.ToolButtonFollowStyle 遵循风格
tb.setToolButtonStyle(Qt.ToolButtonIconOnly)
tb.setToolButtonStyle(Qt.ToolButtonTextOnly)
tb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)  # 类似于普通的 QPushButton
tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
tb.setToolButtonStyle(Qt.ToolButtonFollowStyle)

# 获取 toolButtonStyle()
# 注意返回的是数字
print('当前工具按钮样式：', tb.toolButtonStyle())

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
