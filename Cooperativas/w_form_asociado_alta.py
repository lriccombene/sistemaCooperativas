import sys,datetime
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox,QTableWidgetItem
from PyQt5 import uic
from PyQt5.QtCore import pyqtRemoveInputHook
from E_party_party import E_party_party
from E_party_address import E_party_address
from E_party_contact import E_party_contact
from E_asociado import E_asociado
from E_capital_integracion import E_capital_integracion
from E_observaciones import E_observaciones
from E_capitalizacion import E_capitalizacion
from E_capital_suscripto import E_capital_suscripto
from form_asociado_alta import Ui_form_asociado_alta
from E_cooperativa import E_cooperativa



class asociado_alta(QDialog):
    obj_form= Ui_form_asociado_alta()
    id_party=0
    id_asoc=0

    def __init__(self):
        QDialog.__init__(self)
        obj_form= Ui_form_asociado_alta()
        self.obj_form.setupUi(self)
        self.obj_form.boton_guardar_datos_personales.clicked.connect(self.guardar_datos_personales)
        self.obj_form.boton_guardar_cap_suscripto.clicked.connect(self.guardar_cap_suscripto)
        self.obj_form.boton_agregar.clicked.connect(self.agregar_inte_cap)
        self.obj_form.boton_guardar_cap_integracion.clicked.connect(self.guardar_cap_integracion)
        self.obj_form.boton_agregar_suspensiones.clicked.connect(self.agregar_suspensiones)
        self.obj_form.boton_guardar_renuncia.clicked.connect(self.guardar_renuncia)
        self.obj_form.boton_guardar_exclusion.clicked.connect(self.guardar_exclusion)
        self.obj_form.boton_guardar_suspenciones.clicked.connect(self.guardar_suspenciones)
        self.obj_form.boton_agregar_capitaliza.clicked.connect(self.agregar_capitaliza)
        self.obj_form.boton_guardar_capitalizacion.clicked.connect(self.guardar_capitalizacion)


    def guardar_capitalizacion(self):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        for row in range(self.obj_form.tw_historia_capitaliza.rowCount ()):
            obj_e_capitalizacion = E_capitalizacion()
            obj_e_capitalizacion.fecha =self.obj_form.tw_historia_capitaliza.item(row,0).text()
            obj_e_capitalizacion.pesos =self.obj_form.tw_historia_capitaliza.item(row,1).text()
            obj_e_capitalizacion.nro_acta =self.obj_form.tw_historia_capitaliza.item(row,2).text()
            obj_e_capitalizacion.fec_acta =self.obj_form.tw_historia_capitaliza.item(row,3).text()
            obj_e_capitalizacion.id_asoc =self.id_asoc
            obj_e_capitalizacion.guardar(obj_e_capitalizacion)

        msgBox = QMessageBox()
        msgBox.setWindowTitle("OK")
        msgBox.setText('Se guardo correctamente la capitalizacion')
        msgBox.exec_()

    def agregar_capitaliza(self):

         rowPosition = self.obj_form.tw_historia_capitaliza.rowCount()
         self.obj_form.tw_historia_capitaliza.insertRow(rowPosition)
         self.obj_form.tw_historia_capitaliza.setItem(rowPosition , 0, QTableWidgetItem(self.obj_form.dte_fec_capitalizacion.text()))
         self.obj_form.tw_historia_capitaliza.setItem(rowPosition , 1, QTableWidgetItem(self.obj_form.lne_importe_capitaliza.text()))
         self.obj_form.tw_historia_capitaliza.setItem(rowPosition , 2, QTableWidgetItem(self.obj_form.lne_nro_acta_capitaliza.text()))
         self.obj_form.tw_historia_capitaliza.setItem(rowPosition , 3, QTableWidgetItem(self.obj_form.dte_fec_acta_capitaliza.text()))


    def guardar_exclusion(self):
        obj_E_observaciones = E_observaciones()
        obj_E_observaciones.id_asoc =self.id_asoc
        obj_E_observaciones.tipo = "Exclusion"
        obj_E_observaciones.fecha = self.obj_form.dte_fec_exclu.text()
        obj_E_observaciones.nro_acta = self.obj_form.lne_nro_acta_exclu.text()
        obj_E_observaciones.guardar(obj_E_observaciones)
        msgBox = QMessageBox()
        msgBox.setWindowTitle("OK")
        msgBox.setText('Se guardo correctamente la exclusion')
        msgBox.exec_()

    def guardar_renuncia(self):
        obj_E_observaciones = E_observaciones()
        obj_E_observaciones.id_asoc =self.id_asoc
        obj_E_observaciones.tipo = "Renuncia"
        obj_E_observaciones.fecha = self.obj_form.dte_fec_renuncia.text()
        obj_E_observaciones.nro_acta = self.obj_form.lne_nro_acta_Renuncia.text()
        obj_E_observaciones.guardar(obj_E_observaciones)

        msgBox = QMessageBox()
        msgBox.setWindowTitle("OK")
        msgBox.setText('Se guardo correctamente la renuncia')
        msgBox.exec_()

    def guardar_suspenciones(self):

        for row in range(self.obj_form.tw_historia_susp.rowCount ()):

            obj_E_observaciones = E_observaciones()
            obj_E_observaciones.id_asoc =self.id_asoc
            obj_E_observaciones.tipo = "Suspencion"
            obj_E_observaciones.fecha = self.obj_form.tw_historia_susp.item(row,0).text()
            obj_E_observaciones.nro_acta = self.obj_form.tw_historia_susp.item(row,1).text()
            obj_E_observaciones.detalle= self.obj_form.tw_historia_susp.item(row,2).text()
            obj_E_observaciones.guardar(obj_E_observaciones)

        msgBox = QMessageBox()
        msgBox.setWindowTitle("OK")
        msgBox.setText('Se guardo correctamente el las suspenciones')
        msgBox.exec_()

    def agregar_suspensiones(self):

         rowPosition = self.obj_form.tw_historia_susp.rowCount()
         self.obj_form.tw_historia_susp.insertRow(rowPosition)
         self.obj_form.tw_historia_susp.setItem(rowPosition , 0, QTableWidgetItem(self.obj_form.dte_fec_susp.text()))
         self.obj_form.tw_historia_susp.setItem(rowPosition , 1, QTableWidgetItem(self.obj_form.lne_nro_acta_susp.text()))
         self.obj_form.tw_historia_susp.setItem(rowPosition , 2, QTableWidgetItem(str(self.obj_form.txt_detalle_susp.toPlainText())))


    def guardar_cap_integracion(self):

        for row in range(self.obj_form.tw_capital_integrado.rowCount ()):
            obj_E_capital_integracion = E_capital_integracion()
            obj_E_capital_integracion.id_asoc =self.id_asoc
            obj_E_capital_integracion.nro_cuota = self.obj_form.tw_capital_integrado.item(row,0).text()
            obj_E_capital_integracion.fec_cuota = self.obj_form.tw_capital_integrado.item(row,1).text()
            obj_E_capital_integracion.pesos= self.obj_form.tw_capital_integrado.item(row,2).text()
            obj_E_capital_integracion.tipo_aporte = self.obj_form.tw_capital_integrado.item(row,3).text()
            obj_E_capital_integracion.estado = self.obj_form.tw_capital_integrado.item(row,4).text()
            obj_E_capital_integracion.guardar(obj_E_capital_integracion)

        msgBox = QMessageBox()
        msgBox.setWindowTitle("OK")
        msgBox.setText('Se guardo correctamente el capital de integracion')
        msgBox.exec_()

    def agregar_inte_cap(self):
        obj_E_capital_integracion = E_capital_integracion()
        self.obj_form.tw_capital_integrado
        rowPosition = self.obj_form.tw_capital_integrado.rowCount()
        self.obj_form.tw_capital_integrado.insertRow(rowPosition)
        self.obj_form.tw_capital_integrado.setItem(rowPosition , 0, QTableWidgetItem(self.obj_form.lne_nro_cuota.text()))
        self.obj_form.tw_capital_integrado.setItem(rowPosition , 1, QTableWidgetItem(self.obj_form.dte_fec_cuota.text()))
        self.obj_form.tw_capital_integrado.setItem(rowPosition , 2, QTableWidgetItem(self.obj_form.lne_importe_cta.text()))
        self.obj_form.tw_capital_integrado.setItem(rowPosition , 3, QTableWidgetItem(self.obj_form.cbx_aporte_tipo.currentText()))
        self.obj_form.tw_capital_integrado.setItem(rowPosition , 4, QTableWidgetItem("Pagado"))

    def guardar_cap_suscripto(self):

        obj_e_capital_sus = E_capital_suscripto()
        obj_e_capital_sus.id_asoc = self.id_asoc
        obj_e_capital_sus.nro_asamblea = self.obj_form.lne_capital_nro_asamblea.text()
        obj_e_capital_sus.fec_asamblea = self.obj_form.dte_capital_fec_asamblea.text()
        obj_e_capital_sus.cant_cuotas = self.obj_form.lne_cant_cuotas_suscriptas.text()
        obj_e_capital_sus.pesos = self.obj_form.lne_cant_cuotas_pesos.text()
        obj_e_capital_sus.pesos_letras= self.obj_form.lne_cant_pesos_letras.text()
        obj_e_capital_sus.guardar(obj_e_capital_sus)

        obj_e_coope = E_cooperativa()
        obj_coope = obj_e_coope.get_cooperativa()
        valor_cta = round(float((float(obj_coope.pesos_obliga) - float(obj_e_capital_sus.pesos))/int(obj_coope.cant_cta_obliga)),3)
        obj_date_venc_1er_cuota = datetime.datetime.strptime(self.obj_form.dte_capital_fec_asamblea.text(), '%d/%m/%Y')

        for i in range(int(obj_coope.cant_cta_obliga)):

            nuevo_mes = obj_date_venc_1er_cuota.month + i
            nuevo_year = obj_date_venc_1er_cuota.year
            nuevo_dia = 5
            if nuevo_mes > 12 and nuevo_mes < 24:
                nuevo_mes = nuevo_mes % 12
                if nuevo_mes == 0:
                    nuevo_mes=12
                nuevo_year += 1
            elif nuevo_mes > 23 and nuevo_mes < 37:
                    nuevo_mes = nuevo_mes % 12
                    if nuevo_mes == 0:
                        nuevo_mes=12
                    nuevo_year += 2
            elif nuevo_mes > 36 and nuevo_mes < 49:
                    nuevo_mes = nuevo_mes % 12
                    if nuevo_mes == 0:
                        nuevo_mes=12
                    nuevo_year += 3
            elif nuevo_mes > 48 and nuevo_mes < 61:
                    nuevo_mes = nuevo_mes % 12
                    if nuevo_mes == 0:
                        nuevo_mes=12
                    nuevo_year += 4
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            obj_fecha_cuota= datetime.datetime(nuevo_year, nuevo_mes, nuevo_dia)
            nro_cta= i+1
            rowPosition = self.obj_form.tw_capital_integrado.rowCount()
            self.obj_form.tw_capital_integrado.insertRow(rowPosition)
            self.obj_form.tw_capital_integrado.setItem(rowPosition , 0, QTableWidgetItem(str(nro_cta)))
            self.obj_form.tw_capital_integrado.setItem(rowPosition , 1, QTableWidgetItem(str(obj_fecha_cuota)))
            self.obj_form.tw_capital_integrado.setItem(rowPosition , 2, QTableWidgetItem(str(valor_cta)))
            self.obj_form.tw_capital_integrado.setItem(rowPosition , 3, QTableWidgetItem("efectivo"))
            self.obj_form.tw_capital_integrado.setItem(rowPosition , 4, QTableWidgetItem("A pagar"))

        msgBox = QMessageBox()
        msgBox.setWindowTitle("OK")
        msgBox.setText('Se guardo correctamente el capital suscripto')
        msgBox.exec_()


    def guardar_datos_personales(self):

        obj_party_party = E_party_party()
        obj_party_party.nombre =self.obj_form.lne_nro_asoc.text()
        obj_party_party.apellido = self.obj_form.lne_apellido.text()
        obj_party_party.estado_civil = self.obj_form.cbx_estado_civil.currentText()
        obj_party_party.fec_nac = self.obj_form.dte_fec_nac.text()
        obj_party_party.cuit_cuil = self.obj_form.lne_nro_cuil.text()
        obj_party_party.tipo_doc = self.obj_form.cbx_tipo_doc.currentText()
        obj_party_party.nro_doc = self.obj_form.lne_nro_doc .text()

        self.id_party = obj_party_party.guardar(obj_party_party)

        obj_e_party_address = E_party_address()
        obj_e_party_address.id_party = self.id_party
        obj_e_party_address.domicilio = self.obj_form.lne_domicilio.text()
        obj_e_party_address.nro = self.obj_form.lne_nro_domicilio.text()
        obj_e_party_address.piso = self.obj_form.lne_piso_domicilio.text()
        obj_e_party_address.dpto = self.obj_form.lne_depto.text()
        obj_e_party_address.bloque = self.obj_form.lne_bloque.text()
        obj_e_party_address.mzna = self.obj_form.lne_manzana.text()
        obj_e_party_address.cp = self.obj_form.lne_c_postal.text()
        obj_e_party_address.localidad = self.obj_form.lne_localidad.text()
        obj_e_party_address.provincia = self.obj_form.lne_provincia.text()
        obj_e_party_address.guardar(obj_e_party_address)


        obj_e_party_contact = E_party_contact()
        obj_e_party_contact.id_party = self.id_party
        obj_e_party_contact.tel_principal = self.obj_form.lne_tel_principal.text()
        obj_e_party_contact.tel_secundario = self.obj_form.lne_tel_otro.text()
        obj_e_party_contact.email = self.obj_form.lne_correo.text()
        obj_e_party_contact.guardar(obj_e_party_contact)

        obj_e_asociado= E_asociado()
        obj_e_asociado.id_party = self.id_party
        obj_e_asociado.nro_asociado = self.obj_form.lne_nro_asoc.text()
        obj_e_asociado.fecha_ingreso = self.obj_form.dte_ingreso.text()
        obj_e_asociado.nro_acta_ingreso = self.obj_form.lne_nro_acta_ca.text()
        obj_e_asociado.nro_foja = self.obj_form.lne_nro_foja.text()
        obj_e_asociado.estado = self.obj_form.cbx_estado.currentText()

        self.id_asoc = obj_e_asociado.guardar(obj_e_asociado)
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        self.obj_form.boton_guardar_cap_suscripto.setEnabled(True)
        self.obj_form.boton_guardar_cap_integracion.setEnabled(True)
        self.obj_form.boton_guardar_transferencia.setEnabled(True)
        self.obj_form.boton_guardar_suspenciones.setEnabled(True)
        self.obj_form.boton_guardar_renuncia.setEnabled(True)
        self.obj_form.boton_guardar_exclusion.setEnabled(True)
        self.obj_form.boton_guardar_capitalizacion.setEnabled(True)




        msgBox = QMessageBox()
        msgBox.setWindowTitle("OK")
        msgBox.setText('Se creo correctamente el asociado: ' + self.obj_form.lne_nombre.text())
        msgBox.exec_()
        return False


#app = QApplication(sys.argv)
#dialogo= asociado_alta()
#dialogo.show()
#app.exec_()
