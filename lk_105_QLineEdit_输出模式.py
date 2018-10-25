# 0. 导入需要的包和模块
import sys
from PyQt5.Qt import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('输出模式')
window.resize(500, 500)

le = QLineEdit(window)
le.move(100, 100)

# 查看代码文档
# setEchoMode(self, QLineEdit.EchoMode)
# QLineEdit.EchoMode 说明枚举值被定义在类的内部
# 相当于是定义了类属性，通过 类名.类属性名 来访问
# 在类定义中往下翻就能找到
# Normal = 0
# NoEcho = 1
# Password = 2
# PasswordEchoOnEdit = 3

# 不回显：对密码加密的更狠，连位数都不显示
le.setEchoMode(QLineEdit.NoEcho)

# 普通模式
le.setEchoMode(QLineEdit.Normal)

# 密文模式
le.setEchoMode(QLineEdit.Password)

# 失去焦点变成密文
le.setEchoMode(QLineEdit.PasswordEchoOnEdit)

btn = QPushButton('打印', window)
btn.move(100, 200)
btn.clicked.connect(lambda: print('内容为：', le.text()))
btn.clicked.connect(lambda: print('展示内容为：', le.displayText()))

# 获取当前输出模式
print('当前输出模式为：', le.echoMode())

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
