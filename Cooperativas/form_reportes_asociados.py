# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_reportes_asociados.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_reporte_asoc(object):
    def setupUi(self, form_reporte_asoc):
        form_reporte_asoc.setObjectName("form_reporte_asoc")
        form_reporte_asoc.resize(439, 141)
        form_reporte_asoc.setStyleSheet("font: 12pt \"Courier 10 Pitch\";\n"
"selection-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(170, 255, 127);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(117, 0, 88);")
        self.gridLayout_2 = QtWidgets.QGridLayout(form_reporte_asoc)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(form_reporte_asoc)
        self.tabWidget.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(226, 226, 226);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.dte_asoc_reporte = QtWidgets.QDateEdit(self.tab)
        self.dte_asoc_reporte.setMinimumSize(QtCore.QSize(0, 25))
        self.dte_asoc_reporte.setMaximumSize(QtCore.QSize(16777215, 25))
        self.dte_asoc_reporte.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dte_asoc_reporte.setObjectName("dte_asoc_reporte")
        self.horizontalLayout.addWidget(self.dte_asoc_reporte)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.boton_reporte_asoc_imprimir = QtWidgets.QPushButton(self.tab)
        self.boton_reporte_asoc_imprimir.setMinimumSize(QtCore.QSize(0, 25))
        self.boton_reporte_asoc_imprimir.setMaximumSize(QtCore.QSize(16777215, 25))
        self.boton_reporte_asoc_imprimir.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(140, 189, 58);")
        self.boton_reporte_asoc_imprimir.setObjectName("boton_reporte_asoc_imprimir")
        self.gridLayout.addWidget(self.boton_reporte_asoc_imprimir, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(form_reporte_asoc)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(form_reporte_asoc)

    def retranslateUi(self, form_reporte_asoc):
        _translate = QtCore.QCoreApplication.translate
        form_reporte_asoc.setWindowTitle(_translate("form_reporte_asoc", "Form"))
        self.label_2.setText(_translate("form_reporte_asoc", "Imprimir asociados activos al:"))
        self.dte_asoc_reporte.setDisplayFormat(_translate("form_reporte_asoc", "MM/yyyy"))
        self.boton_reporte_asoc_imprimir.setText(_translate("form_reporte_asoc", "Imprimir"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("form_reporte_asoc", "Reporte mensual de asociados"))

