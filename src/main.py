import sys

from mainwindow import MainWindow
from myapp import MyApp

if __name__ == '__main__':
    app = MyApp(sys.argv)
    mainWin = MainWindow()
    # mainWin.setWindowTitle("my App")
    mainWin.show()

    ret = app.exec_()
    sys.exit(ret)
