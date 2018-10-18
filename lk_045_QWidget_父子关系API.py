# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('QWidget父子关系学习')
window.resize(500, 500)

label1 = QLabel(window)
# 也可以这样写
# label1.setParent(window)
label1.setText('标签1')

label2 = QLabel(window)
label2.setText('标签2')
label2.move(50, 50)

label3 = QLabel(window)
label3.setText('标签3')
label3.move(100, 100)

# 需求：查看 55, 55 坐标点有没有子控件
# 注意：这个是相对于父控件左上角的位置
# 使用 childAt(x, y)
print(window.childAt(55, 55))

# parentWidget() 查看父控件
print(label2.parentWidget())

# childrenRect() 查看所有子控件组成的边界矩形
print(window.childrenRect())

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
