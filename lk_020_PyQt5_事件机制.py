import sys
from PyQt5.Qt import *


class App(QApplication):
    # 方法的重写
    # QObject 是形参类型，实际上是事件的接收者（receiver）
    # QEvent 是事件对象，由事件消息包装而来（evt）
    def notify(self, receiver, evt):
        # QEvent 对象提供了 type 方法
        # 判定是什么类型的事件
        if receiver.inherits('QPushButton') and evt.type() == QEvent.MouseButtonPress:
            print('QApplication 的 notify 方法：', receiver, evt)
        # else:  # 拦截事件分发（最终程序会报错）
        # 调用父类原方法
        # 但是这样还是有错
        # 因为没有写返回值，或者说返回值为 None
        # super().notify(receiver, evt)
        # 所以要这么写！
        return super().notify(receiver, evt)


class Btn(QPushButton):
    # event 方法做了这么一件事
    # 根据接收到的 evt 事件类型
    # 把事件分发给 QPushButton 对象具体的事件函数
    # 在这些具体的事件函数中，QPushButton 可能发送了对应的信号
    def event(self, evt):
        if evt.type() == QEvent.MouseButtonPress:
            print('QPushButton 的 event 方法：', evt)
        return super().event(evt)

    def mousePressEvent(self, *args, **kwargs):
        print('QPushButton 的 mousePressEvent 函数：鼠标被按下了！')
        return super().mousePressEvent(*args, **kwargs)


app = App(sys.argv)

window = QWidget()
btn = Btn(window)
btn.setText('按钮')
btn.move(100, 100)


def slot():
    print('槽函数：按钮被点击了！')


btn.pressed.connect(slot)

window.show()

sys.exit(app.exec_())
