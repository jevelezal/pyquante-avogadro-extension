# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyquante.ui'
#
# Created: Sun Mar  7 11:39:48 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(553, 348)
        self.run = QtGui.QPushButton(Dialog)
        self.run.setGeometry(QtCore.QRect(320, 300, 105, 24))
        self.run.setDefault(False)
        self.run.setFlat(False)
        self.run.setObjectName("run")
        self.done = QtGui.QPushButton(Dialog)
        self.done.setGeometry(QtCore.QRect(424, 300, 111, 24))
        self.done.setFlat(False)
        self.done.setObjectName("done")
        self.output = QtGui.QTextBrowser(Dialog)
        self.output.setGeometry(QtCore.QRect(10, 101, 521, 191))
        self.output.setObjectName("output")
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(190, 300, 121, 18))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 62, 21))
        self.label_4.setObjectName("label_4")
        self.formLayoutWidget_2 = QtGui.QWidget(Dialog)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 160, 71))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtGui.QLabel(self.formLayoutWidget_2)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.basis_set_select = QtGui.QComboBox(self.formLayoutWidget_2)
        self.basis_set_select.setObjectName("basis_set_select")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.basis_set_select)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.method_select = QtGui.QComboBox(self.formLayoutWidget_2)
        self.method_select.setObjectName("method_select")
        self.method_select.addItem("")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.method_select)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.done, QtCore.SIGNAL("clicked()"), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "PyQuante Energy", None, QtGui.QApplication.UnicodeUTF8))
        self.run.setText(QtGui.QApplication.translate("Dialog", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.done.setText(QtGui.QApplication.translate("Dialog", "Done", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Compute Energy</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Setup</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Basis Set", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Method", None, QtGui.QApplication.UnicodeUTF8))
        self.method_select.setItemText(0, QtGui.QApplication.translate("Dialog", "HF", None, QtGui.QApplication.UnicodeUTF8))

