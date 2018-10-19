from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('交互状态案例')
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 添加三个子控件
        label = QLabel(self)
        label.setText('标签')
        label.move(100, 50)
        label.hide()

        line_edit = QLineEdit(self)
        # line_edit.setText('文本框')
        line_edit.move(100, 100)

        button = QPushButton(self)
        button.setText('登录')
        button.move(100, 150)
        button.setEnabled(False)

        def slot(text):
            print('文本内容发生改变：', text)
            # if len(text) > 0:
            #     button.setEnabled(True)
            # else:
            #     button.setEnabled(False)

            # 优化写法！
            button.setEnabled(len(text) > 0)

        # textChanged 的返回值是最新的文本内容！
        line_edit.textChanged.connect(slot)

        def check():
            print('按钮被点击了！')
            if line_edit.text() == '666':
                label.setText('登录成功！')
            else:
                label.setText('登录失败！')
            label.show()
            # 自适应大小
            label.adjustSize()
        button.pressed.connect(check)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
