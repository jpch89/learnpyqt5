# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
# window.setWindowTitle('是否编辑[*]')
# window.setWindowTitle('[*]是否编辑')
window.setWindowTitle('是否[*]编辑')

# 注意：换成 [&] 就不行了，只能 [*]
# window.setWindowTitle('是否[&]编辑')

window.resize(500, 500)
# 显示为已编辑
window.setWindowModified(True)
print('是否已编辑：', window.isWindowModified())

# 应用场景：关闭之前检测 isWindowModified()
# 如果已编辑，就提示保存

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
