"""
案例1: 实现简单的登录界面逻辑
要求:
    1. 如果文本框和密码框有一个为空, 则将登录按钮置为无效, 不能点击;
    2. 正确账号: 进击的团子, 正确密码: 666
    3. 点击登录按钮后, 检查账号密码, 并将比对结果通过提示标签展示给用户;
    (例如: 账号错误, 密码错误, 登录成功)
"""

from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.resize(500, 400)
window.setWindowTitle('登录系统')
icon = QIcon('img/Python.png')
window.setWindowIcon(icon)

title_label = QLabel(window)
title_label.setText('登录系统')
title_label.move(160, 50)
title_label.setStyleSheet('font-size: 40px; font-weight: bold; font-family: 楷体;')


def slot():
    if account.text() and passwd.text():
        btn.setEnabled(True)
    else:
        btn.setEnabled(False)


account = QLineEdit(window)
account.resize(100, 20)
account.move(220, 150)
account.textChanged.connect(slot)

account_label = QLabel(window)
account_label.setText('账号：')
account_label.move(150, 150)
account_label.setStyleSheet('font-size: 20px;')

passwd = QLineEdit(window)
passwd.resize(100, 20)
passwd.move(220, 200)
passwd.textChanged.connect(slot)

passwd_label = QLabel(window)
passwd_label.setText('密码：')
passwd_label.move(150, 200)
passwd_label.setStyleSheet('font-size: 20px;')


def login():
    if account.text() == '进击的团子' and passwd.text() == '666':
        hint_label.setText('登录成功！')
        hint_label.move(200, 260)
        hint_label.setStyleSheet('font-size: 18px; color: #00a854;')
    elif account.text() == '进击的团子' and passwd.text() != '666':
        hint_label.setText('密码错误！')
        hint_label.move(200, 260)
        hint_label.setStyleSheet('font-size: 18px; color: red;')
    elif account.text() != '进击的团子' and passwd.text() == '666':
        hint_label.setText('账号错误！')
        hint_label.move(200, 260)
        hint_label.setStyleSheet('font-size: 18px; color: red;')
    else:
        hint_label.setText('账号和密码有误，请重新输入！')
        hint_label.adjustSize()
        hint_label.move(120, 260)
        hint_label.setStyleSheet('font-size: 18px; color: red;')


btn = QPushButton(window)
btn.resize(100, 50)
btn.move(180, 320)
btn.setText('登录')
btn.setIcon(QIcon('img/登录.png'))
btn.setIconSize(QSize(30, 30))
btn.setStyleSheet('font-size: 20px;')
btn.setEnabled(False)
btn.clicked.connect(login)

hint_label = QLabel(window)
hint_label.setText('请输入账号和密码！')
hint_label.move(160, 260)
hint_label.setStyleSheet('font-size: 18px;')

window.show()

sys.exit(app.exec_())
