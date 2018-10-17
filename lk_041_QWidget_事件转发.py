# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *


class Window(QWidget):
    def mousePressEvent(self, QMouseEvent):
        print('顶层窗口：鼠标按下！')


class MidWindow(QWidget):
    # 如果中间控件不处理鼠标按下事件
    # 则会转发事件给顶层窗口
    # pass
    def mousePressEvent(self, evt):
        print('中间控件：鼠标按下！')


class Label(QLabel):
    # 如果标签不处理鼠标按下事件
    # 则会转发事件给中间控件
    # pass
    def mousePressEvent(self, evt):
        print('标签控件：鼠标按下！')
        # 每个事件里面有两个方法可以标识
        # evt.accept() 告诉系统，事件已经被处理，不要转发
        evt.accept()
        print('标签鼠标点击事件是否被处理：', evt.isAccepted())
        # evt.ignore() 将事件标识为未处理，所以会向父控件转发
        evt.ignore()
        print('标签鼠标点击事件是否被处理：', evt.isAccepted())


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = Window()
# 2.2 设置控件
window.setWindowTitle('事件转发')
window.resize(500, 500)

# 中间控件
mid_window = MidWindow(window)
mid_window.resize(300, 300)
# 让 qss 样式生效
mid_window.setAttribute(Qt.WA_StyledBackground, True)
mid_window.setStyleSheet('background-color: yellow;')

# 标签
# 标签的作用在于展示内容给用户
# 如果使用默认的 QLabel
# 这个类是没有处理 mousePressEvent 的
# 所以会向父控件转发事件
label = Label(mid_window)
label.setText('我是标签')
label.setStyleSheet('background-color: red;')
label.move(100, 100)

# 按钮
# 按钮本身的作用就是监听用户的点击
# 它会在自己类里面的 mousePressEvent 处理事件
# 所以就不会再转发给父控件
btn = QPushButton(mid_window)
btn.setText('我是按钮')
btn.move(50, 50)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
