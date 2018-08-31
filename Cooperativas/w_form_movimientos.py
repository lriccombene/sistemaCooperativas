import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox,QTableWidgetItem,QWidget
from PyQt5 import uic
from form_movimientos import Ui_form_movimientos
from PyQt5.QtCore import pyqtRemoveInputHook
from E_movimientos import E_movimientos

class movimientos(QDialog):
    obj_form= Ui_form_movimientos()


    def __init__(self):
        QDialog.__init__(self)
        self.obj_form= Ui_form_movimientos()
        self.obj_form.setupUi(self)
        self.obj_form.boton_compras.clicked.connect(self.compras)
        self.obj_form.boton_ventas.clicked.connect(self.ventas)


    def ventas(self):
        obj_movimientos = E_movimientos()
        obj_movimientos.nro_factura = self.obj_form.lne_ventas_nro_fact.text()
        obj_movimientos.total = self.obj_form.lne_ventas_total.text()
        obj_movimientos.concepto = self.obj_form.cbx_ventas_concepto.currentText()
        obj_movimientos.detalle = self.obj_form.textEdit_ventas.toPlainText()
        obj_movimientos.fecha = self.obj_form.dte_ventas_fec_fact.text()
        if self.obj_form.ckbx_ventas_coniva.isChecked() != True:
            obj_movimientos.iva = True
        else:
            obj_movimientos.iva = False
        obj_movimientos.tipo = "VENTAS"
        obj_movimientos.guardar(obj_movimientos)

    def compras(self):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        obj_movimientos = E_movimientos()
        obj_movimientos.nro_factura = self.obj_form.lne_compras_nro_fact.text()
        obj_movimientos.total = self.obj_form.lne_compras_total.text()
        obj_movimientos.concepto = self.obj_form.cbx_compras_concepto.currentText()
        obj_movimientos.detalle = self.obj_form.textEdit_compras.toPlainText()
        obj_movimientos.fecha = self.obj_form.dte_compras_fec_factura.text()
        if self.obj_form.ckbx_compras_coniva.isChecked() != True:
            obj_movimientos.iva = True
        else:
            obj_movimientos.iva = False
        obj_movimientos.tipo = "COMPRAS"
        obj_movimientos.guardar(obj_movimientos)


#app = QApplication(sys.argv)
#dialogo= movimientos()
#dialogo.show()
#app.exec_()
