# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *


class Btn(QPushButton):
    def paintEvent(self, evt):
        print('按钮被绘制了！')
        return super().paintEvent(evt)


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('关闭控件')
window.resize(500, 500)

btn = Btn(window)
btn.setText('按钮')
btn.destroyed.connect(lambda: print('按钮被释放了！'))

# 隐藏按钮的三种方式
# btn.setVisible(False)
# btn.setHidden(True)
# btn.hide()
# 关闭控件 - 不会触发 destroyed 信号
# 所以一般情况下，close() 相当于隐藏了控件
# 但是如果设置了 setAttribute(Qt.WA_DeleteOnClose, True)
# 则在关闭之后就会删除控件
btn.setAttribute(Qt.WA_DeleteOnClose, True)
btn.close()
# 下次循环删除按钮 - 会触发 destroyed 信号
# btn.deleteLater()

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
