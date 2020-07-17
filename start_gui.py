
def gui(str_):
    import sys
    from PyQt5 import QtCore, QtGui, QtWidgets

    from gui import Ui_MainWindow

    # create app
    app = QtWidgets.QApplication(sys.argv)

    # init
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # logic
    ui.Interface_list.setText(str_)

    # main loop
    sys.exit(app.exec_())
