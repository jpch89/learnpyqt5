from PyQt5.Qt import *


class AgeValidator(QIntValidator):
    def fixup(self, p_str):
        # 打印出结果，意味着数据是无效的
        # 需要进行修复
        print('fixup：', p_str)
        # 假如 p_str 长度等于零，不会进行 int(p_str) 类型转换
        # 短路逻辑！
        # 注意：这两个条件反过来就不行了！
        if len(p_str) == 0 or int(p_str) < 18:
            return '18'


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QLineEdit验证器')
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        le = QLineEdit(self)
        le.move(100, 100)

        # 验证要求：数字 18-180
        # 只能限定最大值，不能限定最小值
        # 中间状态没有去处理
        # 所以可以借助它，在其基础上进行二次定制
        validator = AgeValidator(18, 180)
        le.setValidator(validator)

        le2 = QLineEdit(self)
        le2.move(100, 200)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
