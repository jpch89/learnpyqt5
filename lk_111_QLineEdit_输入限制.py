# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('输入限制')
window.resize(500, 500)

le_a = QLineEdit(window)
le_a.move(100, 100)
# 长度限制
le_a.setMaxLength(3)
# 获取长度限制
print('上面的文本框的长度限制：', le_a.maxLength())
# 注意：通过代码设置文本，也会自动截断到 3 个字符长度

le_b = QLineEdit(window)
le_b.move(100, 200)
# 只读限制
le_b.setReadOnly(True)
# 获取是否只读
print('下面的文本框是否只读：', le_b.isReadOnly())
# 可以通过代码设置文本
le_b.setText('只能看，不能改')

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
