# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_nomina_cargos.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_nomina_cargos(object):
    def setupUi(self, Form_nomina_cargos):
        Form_nomina_cargos.setObjectName("Form_nomina_cargos")
        Form_nomina_cargos.resize(695, 607)
        Form_nomina_cargos.setStyleSheet("font: 12pt \"Courier 10 Pitch\";\n"
"selection-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(170, 255, 127);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(117, 0, 88);")
        self.gridLayout_2 = QtWidgets.QGridLayout(Form_nomina_cargos)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(Form_nomina_cargos)
        self.tabWidget.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(226, 226, 226);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lne_apellido = QtWidgets.QLineEdit(self.tab)
        self.lne_apellido.setMinimumSize(QtCore.QSize(250, 25))
        self.lne_apellido.setMaximumSize(QtCore.QSize(250, 25))
        self.lne_apellido.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_apellido.setObjectName("lne_apellido")
        self.horizontalLayout.addWidget(self.lne_apellido)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.boton_cargo_buscar = QtWidgets.QPushButton(self.tab)
        self.boton_cargo_buscar.setMinimumSize(QtCore.QSize(100, 25))
        self.boton_cargo_buscar.setMaximumSize(QtCore.QSize(100, 25))
        self.boton_cargo_buscar.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(140, 189, 58);")
        self.boton_cargo_buscar.setObjectName("boton_cargo_buscar")
        self.horizontalLayout.addWidget(self.boton_cargo_buscar)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lne_cargo_nro_doc_buscar = QtWidgets.QLineEdit(self.tab)
        self.lne_cargo_nro_doc_buscar.setMinimumSize(QtCore.QSize(0, 25))
        self.lne_cargo_nro_doc_buscar.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lne_cargo_nro_doc_buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_cargo_nro_doc_buscar.setObjectName("lne_cargo_nro_doc_buscar")
        self.horizontalLayout_2.addWidget(self.lne_cargo_nro_doc_buscar)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lne_nro_asoc = QtWidgets.QLineEdit(self.tab)
        self.lne_nro_asoc.setMinimumSize(QtCore.QSize(0, 25))
        self.lne_nro_asoc.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lne_nro_asoc.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_nro_asoc.setObjectName("lne_nro_asoc")
        self.horizontalLayout_3.addWidget(self.lne_nro_asoc)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lne_apellido_nombre = QtWidgets.QLineEdit(self.tab)
        self.lne_apellido_nombre.setMinimumSize(QtCore.QSize(0, 25))
        self.lne_apellido_nombre.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lne_apellido_nombre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_apellido_nombre.setObjectName("lne_apellido_nombre")
        self.horizontalLayout_4.addWidget(self.lne_apellido_nombre)
        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.cbx_tipo_doc = QtWidgets.QComboBox(self.tab)
        self.cbx_tipo_doc.setMinimumSize(QtCore.QSize(0, 25))
        self.cbx_tipo_doc.setMaximumSize(QtCore.QSize(16777215, 25))
        self.cbx_tipo_doc.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cbx_tipo_doc.setObjectName("cbx_tipo_doc")
        self.cbx_tipo_doc.addItem("")
        self.cbx_tipo_doc.addItem("")
        self.cbx_tipo_doc.addItem("")
        self.cbx_tipo_doc.addItem("")
        self.horizontalLayout_5.addWidget(self.cbx_tipo_doc)
        self.lne_nro_doc = QtWidgets.QLineEdit(self.tab)
        self.lne_nro_doc.setMinimumSize(QtCore.QSize(0, 25))
        self.lne_nro_doc.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lne_nro_doc.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_nro_doc.setText("")
        self.lne_nro_doc.setObjectName("lne_nro_doc")
        self.horizontalLayout_5.addWidget(self.lne_nro_doc)
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.dte_fec_nac = QtWidgets.QDateEdit(self.tab)
        self.dte_fec_nac.setMinimumSize(QtCore.QSize(0, 25))
        self.dte_fec_nac.setMaximumSize(QtCore.QSize(16777215, 25))
        self.dte_fec_nac.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dte_fec_nac.setObjectName("dte_fec_nac")
        self.horizontalLayout_5.addWidget(self.dte_fec_nac)
        self.gridLayout.addLayout(self.horizontalLayout_5, 5, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.tab)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 6, 0, 1, 2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.cbx_cargo = QtWidgets.QComboBox(self.tab)
        self.cbx_cargo.setMinimumSize(QtCore.QSize(0, 25))
        self.cbx_cargo.setMaximumSize(QtCore.QSize(16777215, 25))
        self.cbx_cargo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cbx_cargo.setObjectName("cbx_cargo")
        self.cbx_cargo.addItem("")
        self.cbx_cargo.addItem("")
        self.cbx_cargo.addItem("")
        self.cbx_cargo.addItem("")
        self.cbx_cargo.addItem("")
        self.cbx_cargo.addItem("")
        self.cbx_cargo.addItem("")
        self.horizontalLayout_6.addWidget(self.cbx_cargo)
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.dte_desde = QtWidgets.QDateEdit(self.tab)
        self.dte_desde.setMinimumSize(QtCore.QSize(0, 25))
        self.dte_desde.setMaximumSize(QtCore.QSize(16777215, 25))
        self.dte_desde.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dte_desde.setObjectName("dte_desde")
        self.horizontalLayout_6.addWidget(self.dte_desde)
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.dte_hasta = QtWidgets.QDateEdit(self.tab)
        self.dte_hasta.setMinimumSize(QtCore.QSize(0, 25))
        self.dte_hasta.setMaximumSize(QtCore.QSize(16777215, 25))
        self.dte_hasta.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dte_hasta.setObjectName("dte_hasta")
        self.horizontalLayout_6.addWidget(self.dte_hasta)
        self.gridLayout.addLayout(self.horizontalLayout_6, 7, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.lne_observacion = QtWidgets.QLineEdit(self.tab)
        self.lne_observacion.setMinimumSize(QtCore.QSize(400, 50))
        self.lne_observacion.setMaximumSize(QtCore.QSize(400, 50))
        self.lne_observacion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lne_observacion.setText("")
        self.lne_observacion.setObjectName("lne_observacion")
        self.horizontalLayout_7.addWidget(self.lne_observacion)
        self.gridLayout.addLayout(self.horizontalLayout_7, 8, 0, 1, 1)
        self.boton_cargo_agregar = QtWidgets.QPushButton(self.tab)
        self.boton_cargo_agregar.setMinimumSize(QtCore.QSize(100, 25))
        self.boton_cargo_agregar.setMaximumSize(QtCore.QSize(100, 25))
        self.boton_cargo_agregar.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(140, 189, 58);")
        self.boton_cargo_agregar.setObjectName("boton_cargo_agregar")
        self.gridLayout.addWidget(self.boton_cargo_agregar, 8, 1, 1, 1)
        self.tw_nomina_cargos = QtWidgets.QTableWidget(self.tab)
        self.tw_nomina_cargos.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tw_nomina_cargos.setObjectName("tw_nomina_cargos")
        self.tw_nomina_cargos.setColumnCount(8)
        self.tw_nomina_cargos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(177, 215, 154))
        self.tw_nomina_cargos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(177, 215, 154))
        self.tw_nomina_cargos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(177, 215, 154))
        self.tw_nomina_cargos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(177, 215, 154))
        self.tw_nomina_cargos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(177, 215, 154))
        self.tw_nomina_cargos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(177, 215, 154))
        self.tw_nomina_cargos.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(177, 215, 154))
        self.tw_nomina_cargos.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(177, 215, 154))
        self.tw_nomina_cargos.setHorizontalHeaderItem(7, item)
        self.tw_nomina_cargos.horizontalHeader().setDefaultSectionSize(150)
        self.gridLayout.addWidget(self.tw_nomina_cargos, 9, 0, 1, 2)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Form_nomina_cargos)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form_nomina_cargos)

    def retranslateUi(self, Form_nomina_cargos):
        _translate = QtCore.QCoreApplication.translate
        Form_nomina_cargos.setWindowTitle(_translate("Form_nomina_cargos", "Form"))
        self.label.setText(_translate("Form_nomina_cargos", "Apellido :"))
        self.boton_cargo_buscar.setText(_translate("Form_nomina_cargos", "Buscar"))
        self.label_2.setText(_translate("Form_nomina_cargos", "N° Documento:"))
        self.label_3.setText(_translate("Form_nomina_cargos", "N° asociado:"))
        self.label_4.setText(_translate("Form_nomina_cargos", "Apellido y nombre:"))
        self.label_6.setText(_translate("Form_nomina_cargos", "Documento:"))
        self.cbx_tipo_doc.setItemText(0, _translate("Form_nomina_cargos", "DNI"))
        self.cbx_tipo_doc.setItemText(1, _translate("Form_nomina_cargos", "LC"))
        self.cbx_tipo_doc.setItemText(2, _translate("Form_nomina_cargos", "LE"))
        self.cbx_tipo_doc.setItemText(3, _translate("Form_nomina_cargos", "CI"))
        self.label_7.setText(_translate("Form_nomina_cargos", "Fecha nacimiento:"))
        self.dte_fec_nac.setDisplayFormat(_translate("Form_nomina_cargos", "dd/MM/yyyy"))
        self.label_5.setText(_translate("Form_nomina_cargos", "Cargo:"))
        self.cbx_cargo.setItemText(0, _translate("Form_nomina_cargos", "Presidente"))
        self.cbx_cargo.setItemText(1, _translate("Form_nomina_cargos", "Vicepresidente"))
        self.cbx_cargo.setItemText(2, _translate("Form_nomina_cargos", "Secretario/a"))
        self.cbx_cargo.setItemText(3, _translate("Form_nomina_cargos", "Tesorero/a"))
        self.cbx_cargo.setItemText(4, _translate("Form_nomina_cargos", "Síndico Titular"))
        self.cbx_cargo.setItemText(5, _translate("Form_nomina_cargos", "Síndico Suplente"))
        self.cbx_cargo.setItemText(6, _translate("Form_nomina_cargos", "Vocal 1°"))
        self.label_8.setText(_translate("Form_nomina_cargos", "Desde:"))
        self.dte_desde.setDisplayFormat(_translate("Form_nomina_cargos", "dd/MM/yyyy"))
        self.label_9.setText(_translate("Form_nomina_cargos", "Hasta:"))
        self.dte_hasta.setDisplayFormat(_translate("Form_nomina_cargos", "dd/MM/yyyy"))
        self.label_10.setText(_translate("Form_nomina_cargos", "Observaciones:"))
        self.boton_cargo_agregar.setText(_translate("Form_nomina_cargos", "Agregar"))
        item = self.tw_nomina_cargos.horizontalHeaderItem(0)
        item.setText(_translate("Form_nomina_cargos", "Apellido y nombre"))
        item = self.tw_nomina_cargos.horizontalHeaderItem(1)
        item.setText(_translate("Form_nomina_cargos", "DNI"))
        item = self.tw_nomina_cargos.horizontalHeaderItem(2)
        item.setText(_translate("Form_nomina_cargos", "N° asociado"))
        item = self.tw_nomina_cargos.horizontalHeaderItem(3)
        item.setText(_translate("Form_nomina_cargos", "Cargo"))
        item = self.tw_nomina_cargos.horizontalHeaderItem(4)
        item.setText(_translate("Form_nomina_cargos", "Desde"))
        item = self.tw_nomina_cargos.horizontalHeaderItem(5)
        item.setText(_translate("Form_nomina_cargos", "Hasta"))
        item = self.tw_nomina_cargos.horizontalHeaderItem(6)
        item.setText(_translate("Form_nomina_cargos", "Observaciones"))
        item = self.tw_nomina_cargos.horizontalHeaderItem(7)
        item.setText(_translate("Form_nomina_cargos", "ID"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form_nomina_cargos", "Cargar cargos"))

