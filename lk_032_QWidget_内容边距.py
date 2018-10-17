# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('内容边距')
window.resize(500, 500)

label = QLabel(window)
# 默认是水平靠左，垂直居中
label.setText('天青色等烟雨，而我在等你')
label.resize(300, 300)
label.setStyleSheet('background-color: cyan;')
# 设置内容边距，左上右下
label.setContentsMargins(100, 200, 0, 0)
# 获取内容区域
print(label.contentsRect())
# 获取内容边距 - 注意跟上面获取内容区域是不同的！
print(label.getContentsMargins())

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
