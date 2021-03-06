# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 439)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(780, 780))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("font: 10pt \"Courier 10 Pitch\";\n"
"selection-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(213, 213, 212);\n"
"background-color: rgb(131, 45, 108);")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(13, 13, 611, 371))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.boton_modulo_coope = QtWidgets.QPushButton(self.layoutWidget)
        self.boton_modulo_coope.setMinimumSize(QtCore.QSize(121, 71))
        self.boton_modulo_coope.setMaximumSize(QtCore.QSize(121, 71))
        self.boton_modulo_coope.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 0, 0);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("iconos/limited_userv2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_modulo_coope.setIcon(icon)
        self.boton_modulo_coope.setObjectName("boton_modulo_coope")
        self.gridLayout.addWidget(self.boton_modulo_coope, 0, 3, 1, 1)
        self.boton_modulo_cargos = QtWidgets.QPushButton(self.layoutWidget)
        self.boton_modulo_cargos.setMinimumSize(QtCore.QSize(121, 71))
        self.boton_modulo_cargos.setMaximumSize(QtCore.QSize(121, 71))
        self.boton_modulo_cargos.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("iconos/calidad-de-la-pagina.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_modulo_cargos.setIcon(icon1)
        self.boton_modulo_cargos.setObjectName("boton_modulo_cargos")
        self.gridLayout.addWidget(self.boton_modulo_cargos, 3, 3, 1, 1)
        self.boton_modulo_reportes = QtWidgets.QPushButton(self.layoutWidget)
        self.boton_modulo_reportes.setMinimumSize(QtCore.QSize(121, 71))
        self.boton_modulo_reportes.setMaximumSize(QtCore.QSize(121, 71))
        self.boton_modulo_reportes.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 85, 255);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("iconos/herramientas-de-papel-y-lapiz.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_modulo_reportes.setIcon(icon2)
        self.boton_modulo_reportes.setObjectName("boton_modulo_reportes")
        self.gridLayout.addWidget(self.boton_modulo_reportes, 1, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("iconos/logotipo_dircoop.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 3, 3)
        self.boton_modulo_notas = QtWidgets.QPushButton(self.layoutWidget)
        self.boton_modulo_notas.setMinimumSize(QtCore.QSize(121, 71))
        self.boton_modulo_notas.setMaximumSize(QtCore.QSize(121, 71))
        self.boton_modulo_notas.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(85, 0, 127);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("iconos/casilla-y-boligrafo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_modulo_notas.setIcon(icon3)
        self.boton_modulo_notas.setObjectName("boton_modulo_notas")
        self.gridLayout.addWidget(self.boton_modulo_notas, 2, 3, 1, 1)
        self.boton_modulo_contable = QtWidgets.QPushButton(self.layoutWidget)
        self.boton_modulo_contable.setMinimumSize(QtCore.QSize(121, 71))
        self.boton_modulo_contable.setMaximumSize(QtCore.QSize(121, 71))
        self.boton_modulo_contable.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 180, 5);")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("iconos/maquina-de-facturacion-electronica-con-escaner.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_modulo_contable.setIcon(icon4)
        self.boton_modulo_contable.setObjectName("boton_modulo_contable")
        self.gridLayout.addWidget(self.boton_modulo_contable, 0, 2, 1, 1)
        self.boton_modulo_capital = QtWidgets.QPushButton(self.layoutWidget)
        self.boton_modulo_capital.setMinimumSize(QtCore.QSize(121, 71))
        self.boton_modulo_capital.setMaximumSize(QtCore.QSize(121, 71))
        self.boton_modulo_capital.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 0);")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("iconos/calculadora.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_modulo_capital.setIcon(icon5)
        self.boton_modulo_capital.setObjectName("boton_modulo_capital")
        self.gridLayout.addWidget(self.boton_modulo_capital, 0, 1, 1, 1)
        self.boton_modulo_asociados = QtWidgets.QPushButton(self.layoutWidget)
        self.boton_modulo_asociados.setMinimumSize(QtCore.QSize(121, 71))
        self.boton_modulo_asociados.setMaximumSize(QtCore.QSize(121, 71))
        self.boton_modulo_asociados.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"color: rgb(0, 0, 0);")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("iconos/silueta-masculina-de-usuario.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_modulo_asociados.setIcon(icon6)
        self.boton_modulo_asociados.setObjectName("boton_modulo_asociados")
        self.gridLayout.addWidget(self.boton_modulo_asociados, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 650, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuASOCIADO = QtWidgets.QMenu(self.menuBar)
        self.menuASOCIADO.setObjectName("menuASOCIADO")
        self.menuCAPITAL_SOCIAL = QtWidgets.QMenu(self.menuBar)
        self.menuCAPITAL_SOCIAL.setObjectName("menuCAPITAL_SOCIAL")
        self.menuCONTABLES = QtWidgets.QMenu(self.menuBar)
        self.menuCONTABLES.setObjectName("menuCONTABLES")
        self.menuDATOS_COOPERATIVA = QtWidgets.QMenu(self.menuBar)
        self.menuDATOS_COOPERATIVA.setObjectName("menuDATOS_COOPERATIVA")
        self.menuREPORTES = QtWidgets.QMenu(self.menuBar)
        self.menuREPORTES.setObjectName("menuREPORTES")
        self.menuNOTAS = QtWidgets.QMenu(self.menuBar)
        self.menuNOTAS.setObjectName("menuNOTAS")
        self.menuCONSEJO_DE_ADMINISTRAC_N = QtWidgets.QMenu(self.menuBar)
        self.menuCONSEJO_DE_ADMINISTRAC_N.setObjectName("menuCONSEJO_DE_ADMINISTRAC_N")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionALTA_ASOCIADO = QtWidgets.QAction(MainWindow)
        self.actionALTA_ASOCIADO.setIcon(icon6)
        self.actionALTA_ASOCIADO.setObjectName("actionALTA_ASOCIADO")
        self.actionACTUALIZACI_N_ASOCIADO = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("iconos/boton-actualizar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionACTUALIZACI_N_ASOCIADO.setIcon(icon7)
        self.actionACTUALIZACI_N_ASOCIADO.setObjectName("actionACTUALIZACI_N_ASOCIADO")
        self.actionBAJA_ASOCIADO = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("iconos/foto-principal-del-usuario.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBAJA_ASOCIADO.setIcon(icon8)
        self.actionBAJA_ASOCIADO.setObjectName("actionBAJA_ASOCIADO")
        self.actionBUSCAR_ASOCIADO = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("iconos/prismaticos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBUSCAR_ASOCIADO.setIcon(icon9)
        self.actionBUSCAR_ASOCIADO.setObjectName("actionBUSCAR_ASOCIADO")
        self.actionLISTA_DE_ASOCIADOS = QtWidgets.QAction(MainWindow)
        self.actionLISTA_DE_ASOCIADOS.setIcon(icon2)
        self.actionLISTA_DE_ASOCIADOS.setObjectName("actionLISTA_DE_ASOCIADOS")
        self.actionALTA_COOPERATIVA = QtWidgets.QAction(MainWindow)
        self.actionALTA_COOPERATIVA.setIcon(icon)
        self.actionALTA_COOPERATIVA.setObjectName("actionALTA_COOPERATIVA")
        self.actionACTUALIZACI_N_DATOS = QtWidgets.QAction(MainWindow)
        self.actionACTUALIZACI_N_DATOS.setIcon(icon7)
        self.actionACTUALIZACI_N_DATOS.setObjectName("actionACTUALIZACI_N_DATOS")
        self.actionMOVIMIENTOS = QtWidgets.QAction(MainWindow)
        self.actionMOVIMIENTOS.setIcon(icon4)
        self.actionMOVIMIENTOS.setObjectName("actionMOVIMIENTOS")
        self.actionMOVIMIENTOS_MENSUALES = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("iconos/documento-financiero.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMOVIMIENTOS_MENSUALES.setIcon(icon10)
        self.actionMOVIMIENTOS_MENSUALES.setObjectName("actionMOVIMIENTOS_MENSUALES")
        self.actionMOVIMIENTO_ANUAL = QtWidgets.QAction(MainWindow)
        self.actionMOVIMIENTO_ANUAL.setIcon(icon10)
        self.actionMOVIMIENTO_ANUAL.setObjectName("actionMOVIMIENTO_ANUAL")
        self.actionACTAS = QtWidgets.QAction(MainWindow)
        self.actionACTAS.setIcon(icon1)
        self.actionACTAS.setObjectName("actionACTAS")
        self.actionC_A = QtWidgets.QAction(MainWindow)
        self.actionC_A.setIcon(icon1)
        self.actionC_A.setObjectName("actionC_A")
        self.actionSINDICATURA = QtWidgets.QAction(MainWindow)
        self.actionSINDICATURA.setIcon(icon1)
        self.actionSINDICATURA.setObjectName("actionSINDICATURA")
        self.menuASOCIADO.addAction(self.actionALTA_ASOCIADO)
        self.menuASOCIADO.addAction(self.actionACTUALIZACI_N_ASOCIADO)
        self.menuCONTABLES.addAction(self.actionMOVIMIENTOS)
        self.menuDATOS_COOPERATIVA.addAction(self.actionALTA_COOPERATIVA)
        self.menuREPORTES.addAction(self.actionLISTA_DE_ASOCIADOS)
        self.menuREPORTES.addSeparator()
        self.menuREPORTES.addAction(self.actionMOVIMIENTOS_MENSUALES)
        self.menuNOTAS.addAction(self.actionACTAS)
        self.menuCONSEJO_DE_ADMINISTRAC_N.addAction(self.actionC_A)
        self.menuBar.addAction(self.menuASOCIADO.menuAction())
        self.menuBar.addAction(self.menuCAPITAL_SOCIAL.menuAction())
        self.menuBar.addAction(self.menuCONTABLES.menuAction())
        self.menuBar.addAction(self.menuDATOS_COOPERATIVA.menuAction())
        self.menuBar.addAction(self.menuREPORTES.menuAction())
        self.menuBar.addAction(self.menuNOTAS.menuAction())
        self.menuBar.addAction(self.menuCONSEJO_DE_ADMINISTRAC_N.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SISTEMA DE GESTIÓN COOPERATIVO"))
        self.boton_modulo_coope.setText(_translate("MainWindow", "COOPERATIVA"))
        self.boton_modulo_cargos.setText(_translate("MainWindow", "CARGOS"))
        self.boton_modulo_reportes.setText(_translate("MainWindow", "REPORTES"))
        self.boton_modulo_notas.setText(_translate("MainWindow", "NOTAS"))
        self.boton_modulo_contable.setText(_translate("MainWindow", "CONTABLE"))
        self.boton_modulo_capital.setText(_translate("MainWindow", "CAPITAL"))
        self.boton_modulo_asociados.setText(_translate("MainWindow", "ASOCIADOS"))
        self.menuASOCIADO.setTitle(_translate("MainWindow", "ASOCIADO"))
        self.menuCAPITAL_SOCIAL.setTitle(_translate("MainWindow", "CAP. SOCIAL"))
        self.menuCONTABLES.setTitle(_translate("MainWindow", "CONTABLES"))
        self.menuDATOS_COOPERATIVA.setTitle(_translate("MainWindow", "DATOS COOP."))
        self.menuREPORTES.setTitle(_translate("MainWindow", "REPORTES"))
        self.menuNOTAS.setTitle(_translate("MainWindow", "NOTAS"))
        self.menuCONSEJO_DE_ADMINISTRAC_N.setTitle(_translate("MainWindow", "NOMINA DE CARGOS"))
        self.actionALTA_ASOCIADO.setText(_translate("MainWindow", "ALTA ASOCIADO"))
        self.actionACTUALIZACI_N_ASOCIADO.setText(_translate("MainWindow", "ACTUALIZACIÓN ASOCIADO"))
        self.actionBAJA_ASOCIADO.setText(_translate("MainWindow", "BAJA ASOCIADO"))
        self.actionBUSCAR_ASOCIADO.setText(_translate("MainWindow", "BUSCAR ASOCIADO"))
        self.actionLISTA_DE_ASOCIADOS.setText(_translate("MainWindow", "LISTA DE ASOCIADOS"))
        self.actionALTA_COOPERATIVA.setText(_translate("MainWindow", "ALTA COOPERATIVA"))
        self.actionACTUALIZACI_N_DATOS.setText(_translate("MainWindow", "ACTUALIZACIÓN DATOS"))
        self.actionMOVIMIENTOS.setText(_translate("MainWindow", "COMPRAS Y VENTAS"))
        self.actionMOVIMIENTOS_MENSUALES.setText(_translate("MainWindow", "MOVIMIENTOS MENSUALES"))
        self.actionMOVIMIENTO_ANUAL.setText(_translate("MainWindow", "MOVIMIENTO ANUAL"))
        self.actionACTAS.setText(_translate("MainWindow", "ACTAS E INFORMES"))
        self.actionC_A.setText(_translate("MainWindow", "ABM CARGOS"))
        self.actionSINDICATURA.setText(_translate("MainWindow", "SINDICATURA"))

