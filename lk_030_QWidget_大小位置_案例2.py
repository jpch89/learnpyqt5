import sys
from PyQt5.Qt import *

app = QApplication(sys.argv)

window = QWidget()

# 父控件展示之前先遍历其中所有子控件
# 所以在展示之后再设置子控件，子控件是无法展示的
# 这时子控件要手动展示
window.show()
window.resize(500, 500)
window.move(300, 300)

# 总的控件个数
widget_count = 50
# 一行有多少列
column_count = 4
# 计算一个控件的宽度
widget_width = window.width() / column_count
# 总共有多少行 (编号 // 一行多少列 + 1)
row_count = (widget_count - 1) // column_count + 1
# 计算一个控件的高度
widget_height = window.height() / row_count

for i in range(widget_count):
    # QWidget 是一个空白控件
    # 没有背景颜色，没有尺寸是看不到的
    w = QWidget(window)
    w.resize(widget_width, widget_height)
    widget_x = i % column_count * widget_width
    widget_y = i // column_count * widget_height
    w.move(widget_x, widget_y)
    w.setStyleSheet('background-color: red; border: 1px solid yellow;')
    w.show()

sys.exit(app.exec_())
