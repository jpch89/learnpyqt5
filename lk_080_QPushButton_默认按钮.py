# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('默认按钮')
window.resize(500, 500)

btn1 = QPushButton(window)
btn1.setText('按钮1')
btn1.move(200, 200)
btn2 = QPushButton(window)
btn2.setText('按钮2')
btn2.move(200, 250)

# 设置为自动默认，点击之后就变成了默认状态
btn2.setAutoDefault(True)
# 查看自动默认状态
print('按钮1是否为自动默认：', btn1.autoDefault())
print('按钮2是否为自动默认：', btn2.autoDefault())
# 注意：自动默认必须要用户点击才会变成默认状态

# 设置为默认状态
btn1.setDefault(True)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
