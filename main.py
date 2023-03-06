import ctypes
import sys
import bocchidesu

from PyQt5.QtWidgets import QApplication, QMainWindow

from maindebug import MyMainWindow


def is_admin():
    """

    :return:
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    MyMainWindow()

else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)


class MyMainWindow(QMainWindow):
    def __init__(self, parent=None, layout=None, main_window=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

    if __name__ == "__main__":
        app = QApplication(sys.argv)
        myWin = MyMainWindow()
        myWin.show()
        sys.exit(app.exec_())
