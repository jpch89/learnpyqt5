# 0. 导入需要的包和模块

# 主要包含了我们常用的一些类，汇总到了一块
from PyQt5.Qt import *

# 用到了 sys.argv 和 sys.exit()
import sys
# 我们的代码，到时候的执行方式：
# 1. 通过 PyCharm 执行
# 2. 通过命令执行：python 文件名.py
#    通过命令行执行，是可以传入参数的
# 当别人通过命令行启动这个程序的时候，可以设定一种功能
# 接受命令行传递的参数，来执行不同的业务逻辑
args = sys.argv
# print(args)

# 1. 创建一个应用程序对象
# 假如通过命令行执行，传过来是一个列表
# 传给了应用程序对象
app = QApplication(sys.argv)
print(app.arguments())
# 全局的应用程序对象 qApp
# qApp 是 __init__ 文件最后一行创建的全局应用程序对象
# 只要导入，就会被自动创建
# qApp = QApplication()
print(qApp.arguments())
# 总结：在其他地方获取命令行参数的两种方式
# 1. app.arguments()
# 2. aApp.arguments()

# 2. 控件的操作
# 创建控件，设置控件（大小，位置，样式...），事件，信号的处理
# 2.1 创建控件
# 当我们创建一个控件之后，如果说，这个控件没有父控件，则把它当做顶层空间，把它称作窗口
# 系统会自动给窗口添加一些装饰（比如说标题栏）
# 窗口控件具备一些特性（比如可以设置标题、图标）
window = QWidget()
# window = QPushButton()
# window = QLabel()

# 2.2 设置控件
# window.setText('你好PyQt5')
window.setWindowTitle('PyQt5程序基本结构分析')
window.resize(400, 400)
# 控件也可以作为一个容器（承载其他的控件）
# label = QLabel()
# 设置父控件为 window
# 默认放在左上角
label = QLabel(window)
label.setText('这是一个标签')
# 控制标签的左上角
label.move(100, 50)
# label.setWindowTitle('标签的标题')
# label.show()

# 2.3 展示控件
# 刚创建好一个控件之后（这个控件没有什么父控件）
# 默认情况下不会被展示，只有手动的调用 show() 才可以
# 如果说这个控件，有父控件的，那么一般情况下，父控件展示之后，子控件会自动展示
window.show()

# 3. 应用程序的执行，进入到消息循环
# app.exec_() 的作用就是：
# 让整个程序开始执行，并且进入到消息循环（无限循环）
# 这样窗口就不会一闪而过
# 检测整个程序所接收到的用户交互信息
result = app.exec_()
sys.exit(result)
# 合起来就是 sys.exit(app.exec_())
# 得到错误码，并返回给系统

# sys.exit(status=None)
# 当前系统退出程序的函数
# 可以指定退出码
# Python 解释器是 cPython
# cPython 有一个退出码机制
# 0 为正常退出
# sys.exit()
