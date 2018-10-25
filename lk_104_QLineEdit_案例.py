# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('案例')
window.resize(500, 500)

le_a = QLineEdit(window)
le_a.move(100, 100)

le_b = QLineEdit(window)
le_b.move(100, 200)

copy_btn = QPushButton(window)
# 注意这里的 setText 是 QAbstractButton 的方法
# 而 le_b.setText 是 QLineEdit 的方法
copy_btn.setText('复制')
copy_btn.move(100, 300)


def copy_text():
    # 获取文本框a的内容
    text = le_a.text()
    # 把上面的内容，设置到文本框b
    le_b.setText(text)
    
    # 如果是插入文本，就有问题了，因为它不会清除之前的文本！
    # 所以要先清空内容
    # le_b.setText('')
    # le_b.insert(text)


copy_btn.clicked.connect(copy_text)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
