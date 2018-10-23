# 0. 导入需要的包和模块
import sys
from math import sqrt
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('设置有效区域-圆形')
window.resize(500, 500)


class Button(QPushButton):
    def hitButton(self, point):
        # 通过给定的一个点的坐标，计算与圆心的距离
        center_x = self.width() / 2
        center_y = self.height() / 2

        hit_x = point.x()
        hit_y = point.y()

        # 平方也可以用 math.pow(x, 2)
        dist = sqrt((center_x - hit_x) ** 2 + (center_y - hit_y) ** 2)
        # print(dist)

        # 注意：必须要写 return True 或者 return False
        # 否则程序会崩溃

        if dist < self.width() / 2:
            return True
        return False

    # 在整个按钮内部画一个内切圆
    def paintEvent(self, evt):
        # 通过调用父类方法，保留之前的绘制（即按钮上的文本）
        super().paintEvent(evt)
        # 创建画家，传入画布（就是按钮）
        painter = QPainter(self)
        # 给画家一根笔
        pen = QPen(QColor(100, 150, 200), 2)
        painter.setPen(pen)
        # 画画
        painter.drawEllipse(self.rect())


button = Button(window)
button.setText('按钮')
button.resize(200, 200)
button.move(100, 100)
button.clicked.connect(lambda: print('按钮被点击了！'))


# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
