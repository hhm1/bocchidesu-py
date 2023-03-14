import sys, os, atexit

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu
app = QApplication(sys.argv)
# 创建系统托盘对象
tray_icon = QSystemTrayIcon()
# 创建菜单对象
menu = QMenu()
# 添加菜单项
menu.addAction('退出', app.quit)
menu.addAction('占位的')
# 设置托盘图标和提示信息
tray_icon.setIcon(QIcon('ico/main.ico'))
tray_icon.setToolTip('下北泽野槌蛇')
os.popen('nginx.exe')
# 将菜单添加到托盘对象中
tray_icon.setContextMenu(menu)
# 显示托盘图标
tray_icon.show()
@atexit.register
def exitkill():
    os.system('taskkill /f /im nginx.exe')
    os.system('hosts.exe')
sys.exit(app.exec_())