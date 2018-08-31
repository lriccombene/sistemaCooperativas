import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox,QTableWidgetItem,QWidget
from PyQt5 import uic
from form_cooperativa_alta import Ui_form_cooperativa_alta
from E_cooperativa import E_cooperativa
from E_cooperativa_address import E_cooperativa_address
from PyQt5.QtCore import pyqtRemoveInputHook

class cooperativa_alta(QDialog):
    obj_form= Ui_form_cooperativa_alta()
    id_party=0
    id_asoc=0
    id=""

    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_form_cooperativa_alta()
        self.obj_form.setupUi(self)
        self.obj_form.boton_coope_guardar.clicked.connect(self.coope_guardar)
        self.obj_form.boton_coope_actualizar.clicked.connect(self.coope_actualizar)
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        obj_e_cooperativa = E_cooperativa()
        obj_e_cooperativa = obj_e_cooperativa.get_cooperativa()

        try:
            self.id = obj_e_cooperativa.id
        except :
            self.id=""

        if self.id != "" :
            self.obj_form.lne_denominacion.setText(obj_e_cooperativa.denominacion)
            self.obj_form.lne_nro_matricula.setText(str(obj_e_cooperativa.matricula))
            self.obj_form.lne_nro_reg_prov.setText(str(obj_e_cooperativa.nro_reg_prov))
            self.obj_form.dte_inicio_actividades.setDate(obj_e_cooperativa.fec)
            self.obj_form.lne_coope_cuit.setText(str(obj_e_cooperativa.cuit))

            obj_coop_address = E_cooperativa_address()
            obj_E_cooperativa_address = obj_coop_address.get_coop_address()
            self.obj_form.lne_coope_domicilio.setText(obj_E_cooperativa_address.domicilio)
            self.obj_form.lne_coope_piso.setText(obj_E_cooperativa_address.piso)
            self.obj_form.lne_coope_nro_dom.setText(obj_E_cooperativa_address.nro)
            self.obj_form.lne_coope_c_postal.setText(obj_E_cooperativa_address.cp)
            self.obj_form.lne_coope_localidad.setText(obj_E_cooperativa_address.localidad)
            self.obj_form.lne_coope_provincia.setText(obj_E_cooperativa_address.provincia)
            self.obj_form.lne_coope_telefono.setText(obj_E_cooperativa_address.telefono)
            self.obj_form.lne_coope_email.setText(obj_E_cooperativa_address.email)
            self.obj_form.lne_cap_obliga.setText(str(obj_e_cooperativa.pesos_obliga))
            self.obj_form.lne_cant_cuotas.setText(str(obj_e_cooperativa.cant_cta_obliga))


    def coope_actualizar(self):
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            obj_e_cooperativa = E_cooperativa()
            obj_e_cooperativa.denominacion = self.obj_form.lne_denominacion.text()
            obj_e_cooperativa.matricula = self.obj_form.lne_nro_matricula.text()
            obj_e_cooperativa.nro_reg_prov = self.obj_form.lne_nro_reg_prov.text()
            obj_e_cooperativa.fec = self.obj_form.dte_inicio_actividades.text()
            obj_e_cooperativa.cuit = self.obj_form.lne_coope_cuit.text()
            obj_e_cooperativa.pesos_obliga = self.obj_form.lne_cap_obliga.text()
            obj_e_cooperativa.cant_cta_obliga = self.obj_form.lne_cant_cuotas.text()
            obj_e_cooperativa.actualizar(obj_e_cooperativa)

            obj_coop = obj_e_cooperativa.get_cooperativa()
            obj_E_cooperativa_address = E_cooperativa_address()
            obj_E_cooperativa_address.id_cooperativa = obj_coop.id
            obj_E_cooperativa_address.domicilio = self.obj_form.lne_coope_domicilio.text()
            obj_E_cooperativa_address.piso =self.obj_form.lne_coope_piso.text()
            obj_E_cooperativa_address.nro = self.obj_form.lne_coope_nro_dom.text()
            obj_E_cooperativa_address.cp = self.obj_form.lne_coope_c_postal.text()
            obj_E_cooperativa_address.localidad = self.obj_form.lne_coope_localidad.text()
            obj_E_cooperativa_address.provincia = self.obj_form.lne_coope_provincia.text()
            obj_E_cooperativa_address.telefono = self.obj_form.lne_coope_telefono.text()
            obj_E_cooperativa_address.email = self.obj_form.lne_coope_email.text()
            obj_E_cooperativa_address.actualizar(obj_E_cooperativa_address)


    def coope_guardar(self):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        if self.id == "":
            obj_e_cooperativa = E_cooperativa()
            obj_e_cooperativa.denominacion = self.obj_form.lne_denominacion.text()
            obj_e_cooperativa.matricula = self.obj_form.lne_nro_matricula.text()
            obj_e_cooperativa.nro_reg_prov = self.obj_form.lne_nro_reg_prov.text()
            obj_e_cooperativa.fec = self.obj_form.dte_inicio_actividades.text()
            obj_e_cooperativa.cuit = self.obj_form.lne_coope_cuit.text()
            obj_e_cooperativa.pesos_obliga = self.obj_form.lne_cap_obliga.text()
            obj_e_cooperativa.cant_cta_obliga = self.obj_form.lne_cant_cuotas.text()
            obj_e_cooperativa.guardar(obj_e_cooperativa)

            obj_coop = obj_e_cooperativa.get_cooperativa()
            obj_E_cooperativa_address = E_cooperativa_address()
            obj_E_cooperativa_address.id_cooperativa = obj_coop.id
            obj_E_cooperativa_address.domicilio = self.obj_form.lne_coope_domicilio.text()
            obj_E_cooperativa_address.piso =self.obj_form.lne_coope_piso.text()
            obj_E_cooperativa_address.nro = self.obj_form.lne_coope_nro_dom.text()
            obj_E_cooperativa_address.cp = self.obj_form.lne_coope_c_postal.text()
            obj_E_cooperativa_address.localidad = self.obj_form.lne_coope_localidad.text()
            obj_E_cooperativa_address.provincia = self.obj_form.lne_coope_provincia.text()
            obj_E_cooperativa_address.telefono = self.obj_form.lne_coope_telefono.text()
            obj_E_cooperativa_address.email = self.obj_form.lne_coope_email.text()
            obj_E_cooperativa_address.guardar(obj_E_cooperativa_address)

            msgBox = QMessageBox()
            msgBox.setWindowTitle("Todo OK")
            msgBox.setText( 'Se guardaron los datos correctamente.')
            msgBox.exec_()



#app = QApplication(sys.argv)
#dialogo= cooperativa_alta()
#dialogo.show()
#app.exec_()
