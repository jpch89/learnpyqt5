# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('排他性')
window.resize(500, 500)

for i in range(3):
    btn = QPushButton(window)
    btn_name = '按钮' + str(i + 1)
    btn.setText(btn_name)
    btn.move(50 * i, 50 * i)

    # 使用 autoExclusive() 获取按钮排他性状态
    print(btn_name, '是否排他：', btn.autoExclusive())
    # 默认情况下 QPushButton 是不可选中的
    print(f'默认情况 {btn_name} 是否可选中：', btn.isCheckable())
    print('-' * 50)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
