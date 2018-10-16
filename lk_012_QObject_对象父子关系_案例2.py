from PyQt5.Qt import *

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    win_root = QWidget()

    label1 = QLabel()
    label1.setParent(win_root)
    # 或者可以这么设置
    # label1 = QLabel(win_root)
    label1.setText('label1')

    btn = QPushButton(win_root)
    # 或者也可以这么设置
    # btn.setParent(win_root)
    btn.setText('btn')
    btn.move(100, 100)

    win_root.show()

    sys.exit(app.exec_())
