# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 方法1：在创建的时候设置 flags
        # window = QWidget(flags=Qt.FramelessWindowHint)
        # 方法2：使用 setWindowFlags()
        # 注意：setWindowFlag() 也可以，设置单个标志
        self.setWindowFlags(Qt.FramelessWindowHint)

        # 不透明度设置
        self.setWindowOpacity(0.9)

        # 设置控件
        self.setWindowTitle('顶层窗口操作案例')
        self.resize(500, 500)
        self.move_flag = False

        # 公共数据
        self.top_margin = 0
        self.btn_w = 40
        self.btn_h = 40

        self.setup_ui()

    def setup_ui(self):
        # 添加 3 个子控件按钮 - 窗口的右上角
        close_icon = QIcon('img/close.png')
        close_btn = QPushButton(close_icon, '', self)
        self.close_btn = close_btn
        # close_btn.setText('关闭')
        close_btn.resize(self.btn_w, self.btn_h)

        max_icon = QIcon('img/maximize.png')
        max_btn = QPushButton(max_icon, '', self)
        self.max_btn = max_btn
        # max_btn.setText('最大化')
        max_btn.resize(self.btn_w, self.btn_h)

        mini_icon = QIcon('img/minimize.png')
        mini_btn = QPushButton(mini_icon, '', self)
        self.mini_btn = mini_btn
        # mini_btn.setText('最小化')
        mini_btn.resize(self.btn_w, self.btn_h)

        def max_normal():
            if self.isMaximized():
                self.showNormal()
                # max_btn.setText('最大化')
            else:
                self.showMaximized()
                # max_btn.setText('还原')

        close_btn.pressed.connect(self.close)
        max_btn.pressed.connect(max_normal)
        mini_btn.pressed.connect(self.showMinimized)

    def resizeEvent(self, evt):
        # print('窗口大小改变了')

        window_w = self.width()
        close_btn_x = window_w - self.btn_w
        close_btn_y = self.top_margin
        self.close_btn.move(close_btn_x, close_btn_y)

        max_btn_x = close_btn_x - self.btn_w
        max_btn_y = self.top_margin
        self.max_btn.move(max_btn_x, max_btn_y)

        mini_btn_x = max_btn_x - self.btn_w
        mini_btn_y = self.top_margin
        self.mini_btn.move(mini_btn_x, mini_btn_y)

    def mousePressEvent(self, evt):
        # 设置标记，用于判定是否需要移动
        # 并判定是否点击了鼠标左键
        # 注意：这个判等不能用 is
        if evt.button() == Qt.LeftButton:
            self.move_flag = True
        # 窗口的原始坐标点（左上角）
        # 注意：之前这里用了 self.x 和 self.y
        # 程序报错！我怀疑是 self.x 和 self.y 已经被 PyQt 占用
        self.origin_x = self.x()
        self.origin_y = self.y()
        # 鼠标按下的点
        self.mouse_x = evt.globalX()
        self.mouse_y = evt.globalY()

    def mouseMoveEvent(self, evt):
        # 如果窗口移动标记 = True
        if self.move_flag:
            # 根据鼠标按下的点，计算移动向量
            move_x = evt.globalX() - self.mouse_x
            move_y = evt.globalY() - self.mouse_y
            # 根据移动向量和窗口原始坐标，计算最新坐标
            new_x = self.origin_x + move_x
            new_y = self.origin_y + move_y
            # 移动整个窗口的位置
            self.move(new_x, new_y)

    def mouseReleaseEvent(self, evt):
        # 重置窗口移动标记 = False
        self.move_flag = False


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)
window = Window()

# 2 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
