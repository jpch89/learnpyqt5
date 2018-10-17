import sys
from PyQt5.Qt import *

app = QApplication(sys.argv)

window = QWidget()
# window.resize
# window.setGeometry
window.resize(500, 500)  # 不加窗口框架，仅仅是用户区域
window.move(300, 300)  # 加上窗口框架
window.show()

sys.exit(app.exec_())
