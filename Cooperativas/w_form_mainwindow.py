import sys,datetime
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem,QMainWindow
from mainwindow import Ui_MainWindow
from PyQt5 import uic
from PyQt5.QtCore import pyqtRemoveInputHook
from PyQt5.QtWidgets import QFileDialog

#from w_form_asociado_actualizar import asociado_actualizar
#from w_form_asociado_alta import asociado_alta
#from w_form_cooperativa_alta import cooperativa_alta
from w_form_movimientos import movimientos
from w_form_cooperativa_alta import cooperativa_alta
from w_form_asociado_alta import asociado_alta
from w_form_asociado_actualizar import asociado_actualizar
from w_form_nomina_cargos import nomina_cargos
from w_form_notas import notas
from w_form_reporte_asoc import reporte_asoc



class Mainwindow(QMainWindow):
    def __init__(self):
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        self.obj_form_main = Ui_MainWindow()
        self.obj_form_main.setupUi(self)
        self.obj_form_main.actionALTA_ASOCIADO.triggered.connect(self.ALTA_ASOCIADO)
        self.obj_form_main.actionACTUALIZACI_N_ASOCIADO.triggered.connect(self.ACTUALIZACI_N_ASOCIADO)
        self.obj_form_main.actionMOVIMIENTOS.triggered.connect(self.MOVIMIENTOS)
        self.obj_form_main.actionALTA_COOPERATIVA.triggered.connect(self.ALTA_COOPERATIVA)
        self.obj_form_main.actionC_A.triggered.connect(self.nomina_cargos)
        self.obj_form_main.actionACTAS.triggered.connect(self.ACTAS)
        self.obj_form_main.boton_modulo_asociados.clicked.connect(self.ALTA_ASOCIADO)
        self.obj_form_main.boton_modulo_capital.clicked.connect(self.ACTUALIZACI_N_ASOCIADO)
        self.obj_form_main.boton_modulo_contable.clicked.connect(self.MOVIMIENTOS)
        self.obj_form_main.boton_modulo_coope.clicked.connect(self.ALTA_COOPERATIVA)
        self.obj_form_main.boton_modulo_notas.clicked.connect(self.ACTAS)
        self.obj_form_main.boton_modulo_cargos.clicked.connect(self.nomina_cargos)
        self.obj_form_main.actionLISTA_DE_ASOCIADOS.triggered.connect(self.LISTA_DE_ASOCIADOS)



    def LISTA_DE_ASOCIADOS(self):
        self.obj_reporte_asoc= reporte_asoc()
        self.obj_reporte_asoc.show()


    def ACTAS(self):
        self.notas= notas()
        self.notas.show()

    def nomina_cargos(self):
        self.nomina_cargos = nomina_cargos()
        self.nomina_cargos.show()

    def ALTA_COOPERATIVA(self):
        self.cooperativa_alta = cooperativa_alta()
        self.cooperativa_alta.show()


    def MOVIMIENTOS(self):
        self.form_movimientos = movimientos()
        self.form_movimientos.show()

    def ALTA_ASOCIADO(self):

        self.form_asociado_alta = asociado_alta()
        self.form_asociado_alta.show()

    def ACTUALIZACI_N_ASOCIADO(self):

        self.form_creditos_refinanciar = asociado_actualizar()
        self.form_creditos_refinanciar.show()



app = QApplication(sys.argv)
dialogo= Mainwindow()
dialogo.show()
app.exec_()
