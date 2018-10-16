from PyQt5.Qt import *

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    win_root = QWidget()

    label1 = QLabel()
    label1.setParent(win_root)
    label1.setText('label1')

    label2 = QLabel()
    label2.setParent(win_root)
    label2.setText('label2')
    label2.move(50, 50)

    label3 = QLabel()
    label3.setParent(win_root)
    label3.setText('label3')
    label3.move(80, 80)

    btn = QPushButton(win_root)
    btn.setText('btn')
    btn.move(100, 100)

    win_root.show()

    for sub_widget in win_root.findChildren(QLabel):
        print(sub_widget)
        sub_widget.setStyleSheet('background-color: cyan;')

    sys.exit(app.exec_())
