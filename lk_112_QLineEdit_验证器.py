from PyQt5.Qt import *


class AgeValidator(QValidator):
    def validate(self, input_str, pos_int):
        print(input_str, pos_int)

        # 判定
        # 结果字符串，应该全部都是由一些数字组成
        # 方法1：正则
        # 方法2：try except
        # 自己想的方法3：str.isdigits()
        try:
            if 18 <= int(input_str) <= 180:
                return QValidator.Acceptable, input_str, pos_int
            elif 1 <= int(input_str) <= 17:
                return QValidator.Intermediate, input_str, pos_int
            else:
                # 注意：无效数据不会被展示在文本框内部！
                return QValidator.Invalid, input_str, pos_int
        except:
            if len(input_str) == 0:
                return QValidator.Intermediate, input_str, pos_int
            return QValidator.Invalid, input_str, pos_int

        # 这样返回，不管怎么样都会被重置为 测试一下
        # return QValidator.Acceptable, '测试一下', 2

    def fixup(self, p_str):
        print('fixup:', p_str)
        try:
            if int(p_str) < 18:
                return '18'
            return '180'
        except:
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
        # QValidator 是 C++ 抽象类，不能直接被实例化
        # 所以要对其进行子类化
        validator = AgeValidator()
        le.setValidator(validator)

        le2 = QLineEdit(self)
        le2.move(100, 200)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
