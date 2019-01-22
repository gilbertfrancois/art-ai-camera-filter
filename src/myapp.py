from PySide2.QtWidgets import *


class MyApp(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setApplicationName("My Camera App")
        self.setApplicationVersion("0.1")


