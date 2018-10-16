# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('QWidget继承')
window.resize(500, 500)

# 查看 QWidget 父类的几种方式：
# 方法1：Ctrl - 单击 QWidget
# 方法2：__bases__，返回一个元组
print(QWidget.__bases__)
# 方法3：mro
print(QWidget.mro())

# 父类 QObject 的方法 QWidget 都可以使用
window.setObjectName('窗口')
print(window.objectName())

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
