import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

import bocchidesu


class MyMainWindow(QMainWindow, bocchidesu.Ui_Bocchidesu):

    def __init__(self, parent=None, layout=None, main_window=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
