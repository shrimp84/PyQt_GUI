# window
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QDesktopWidget, QToolTip, 
        QPushButton, QMessageBox)
from PyQt5.QtGui import QIcon, QFont

#app = QApplication(sys.argv)
#w = QWidget()
#w.resize(350,150)
#w.move(300, 300)
#w.setWindowTitle("Simple")
#w.show()

#sys.exit(app.exec_())





### application icon
#class Example(QWidget):
#    def __init__(self):
#        super().__init__()
#        self.initUI()
#    def initUI(self):
#        self.setGeometry(300,300,300,220)
#        self.setWindowTitle('Icon')
#        self.setWindowIcon(QIcon('web.png'))
#
#        self.show()
#
#app = QApplication(sys.argv)
#ex = Example()
#sys.exit(app.exec_())








### push button
#class Example(QWidget):
#    def __init__(self):
#        super().__init__()
#        self.initUI()
#    def initUI(self):
#        QToolTip.setFont(QFont('SansSerif', 10))
#        self.setToolTip('This is a <b>QWidget</b> widget')
#        btn = QPushButton('Button', self)
#        btn.setToolTip("This is a <b>QPushButton</b> widget")
#        btn.resize(btn.sizeHint())
#        btn.move(50,50)
#        self.setGeometry(300,300,300,200)
#        self.setWindowTitle('ToolTips')
#        self.show()
#app = QApplication(sys.argv)
#ex = Example()
#sys.exit(app.exec_())





### closing a window
#class Example(QWidget):
#    def __init__(self):
#        super().__init__()
#        self.initUI()
#    def initUI(self):
#        qbtn = QPushButton('Quit', self)
#        qbtn.clicked.connect(QApplication.instance().quit)
#        qbtn.resize(qbtn.sizeHint())
#        qbtn.move(50,50)
#        self.setGeometry(300,300,450,150)
#        self.setWindowTitle('Quit button')
#        self.show()
#app = QApplication(sys.argv)
#ex = Example()
#sys.exit(app.exec_())




### message box
#class Example(QWidget):
#    def __init__(self):
#        super().__init__()
#        self.initUI()
#    def initUI(self):
#        self.setGeometry(300,300,450,300)
#        self.setWindowTitle("Message box")
#        self.show()
#    def closeEvent(self, event):
#        reply = QMessageBox.question(self, 'Message', 
#                "Are you sure you want to quit?", 
#                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
#        if reply == QMessageBox.Yes:
#            event.accept()
#        else:
#            event.ignore()
#app = QApplication(sys.argv)
#ex = Example()
#sys.exit(app.exec_())






### centering a window on the screen
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.resize(450, 300)
        self.center()
        self.setWindowTitle("Center")
        self.show()
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())

