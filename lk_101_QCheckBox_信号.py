# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('QCheckBox信号')
window.resize(500, 500)

cb = QCheckBox('&Python', window)
cb.setIcon(QIcon('img/Python.png'))
cb.setIconSize(QSize(30, 30))
cb.setTristate(True)

# cb.stateChanged.connect(lambda state: print('状态是：', state))
cb.toggled.connect(lambda is_checked: print('是否被选中：', is_checked))

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
