# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('鼠标操作1')
window.resize(500, 500)

# 更改鼠标样式
# window.setCursor(Qt.BusyCursor)
window.setCursor(Qt.ForbiddenCursor)


# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
