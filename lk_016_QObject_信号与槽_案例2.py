# 修改窗口标题自动加 'jpch89-' 前缀
# 支持多次修改

from PyQt5.Qt import *


def slot(title):
    print(title, '的标题变化了')

    # 注意不能这样重新设置标题
    # 因为会发生循环调用槽函数
    # window.setWindowTitle('jpch89-' + title)

    # 方案1：先断开再连接槽函数
    # 意思就是不想让中间的语句触发槽函数
    # window.windowTitleChanged.disconnect()
    # window.setWindowTitle('jpch89-' + title)
    # window.windowTitleChanged.connect(slot)

    # 方案2：临时终止信号连接，然后恢复
    window.blockSignals(True)
    window.setWindowTitle('jpch89-' + title)
    window.blockSignals(False)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = QWidget()
    window.show()
    window.windowTitleChanged.connect(slot)
    window.setWindowTitle('你好，小明')
    window.setWindowTitle('你好，小黄')
    window.setWindowTitle('你好，小花')

    sys.exit(app.exec_())
