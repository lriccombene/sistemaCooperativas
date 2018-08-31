import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox,QTableWidgetItem,QWidget
from PyQt5 import uic
from form_nomina_cargos import Ui_Form_nomina_cargos
from E_asociado import E_asociado
from E_party_party import E_party_party
from PyQt5.QtCore import pyqtRemoveInputHook
from E_cargos import E_cargos
from E_asociado import E_asociado

class nomina_cargos(QDialog):
    obj_form= Ui_Form_nomina_cargos()
    id_party=0
    id_asoc=0

    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_Form_nomina_cargos()
        self.obj_form.setupUi(self)
        self.obj_form.boton_cargo_buscar.clicked.connect(self.buscar_asoc)
        self.obj_form.boton_cargo_agregar.clicked.connect(self.cargo_agregar)
        self.obj_form.tw_nomina_cargos.cellClicked.connect(self.seleccion_item_tabla)

        obj_E_cargos = E_cargos()
        lista_cargos =  obj_E_cargos.get_grilla_form_cargos()
        for item in lista_cargos:
            rowPosition = self.obj_form.tw_nomina_cargos.rowCount()
            self.obj_form.tw_nomina_cargos.insertRow(rowPosition)
            self.obj_form.tw_nomina_cargos.setItem(rowPosition , 0, QTableWidgetItem(str(item.apellido)))
            self.obj_form.tw_nomina_cargos.setItem(rowPosition , 1, QTableWidgetItem(str(item.nro_doc)))
            self.obj_form.tw_nomina_cargos.setItem(rowPosition , 2, QTableWidgetItem(str(item.nro_asociado)))
            self.obj_form.tw_nomina_cargos.setItem(rowPosition , 3, QTableWidgetItem(str(item.cargo)))
            self.obj_form.tw_nomina_cargos.setItem(rowPosition , 4, QTableWidgetItem(str(item.fec_desde)))
            self.obj_form.tw_nomina_cargos.setItem(rowPosition , 5, QTableWidgetItem(str(item.fec_hasta)))
            self.obj_form.tw_nomina_cargos.setItem(rowPosition , 6, QTableWidgetItem(str(item.observacion)))
            self.obj_form.tw_nomina_cargos.setItem(rowPosition , 7, QTableWidgetItem(str(item.id)))


    def seleccion_item_tabla(self, clickedIndex):

        w = QWidget()
        result = QMessageBox.question(w, 'Alerta', " Desea eliminar el cargo?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        obj_E_cargos = E_cargos()
        if result == QMessageBox.Yes:
            pyqtRemoveInputHook()
            import pdb; pdb.set_trace()
            twi2 = self.obj_form.tw_nomina_cargos.item(clickedIndex, 7)
            obj_E_cargos.borrar_cargo(twi2.text())

        while (self.obj_form.tw_nomina_cargos.rowCount() > 0):
            self.obj_form.tw_nomina_cargos.removeRow(0)

        lista_cargos =  obj_E_cargos.get_grilla_form_cargos()
        for item in lista_cargos:
            rowPosition = self.obj_form.tw_nomina_cargos.rowCount()
            self.obj_form.tw_nomina_cargos.insertRow(rowPosition)
            self.obj_form.tw_nomina_cargos.setItem(rowPosition , 0, QTableWidgetItem(str(item.apellido)))
            self.obj_form.tw_nomina_cargos.setItem(rowPosition , 1, QTableWidgetItem(str(item.nro_doc)))
            self.obj_form.tw_nomina_cargos.setItem(rowPosition , 2, QTableWidgetItem(str(item.nro_asociado)))
            self.obj_form.tw_nomina_cargos.setItem(rowPosition , 3, QTableWidgetItem(str(item.cargo)))
            self.obj_form.tw_nomina_cargos.setItem(rowPosition , 4, QTableWidgetItem(str(item.fec_desde)))
            self.obj_form.tw_nomina_cargos.setItem(rowPosition , 5, QTableWidgetItem(str(item.fec_hasta)))
            self.obj_form.tw_nomina_cargos.setItem(rowPosition , 6, QTableWidgetItem(str(item.observacion)))
            self.obj_form.tw_nomina_cargos.setItem(rowPosition , 7, QTableWidgetItem(str(item.id)))


    def cargo_agregar(self):

        obj_E_asociado = E_asociado()
        obj_asociado = obj_E_asociado.get_E_asociado(self.id_party)

        obj_E_cargos = E_cargos()
        obj_E_cargos.id_asoc =obj_asociado.id
        obj_E_cargos.cargo = self.obj_form.cbx_cargo.currentText()
        obj_E_cargos.fec_desde = self.obj_form.dte_desde.text()
        obj_E_cargos.fec_hasta = self.obj_form.dte_hasta.text()
        obj_E_cargos.observacion =self.obj_form.lne_observacion.text()
        obj_cargo = obj_E_cargos.guardar(obj_E_cargos)
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        rowPosition = self.obj_form.tw_nomina_cargos.rowCount()
        self.obj_form.tw_nomina_cargos.insertRow(rowPosition)
        self.obj_form.tw_nomina_cargos.setItem(rowPosition , 0, QTableWidgetItem(self.obj_form.lne_apellido_nombre.text()))
        self.obj_form.tw_nomina_cargos.setItem(rowPosition , 1, QTableWidgetItem(self.obj_form.lne_nro_doc.text()))
        self.obj_form.tw_nomina_cargos.setItem(rowPosition , 2, QTableWidgetItem(self.obj_form.lne_nro_asoc.text()))
        self.obj_form.tw_nomina_cargos.setItem(rowPosition , 3, QTableWidgetItem(self.obj_form.cbx_cargo.currentText()))
        self.obj_form.tw_nomina_cargos.setItem(rowPosition , 4, QTableWidgetItem(self.obj_form.dte_desde.text()))
        self.obj_form.tw_nomina_cargos.setItem(rowPosition , 5, QTableWidgetItem(self.obj_form.dte_hasta.text()))
        self.obj_form.tw_nomina_cargos.setItem(rowPosition , 6, QTableWidgetItem(self.obj_form.lne_observacion.text()))
        self.obj_form.tw_nomina_cargos.setItem(rowPosition , 7, QTableWidgetItem(str(obj_cargo.id)))

    def buscar_asoc(self):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        obj_E_party =E_party_party()
        obj_party = ""
        if self.obj_form.lne_apellido.text() !="" :
            obj_party =obj_E_party.buscar_asoc_apellido(self.obj_form.lne_apellido.text())

        if self.obj_form.lne_cargo_nro_doc_buscar.text() !="" :
            obj_party =obj_E_party.buscar_asoc_dni(self.obj_form.lne_cargo_nro_doc_buscar.text())

        self.obj_form.lne_apellido_nombre.setText( obj_party.apellido+ ", " +obj_party.nombre)
        self.obj_form.lne_nro_doc.setText(obj_party.nro_doc)
        self.obj_form.dte_fec_nac.setDate(obj_party.fec_nac)
        index_tipo_doc=self.obj_form.cbx_tipo_doc.findText(str(obj_party.tipo_doc))
        self.obj_form.cbx_tipo_doc.setCurrentIndex(index_tipo_doc)

        obj_E_asociado = E_asociado()
        obj_asoc = obj_E_asociado.get_E_asociado(obj_party.id)
        self.obj_form.lne_nro_asoc.setText(obj_asoc.nro_asociado)
        self.id_party =obj_party.id




#app = QApplication(sys.argv)
#dialogo= nomina_cargos()
#dialogo.show()
#app.exec_()
