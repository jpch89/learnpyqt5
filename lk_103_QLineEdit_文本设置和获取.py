# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('文本设置和获取')
window.resize(500, 500)

# 其实这个构造函数就是帮我们调用了一个 setText() 方法
le = QLineEdit('单行文本编辑器', window)
# 文本设置
le.setText('进击的团子')
# 在光标处插入
# le.insert('666')

# 在光标处插入文本
btn = QPushButton(window)
btn.setText('插入')
btn.move(100, 100)
btn.clicked.connect(lambda: le.insert('666'))

# 获取文本
btn2 = QPushButton(window)
btn2.setText('获取')
btn2.move(100, 200)
btn2.clicked.connect(lambda: print('文本内容为：', le.text()))

# 获取显示的文本 displayText()

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
