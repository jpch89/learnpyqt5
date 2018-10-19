# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QMainWindow()  # 组合控件：这个控件由很多控件组合起来的
# 里面很多子控件是懒加载的 -- 用到的时候才会创建
window.statusBar()  # 加载状态栏
# 2.2 设置控件
window.setWindowTitle('信息提示案例')
window.resize(500, 500)
# Qt.WindowContextHelpButtonHint 窗口上下文帮助按钮
window.setWindowFlags(Qt.WindowContextHelpButtonHint)

# 当鼠标停留在窗口控件身上之后，在状态栏提示的一段文本
# 注意：必须先有状态栏！
window.setStatusTip('这是状态提示！')
# 获取状态提示信息
print(window.statusTip())

label = QLabel(window)
label.setText('标签控件')
# 设置状态提示
label.setStatusTip('这是标签的状态提示！')
# 设置工具提示
label.setToolTip('这是标签的工具提示！')
# 获取工具提示
print(label.toolTip())
# 设置工具提示显示时长，单位是 ms
label.setToolTipDuration(2000)
# 获取显示时长
print(label.toolTipDuration())
# 这是啥提示（黄底文本）
label.setWhatsThis('这是啥？这是标签')
# 获取这是啥提示
print(label.whatsThis())

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
