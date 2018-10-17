# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('自定义鼠标')
window.resize(500, 500)
# 自定义鼠标
# 1> 创建 QPixmap 对象并调整大小
pixmap = QPixmap('img/cursor.png')
# scaled方法不改变原来的 QPixmap 对象
# 而是会返回一个新的 QPixmap 对象
pixmap = pixmap.scaled(50, 50)
# 2> 创建 QCursor 对象
# QCursor(QPixmap, hotX: int = -1, hotY: int = -1)
# 热点x和热点y默认是 -1, -1：大概是鼠标图片的中间位置
# 0, 0：图片的左上角
# 假如是 50, 50：图片的右下角
cursor = QCursor(pixmap, 0, 0)
# 3> 设置自定义鼠标
window.setCursor(cursor)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
