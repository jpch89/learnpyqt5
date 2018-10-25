# 拓展1：假如账号和密码其中之一没有内容，登录按钮不可用
# 拓展2：账号下面和密码下面都有提示标签，一开始是隐藏的，根据输入展示提示信息
# 拓展3：账号和密码是业务逻辑，需要与界面分离

from PyQt5.Qt import *


class AccountTool:  # 默认继承 object
    ACCOUNT_ERROR = 1
    PWD_ERROR = 2
    SUCCESS = 3

    @staticmethod
    def check_login(account, pwd):
        # 把账号和密码发送给服务器，等待服务器返回结果
        if account != 'jpch89':
            # 返回一个状态
            return AccountTool.ACCOUNT_ERROR
            # 或者通过类名访问也可以
            # return AccountTool.ACCOUNT_ERROR
        if pwd != '666':
            return AccountTool.PWD_ERROR
        return AccountTool.SUCCESS


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QLineEdit案例')
        self.resize(500, 500)
        # 设置最小尺寸
        self.setMinimumSize(400, 400)
        self.setup_ui()

    def setup_ui(self):
        self.account_le = QLineEdit(self)
        self.pwd_le = QLineEdit(self)
        self.pwd_le.setEchoMode(QLineEdit.Password)
        self.login_btn = QPushButton(self)
        self.login_btn.setText('登  录')

        # 占位文本的提示
        self.account_le.setPlaceholderText('请输入账号')
        self.pwd_le.setPlaceholderText('请输入密码')

        # 设置密码文本框，自动显示清空按钮
        self.pwd_le.setClearButtonEnabled(True)

        # 添加自定义动作（明文和密文切换）
        # 三种写法：
        # addAction(self, QAction)
        # addAction(self, QAction, QLineEdit.ActionPosition)
        # addAction(self, QIcon, QLineEdit.ActionPosition) -> QAction
        # 设置文本框作为它的父对象，文本框没有的时候，它就会被自动释放掉
        action = QAction(self.pwd_le)
        action.setIcon(QIcon('img/隐藏密码.png'))

        def change():
            # print('切换明文和密文')
            if self.pwd_le.echoMode() == QLineEdit.Password:
                self.pwd_le.setEchoMode(QLineEdit.Normal)
                action.setIcon(QIcon('img/显示密码.png'))
            else:
                self.pwd_le.setEchoMode(QLineEdit.Password)
                action.setIcon(QIcon('img/隐藏密码.png'))

        action.triggered.connect(change)
        # 图标在尾部
        self.pwd_le.addAction(action, QLineEdit.TrailingPosition)
        # 图标在头部
        # self.pwd_le.addAction(action, QLineEdit.LeadingPosition)

        # 自动补全
        # QCompleter(Iterable[str], parent: QObject = None)
        # 完成器生命周期归账号文本框 account_le 管理
        completer = QCompleter(['jpch89', '进击的团子', 'jinjidetuanzi'], self.account_le)
        self.account_le.setCompleter(completer)

        # 连接槽函数
        self.login_btn.clicked.connect(self.login)

    def login(self):
        # 获取账号和密码信息
        account = self.account_le.text()
        pwd = self.pwd_le.text()
        print(f'账号：{account}\n密码：{pwd}')
        state = AccountTool.check_login(account, pwd)
        if state == AccountTool.ACCOUNT_ERROR:
            print('账号错误')
            self.account_le.setText('')
            self.pwd_le.setText('')
            self.account_le.setFocus()
            # 可写可不写
            # 但是写了可以跳过后续判定
            # 加快程序执行
            return None

        if state == AccountTool.PWD_ERROR:
            print('密码错误')
            self.pwd_le.setText('')
            self.pwd_le.setFocus()
            # 可写可不写
            # 但是写了可以跳过后续判定
            # 加快程序执行
            return None

        # 这里可以不用判定！
        if state == AccountTool.SUCCESS:
            print('登录成功')

    def resizeEvent(self, evt):
        widget_w = 200
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
