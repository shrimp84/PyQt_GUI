import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication,
        QAction, qApp,
        QMenu,
        QTextEdit)
from PyQt5.QtGui import QIcon

### Status Bar
#class Example(QMainWindow):
#    def __init__(self):
#        super().__init__()
#        self.initUI()
#    def initUI(self):
#        self.statusBar().showMessage("Ready")
#        self.setGeometry(300,300,450,150)
#        self.setWindowTitle("Status Bar")
#        self.show()
#app = QApplication(sys.argv)
#ex = Example()
#sys.exit(app.exec_())





### Simple Menu
#class Example(QMainWindow):
#    def __init__(self):
#        super().__init__()
#        self.initUI()
#    def initUI(self):
#        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
#        exitAct.setShortcut('Ctrl+Q')
#        exitAct.setStatusTip('Exit Application')
#        exitAct.triggered.connect(qApp.quit)
#
#        self.statusBar()
#
#        menubar = self.menuBar()
#        fileMenu = menubar.addMenu("&File")
#        fileMenu.addAction(exitAct)
#
#        self.setGeometry(300,300,300,200)
#        self.setWindowTitle('Simple Menu')
#        self.show()
#app = QApplication(sys.argv)
#ex = Example()
#sys.exit(app.exec_())




### Submenu
#class Example(QMainWindow):
#    def __init__(self):
#        super().__init__()
#        self.initUI()
#    def initUI(self):
#        menubar = self.menuBar()
#        fileMenu = menubar.addMenu('File')
#
#        impMenu = QMenu('Import', self)
#        impAct = QAction('Import Mail', self)
#        impMenu.addAction(impAct)
#
#        newAct = QAction('New', self)
#
#        fileMenu.addAction(newAct)
#        fileMenu.addMenu(impMenu)
#
#        self.setGeometry(300,300,300,300)
#        self.setWindowTitle('Submenu')
#        self.show()
#app = QApplication(sys.argv)
#ex = Example()
#sys.exit(app.exec_())




### Check Menu
#class Example(QMainWindow):
#    def __init__(self):
#        super().__init__()
#        self.initUI()
#    def initUI(self):
#        self.statusbar = self.statusBar()
#        self.statusbar.showMessage('Ready') 
#        menubar = self.menuBar()
#        viewMenu = menubar.addMenu('View')
#
#        viewStatAct = QAction('View status bar', self, checkable = True)
#        viewStatAct.setStatusTip('View status bar')
#        viewStatAct.setChecked(True)
#        viewStatAct.triggered.connect(self.toggleMenu)
#
#        viewMenu.addAction(viewStatAct)
#
#        self.setGeometry(300,300,450,250)
#        self.setWindowTitle("Check Menu")
#        self.show()
#    def toggleMenu(self, state):
#        if state:
#            self.statusbar.show()
#        else:
#            self.statusbar.hide()
#app = QApplication(sys.argv)
#ex = Example()
#sys.exit(app.exec_())





### context menu
#class Example(QMainWindow):
#    def __init__(self):
#        super().__init__()
#        self.initUI()
#    def initUI(self):
#        self.setGeometry(300,300,500,300)
#        self.setWindowTitle('Context menu')
#        self.show()
#    def contextMenuEvent(self, event):
#        cmenu = QMenu(self)
#        newAct = cmenu.addAction("New")
#        opnAct = cmenu.addAction("Open")
#        quitAct = cmenu.addAction("Quit")
#        action = cmenu.exec_(self.mapToGlobal(event.pos()))
#
#        if action == quitAct:
#            qApp.quit()
#
#if __name__ == '__main__':
#    app = QApplication(sys.argv)
#    ex = Example()
#    sys.exit(app.exec_())





### toolbar
#class Example(QMainWindow):
#    def __init__(self):
#        super().__init__()
#        self.initUI()
#    def initUI(self):
#        exitAct = QAction(QIcon('exit.png'), 'Exit', self)
#        exitAct.setShortcut('Ctrl+Q')
#        exitAct.triggered.connect(qApp.quit)
#
#        self.toolbar = self.addToolBar('Exit')
#        self.toolbar.addAction(exitAct)
#
#        self.setGeometry(300,300,400,300)
#        self.setWindowTitle('Toolbar')
#        self.show()
#app = QApplication(sys.argv)
#ex = Example()
#sys.exit(app.exec_())





### Putting it all together
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAct = QAction(QIcon('exit.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit Application')
        exitAct.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(exitAct)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAct)

        self.setGeometry(300,300,400,400)
        self.setWindowTitle('Main Window')
        self.show()
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())

