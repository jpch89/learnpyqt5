# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('尺寸限定API')
# window.resize(500, 500)
# 固定尺寸
# window.setFixedSize(500, 500)

# 整体限定最小最大尺寸
# window.setMinimumSize(300, 300)
# 如果不设置最大值，其实也有一个限定，不会大过桌面
window.setMaximumSize(600, 600)

# 单独限定尺寸
# window.setMinimumWidth(300)
# window.setMaximumWidth(600)

# 尝试能否通过 resize 来重新设置大小
# 不可以！
# 一旦通过 resize 修改的范围大于最大值
# 会被限定在最大值
window.resize(800, 800)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
