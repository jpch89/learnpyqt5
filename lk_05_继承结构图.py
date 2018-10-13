# 本文件未完成！
# 遍历所有类还不太会编写
from PyQt5.Qt import *

def get_sub_classes(cls):
    for subcls in cls.__subclasses__():
        print(subcls)
        if len(subcls.__subclasses__()) > 0:
            get_sub_classes(subcls)


# print(QObject.__subclasses__())
# print(QWidget.__subclasses__())
print(QAbstractButton.__subclasses__())
get_sub_classes(QObject)
