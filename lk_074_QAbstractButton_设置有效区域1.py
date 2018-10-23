# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('设置有效区域')
window.resize(500, 500)


class Button(QPushButton):
    # 需求：点击按钮右半部分有效，左半部分无效
    # 注意：点的坐标参照按钮的坐标，是相对坐标
    # 右侧区域：x 大于整个按钮宽度的一半
    def hitButton(self, point):
        print(point)
        # point 的类型是 PyQt5.QtCore.QPoint
        # 可以 Ctrl - 单击 查看文档
        if point.x() > self.width() / 2:
            return True

        return False


button = Button(window)
button.setText('点击')
button.move(200, 200)
button.pressed.connect(lambda: print('按钮被点击了！'))

# 按钮被点击之后
# 会把点坐标传递给 hitButton 方法
# 看看 hitButton 方法的返回值是什么
# 如果是 True，说明点击是有效的，会发射信号
# 如果是 False，说明点击是无效的，就不会触发相关信号的发射

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
