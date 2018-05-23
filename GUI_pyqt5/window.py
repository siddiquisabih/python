import sys
from PyQt5 import QtWidgets


def window():
    app = QtWidgets.QApplication (sys.argv)
    w = QtWidgets.QWidget ()
    b = QtWidgets.QPushButton ('Push Me')

    l = QtWidgets.QLabel ('Hello world')
    v_box = QtWidgets.QVBoxLayout ()
    h_box = QtWidgets.QHBoxLayout ()
    h_box.addStretch()
    h_box.addWidget(l)
    h_box.addStretch()
    v_box.addWidget (b)
    v_box.addLayout(h_box)
    w.setLayout (v_box)
    w.setWindowTitle ('First Window')
    w.show ()
    sys.exit (app.exec_ ())


window ()


def clickasd ():
    print('abc')

