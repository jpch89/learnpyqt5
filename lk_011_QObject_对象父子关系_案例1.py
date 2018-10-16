from PyQt5.Qt import *

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    win1 = QWidget()
    win1.setWindowTitle('第一个独立窗口')
    win1.setStyleSheet('background-color: red;')
    win1.resize(500, 500)

    win2 = QWidget()
    win2.setWindowTitle('第二个独立窗口')
    win2.setStyleSheet('background-color: green')
    win2.resize(400, 400)

    # 如果要设置不同的标题
    # 必须是独立窗口
    # 所以不能设置父子关系
    # win2.setParent(win1)

    win1.show()
    win2.show()

    sys.exit(app.exec_())
