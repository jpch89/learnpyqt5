# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('自动提升')
window.resize(500, 500)

tb = QToolButton(window)
tb.setArrowType(Qt.RightArrow)
tb.setText('前进')
tb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

# QPushButton 里面有 setFlat(True) 的扁平化方法
# 但是 QToolButton 是继承自 QAbstractButton，所以没有这个方法
# 注意普通按钮如果设置扁平化，鼠标移入不会有突起状态
# 普通按钮需要借助样式表实现（一般不用这个方法）
btn = QPushButton(window)
btn.setText('一般按钮')
btn.move(100, 100)
btn.setFlat(True)

# 使用工具按钮 setAutoRaise 设置自动提升
tb.setAutoRaise(True)
# 获取自动提升状态
print('当前按钮是否设置自动提升：', tb.autoRaise())

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
