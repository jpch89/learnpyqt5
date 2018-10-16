# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
window = QWidget()
window.move(100, 100)
window.resize(200, 200)

print('x:', window.x())
print('width:', window.width())
# 用户区域的 x, y, width, height
print('geometry:', window.geometry())

# 注意：控件显示完毕之后，获取到的尺寸数据才是正确的
window.show()

print('-' * 20 + '控件显示完毕' + '-' * 20)
print('x:', window.x())
print('width:', window.width())
# 用户区域的 x, y, width, height
print('geometry:', window.geometry())

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
