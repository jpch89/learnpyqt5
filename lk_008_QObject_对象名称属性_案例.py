from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QObject的学习')
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        self.QObject案例演示()

    def QObject案例演示(self):
        # 设置全局 QSS
        with open('lk_008_QObject_对象名称属性_案例.qss', 'r') as f:
            qApp.setStyleSheet(f.read())

        label = QLabel(self)
        label.setObjectName('notice')
        label.setProperty('notice_level', 'normal')
        label.setText('QObject学习1')
        # 设置 QSS 字符串
        # label.setStyleSheet('font-size: 20px; color: red;')

        label2 = QLabel(self)
        label2.setObjectName('notice')
        label2.setProperty('notice_level', 'warning')
        label2.move(100, 100)
        label2.setText('QObject学习2')

        label3 = QLabel(self)
        label3.setObjectName('notice')
        label3.setProperty('notice_level', 'error')
        label3.setText('QObject学习3')
        label3.move(150, 150)

        # 没有匹配到 QPushButton
        # 所以样式不生效
        btn = QPushButton(self)
        # 这样也不行，因为 QPushButton 不是 QLabel
        btn.setObjectName('notice')
        btn.setText('按钮')
        btn.move(50, 50)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
