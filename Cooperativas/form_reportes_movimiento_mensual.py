# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_reportes_movimiento_mensual.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_reportes_mensual(object):
    def setupUi(self, form_reportes_mensual):
        form_reportes_mensual.setObjectName("form_reportes_mensual")
        form_reportes_mensual.resize(399, 141)
        form_reportes_mensual.setStyleSheet("font: 12pt \"Courier 10 Pitch\";\n"
"selection-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(170, 255, 127);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(117, 0, 88);")
        self.gridLayout_2 = QtWidgets.QGridLayout(form_reportes_mensual)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(form_reportes_mensual)
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
        self.dte_fec_reporte_movs = QtWidgets.QDateEdit(self.tab)
        self.dte_fec_reporte_movs.setMinimumSize(QtCore.QSize(0, 25))
        self.dte_fec_reporte_movs.setMaximumSize(QtCore.QSize(16777215, 25))
        self.dte_fec_reporte_movs.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dte_fec_reporte_movs.setObjectName("dte_fec_reporte_movs")
        self.horizontalLayout.addWidget(self.dte_fec_reporte_movs)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.boton_imprimir_movs = QtWidgets.QPushButton(self.tab)
        self.boton_imprimir_movs.setMinimumSize(QtCore.QSize(0, 25))
        self.boton_imprimir_movs.setMaximumSize(QtCore.QSize(16777215, 25))
        self.boton_imprimir_movs.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(140, 189, 58);")
        self.boton_imprimir_movs.setObjectName("boton_imprimir_movs")
        self.gridLayout.addWidget(self.boton_imprimir_movs, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(form_reportes_mensual)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(form_reportes_mensual)

    def retranslateUi(self, form_reportes_mensual):
        _translate = QtCore.QCoreApplication.translate
        form_reportes_mensual.setWindowTitle(_translate("form_reportes_mensual", "Form"))
        self.label_2.setText(_translate("form_reportes_mensual", "Imprimir movimientos de:"))
        self.dte_fec_reporte_movs.setDisplayFormat(_translate("form_reportes_mensual", "MM/yyyy"))
        self.boton_imprimir_movs.setText(_translate("form_reportes_mensual", "Imprimir"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("form_reportes_mensual", "Reporte mensual"))

