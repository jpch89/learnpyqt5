# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('交互状态')
window.resize(500, 500)

btn = QPushButton(window)
btn.setText('按钮')
btn.pressed.connect(lambda: print('被点击了！'))
btn.setEnabled(False)
print('按钮是否可用：', btn.isEnabled())

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
