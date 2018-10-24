# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('QCommandLinkButton使用')
window.resize(500, 500)

# QCommandLinkButton(父控件)
# QCommandLinkButton(标题, 父控件)
# QCommandLinkButton(标题, 描述, 父控件)
btn = QCommandLinkButton('标题', '描述', window)

# QCommandLinkButton 自动多出来一个箭头图标
# 可以使用 setIcon 来更换
# 描述字体小于标题

# 更改标题 setText
btn.setText('更改后的标题')

# 更改描述 setDescription
btn.setDescription('更改后的描述')

# 更改图标 setIcon
# 该方法属于 QAbstractButton
btn.setIcon(QIcon('img/Python.png'))

# 获取文本 text
# 获取图标 icon
# 获取描述 description
print(btn.description())

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
