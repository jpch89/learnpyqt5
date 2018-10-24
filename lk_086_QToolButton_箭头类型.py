# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('箭头类型')
window.resize(500, 500)

tb = QToolButton(window)

# Qt.NoArrow 无箭头
# Qt.UpArrow 向上箭头
# Qt.DownArrow 向下箭头
# Qt.LeftArrow 向左箭头
# Qt.RightArrow 向右箭头
tb.setArrowType(Qt.NoArrow)
tb.setArrowType(Qt.UpArrow)
tb.setArrowType(Qt.DownArrow)
tb.setArrowType(Qt.LeftArrow)
tb.setArrowType(Qt.RightArrow)

# 注意：如果设置了箭头和图标，箭头的优先级高
tb.setText('前进')
tb.setIcon(QIcon('img/Python.png'))
tb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

# 获取箭头类型
print('当前箭头类型：', tb.arrowType())

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
