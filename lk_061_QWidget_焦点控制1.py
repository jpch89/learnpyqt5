# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('焦点控制1')
window.resize(500, 500)

le1 = QLineEdit(window)
le1.move(50, 50)

le2 = QLineEdit(window)
le2.move(50, 100)

le3 = QLineEdit(window)
le3.move(50, 150)

# 设置焦点
le2.setFocus()
# 清除焦点
# 注意：清除焦点后，在大控件中需要找到一个控件来设置焦点
# 所以一般默认找到第一个作为焦点
le2.clearFocus()

# 设置焦点获取策略
# Qt.TabFocus 只通过 Tab 获取焦点
le3.setFocusPolicy(Qt.TabFocus)
# Qt.ClickFocus 只通过 鼠标点击 获取焦点
le3.setFocusPolicy(Qt.ClickFocus)
# Qt.StrongFoucus 可以通过鼠标或者点击获取焦点
# 默认就是这一种
le3.setFocusPolicy(Qt.StrongFocus)
# Qt.NoFocus 禁止获取焦点，但是 setFoucs() 方法可以让其获取焦点
le3.setFocusPolicy(Qt.NoFocus)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
