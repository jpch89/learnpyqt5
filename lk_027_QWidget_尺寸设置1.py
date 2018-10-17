# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('QWidget 尺寸设置1')

# 移动（包含窗口框架）
# window.move(100, 100)

# 更改用户区域的宽高
# 100, 100 显示出来的是一个长方形
# 因为窗口框架有一个最小值的限定
# window.resize(100, 100)
# window.resize(200, 200)

# 用户区域距离左上角的位置
# 显示之前设置会有问题
# window.setGeometry(0, 0, 200, 200)

window.show()
# 要在显示之后设置
# window.setGeometry(0, 0, 200, 200)

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
