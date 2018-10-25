# 拓展1：假如账号和密码其中之一没有内容，登录按钮不可用
# 拓展2：账号下面和密码下面都有提示标签，一开始是隐藏的，根据输入展示提示信息
# 拓展3：账号和密码是业务逻辑，需要与界面分离

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QLineEdit案例')
        self.resize(500, 500)
        # 设置最小尺寸
        self.setMinimumSize(400, 400)
        self.setup_ui()

    def setup_ui(self):
        # 添加三个控件
        # 下面有三个灰色波浪线
        # 提示：Instance attribute ... defined outside __init__
        # 假如在调用 setup_ui 之前就调用了 resizeEvent，就会出现问题
        # 因为此时 resizeEvent 里面会访问还没有设置的相关属性
        # 所以要把相关属性的设置放到 __init__ 里面，才会保证第一时间就被设置
        # 但我们为了方便、美观而提取了一个 setup_ui 方法
        # 实际上 setup_ui 这个方法还是在 __init__ 里面的，所以并不会有什么问题
        self.account_le = QLineEdit(self)
        self.pwd_le = QLineEdit(self)
        self.pwd_le.setEchoMode(QLineEdit.Password)
        self.login_btn = QPushButton(self)
        self.login_btn.setText('登  录')

        # 连接槽函数
        self.login_btn.clicked.connect(self.login)

    def login(self):
        # 获取账号和密码信息
        account = self.account_le.text()
        pwd = self.pwd_le.text()
        print(f'账号：{account}\n密码：{pwd}')
        if account == 'jpch89':
            if pwd == '666':
                print('登录成功')
            else:
                print('密码错误')
                self.pwd_le.setText('')
                # 密码框自动获取焦点
                # 之所以会失去焦点，是因为点击了登录按钮！
                self.pwd_le.setFocus()
        else:
            print('账号错误')
            self.account_le.setText('')
            self.pwd_le.setText('')
            # 账号文本框自动获取焦点
            self.account_le.setFocus()

        # 另外一种写法（不用写很多else）：
        # 账号错误！
        # if account != 'jpch89':
            # 进行操作
            # 账号错误，直接返回
            # return None
        # 账号正确，密码错误！
        # if pwd != '666':
            # 进行操作
            # 密码错误，直接返回
            # return None
        # 走到这里，账号密码都正确
        # print('登录成功！')

    def resizeEvent(self, evt):
        widget_w = 150
        widget_h = 40
        margin = 60
        self.account_le.resize(widget_w, widget_h)
        self.pwd_le.resize(widget_w, widget_h)
        self.login_btn.resize(widget_w, widget_h)

        x = (self.width() - widget_w) / 2

        self.account_le.move(x, self.height() / 5)
        self.pwd_le.move(x, self.account_le.y() + widget_h + margin)
        self.login_btn.move(x, self.pwd_le.y() + widget_h + margin)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
