import sys
from PyQt5.Qt import *

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('PyQt5初体验')
window.resize(500, 500)
window.move(400, 200)

label = QLabel(window)
label.setText('你好，PyQt5')
label.move(200, 200)

window.show()

sys.exit(app.exec_())
