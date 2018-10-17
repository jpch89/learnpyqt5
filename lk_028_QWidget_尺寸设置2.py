# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('QWidget 尺寸设置2')
window.move(200, 100)
# window.resize(500, 500)
# 这样就无法改变窗口大小了
window.setFixedSize(500, 500)


def slot():
    new_content = label.text() + '标签1'
    label.setText(new_content)
    # 笨方法
    # label.resize(label.width() + 100, label.height())
    # 或者使用自适应大小 label.adjustSize()
    label.adjustSize()


label = QLabel(window)
label.setText('标签1')
label.move(100, 100)
label.setStyleSheet('background-color: cyan;')

btn = QPushButton(window)
btn.setText('增加内容')
btn.move(100, 300)
btn.clicked.connect(slot)

window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
