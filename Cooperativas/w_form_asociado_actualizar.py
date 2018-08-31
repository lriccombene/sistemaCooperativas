import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox,QTableWidgetItem,QWidget
from PyQt5.QtCore import QDate
from PyQt5 import uic
from E_party_party import E_party_party
from E_party_address import E_party_address
from E_party_contact import E_party_contact
from E_asociado import E_asociado
from E_capital_integracion import E_capital_integracion
from E_observaciones import E_observaciones
from E_capitalizacion import E_capitalizacion
from E_capital_suscripto import E_capital_suscripto
from E_capital_integracion import E_capital_integracion
from form_asociado_actualizar import Ui_form_asociado_actualizar
from PyQt5.QtCore import pyqtRemoveInputHook


class asociado_actualizar(QDialog):
    obj_form= Ui_form_asociado_actualizar()
    id_party=0
    id_asoc=0

    def __init__(self):
        QDialog.__init__(self)
        self.obj_form.setupUi(self)
        self.obj_form.boton_buscar.clicked.connect(self.buscar_asoc)
        self.obj_form.boton_actualizar.clicked.connect(self.actualizar_datos_personales)
        self.obj_form.boton_actualizar_cap_suscripto.clicked.connect(self.actualizar_cap_suscripto)
        self.obj_form.boton_agregar.clicked.connect(self.agregar_inte_cap)
        self.obj_form.tw_integracion_cap.cellClicked.connect(self.select_item_integracion_cap)
        self.obj_form.boton_act_cap_integracion.clicked.connect(self.actualizar_cap_integracion)
        self.obj_form.boton_agregar_suspensiones.clicked.connect(self.agregar_suspensiones)
        self.obj_form.boton_guardar_suspenciones.clicked.connect(self.guardar_suspenciones)
        self.obj_form.tw_historia_susp.cellClicked.connect(self.select_item_suspension)
        self.obj_form.boton_actualizar_renuncia.clicked.connect(self.actualziar_renuncia)
        self.obj_form.boton_actualizar_exclusion.clicked.connect(self.actualizar_exclusion)

        self.obj_form.boton_agregar_capitaliza.clicked.connect(self.agregar_capitaliza)
        self.obj_form.boton_actualizar_capitali.clicked.connect(self.actualizar_capitali)
        self.obj_form.tw_historia_capitaliza.cellClicked.connect(self.select_item_capitaliza)


    def select_item_capitaliza(self,clickedIndex):

        w = QWidget()
        result = QMessageBox.question(w, 'Alerta', " Desea eleminar el registro de capitalizacion?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            twi0 = self.obj_form.tw_historia_capitaliza.item(clickedIndex,0)
            fecha = QDate.fromString(twi0.text(), 'yyyy-MM-dd')

            twi1 = self.obj_form.tw_historia_capitaliza.item(clickedIndex,1)
            importe = twi0.text()

            twi2 = self.obj_form.tw_historia_capitaliza.item(clickedIndex,2)
            nro_acta =twi2.text()

            twi3 = self.obj_form.tw_historia_capitaliza.item(clickedIndex,3)
            fecha_acta = QDate.fromString(twi3.text(), 'yyyy-MM-dd')

            twi3 = self.obj_form.tw_historia_capitaliza.item(clickedIndex,4)
            try:
                id_capitalizacion = twi3.text()
            except:
                id_capitalizacion =None

            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            if id_capitalizacion != None:
                obj_capitalizacion= E_capitalizacion()
                obj_capitalizacion.borrar(id_capitalizacion)

            self.obj_form.tw_historia_capitaliza.removeRow(clickedIndex)
            self.obj_form.dte_fec_capitalizacion.setDate(fecha)
            self.obj_form.lne_importe_capitaliza.setText(importe)
            self.obj_form.lne_nro_acta_capitaliza.setText(nro_acta)
            self.obj_form.dte_fec_acta_capitaliza.setDate(fecha_acta)


    def actualizar_capitali(self):

        for row in range(self.obj_form.tw_historia_capitaliza.rowCount ()):
            try:
                id = self.obj_form.tw_historia_capitaliza.item(row,4).text()
            except Exception as ex:
                id =""
                if id =="":
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
        msgBox.setText('Se actualizo correctamente la capitalizacion')
        msgBox.exec_()

    def agregar_capitaliza(self):

        rowPosition = self.obj_form.tw_historia_capitaliza.rowCount()
        self.obj_form.tw_historia_capitaliza.insertRow(rowPosition)
        self.obj_form.tw_historia_capitaliza.setItem(rowPosition , 0, QTableWidgetItem(self.obj_form.dte_fec_capitalizacion.text()))
        self.obj_form.tw_historia_capitaliza.setItem(rowPosition , 1, QTableWidgetItem(self.obj_form.lne_importe_capitaliza.text()))
        self.obj_form.tw_historia_capitaliza.setItem(rowPosition , 2, QTableWidgetItem(str(self.obj_form.lne_nro_acta_capitaliza.text())))
        self.obj_form.tw_historia_capitaliza.setItem(rowPosition , 3, QTableWidgetItem(str(self.obj_form.dte_fec_acta_capitaliza.text())))
        self.obj_form.tw_historia_capitaliza.setItem(rowPosition , 4, QTableWidgetItem("Pagado"))



    def actualizar_exclusion(self):
        obj_observacion = E_observaciones()
        obj_observacion.id_asoc = self.id_asoc
        obj_observacion.fecha = self.obj_form.dte_fec_exclusion.text()
        obj_observacion.nro_acta =self.obj_form.lne_nro_acta_exclusion.text()
        obj_observacion.actualizar_exclusion(obj_observacion)
        msgBox = QMessageBox()
        msgBox.setWindowTitle("OK")
        msgBox.setText('Se actualizo correctamente la exclusion')
        msgBox.exec_()


    def actualziar_renuncia(self):
        obj_observacion = E_observaciones()

        obj_observacion.id_asoc = self.id_asoc
        obj_observacion.fecha = self.obj_form.dte_fec_renuncia.text()
        obj_observacion.nro_acta =self.obj_form.lne_nro_acta_Renuncia.text()
        obj_observacion.actualizar_renuncia(obj_observacion)
        msgBox = QMessageBox()
        msgBox.setWindowTitle("OK")
        msgBox.setText('Se actualizo correctamente la renuncia')
        msgBox.exec_()

    def select_item_suspension(self,clickedIndex):

        w = QWidget()
        result = QMessageBox.question(w, 'Alerta', " Desea eleminar el registro de Suspencion?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            twi0 = self.obj_form.tw_historia_susp.item(clickedIndex,0)
            fecha = QDate.fromString(twi0.text(), 'yyyy-MM-dd')

            twi1 = self.obj_form.tw_historia_susp.item(clickedIndex,1)
            nro_acta = twi0.text()

            twi2 = self.obj_form.tw_historia_susp.item(clickedIndex,2)
            detalle =twi2.text()

            twi3 = self.obj_form.tw_historia_susp.item(clickedIndex,3)
            try:
                id_observacion = twi3.text()
            except:
                id_observacion =None

            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            if id_observacion != None:
                obj_observaciones= E_observaciones()
                obj_observaciones.borrar(id_observacion)

            self.obj_form.tw_integracion_cap.removeRow(clickedIndex)
            self.obj_form.dte_fec_susp.setDate(fecha)
            self.obj_form.lne_nro_acta_susp.setText(nro_acta)
            self.obj_form.txt_detalle_susp.setText(detalle)


    def guardar_suspenciones(self):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        for row in range(self.obj_form.tw_historia_susp.rowCount ()):
            try:
                id = self.obj_form.tw_historia_susp.item(row,3).text()
            except Exception as ex:
                id =""

            if id =="":
                obj_E_observaciones = E_observaciones()
                obj_E_observaciones.id_asoc =self.id_asoc
                obj_E_observaciones.fecha = self.obj_form.tw_historia_susp.item(row,0).text()
                obj_E_observaciones.nro_acta = self.obj_form.tw_historia_susp.item(row,1).text()
                obj_E_observaciones.detalle= self.obj_form.tw_historia_susp.item(row,2).text()
                obj_E_observaciones.tipo = "Suspencion"
                obj_E_observaciones.guardar(obj_E_observaciones)

        msgBox = QMessageBox()
        msgBox.setWindowTitle("OK")
        msgBox.setText('Se actualizo correctamente')
        msgBox.exec_()

    def agregar_suspensiones(self):
         rowPosition = self.obj_form.tw_historia_susp.rowCount()
         self.obj_form.tw_historia_susp.insertRow(rowPosition)
         self.obj_form.tw_historia_susp.setItem(rowPosition , 0, QTableWidgetItem(self.obj_form.dte_fec_susp.text()))
         self.obj_form.tw_historia_susp.setItem(rowPosition , 1, QTableWidgetItem(self.obj_form.lne_nro_acta_susp.text()))
         self.obj_form.tw_historia_susp.setItem(rowPosition , 2, QTableWidgetItem(str(self.obj_form.txt_detalle_susp.toPlainText())))


    def actualizar_cap_integracion(self):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()

        for row in range(self.obj_form.tw_integracion_cap.rowCount ()):
            try:
                id = self.obj_form.tw_integracion_cap.item(row,4).text()
            except Exception as ex:
                id =""

            if id =="":
                obj_E_capital_integracion = E_capital_integracion()
                obj_E_capital_integracion.id_asoc =self.id_asoc
                obj_E_capital_integracion.nro_cuota = self.obj_form.tw_integracion_cap.item(row,0).text()
                obj_E_capital_integracion.fec_cuota = self.obj_form.tw_integracion_cap.item(row,1).text()
                obj_E_capital_integracion.pesos= self.obj_form.tw_integracion_cap.item(row,2).text()
                obj_E_capital_integracion.tipo_aporte = self.obj_form.tw_integracion_cap.item(row,3).text()
                obj_E_capital_integracion.guardar(obj_E_capital_integracion)

        msgBox = QMessageBox()
        msgBox.setWindowTitle("OK")
        msgBox.setText('Se actualizo correctamente capital de integracion')
        msgBox.exec_()

    def select_item_integracion_cap(self,clickedIndex):

        w = QWidget()
        result = QMessageBox.question(w, 'Alerta', " Desea eleminar el registro de integracion de capital?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            twi0 = self.obj_form.tw_integracion_cap.item(clickedIndex,0)
            nro_cta = twi0.text()
            twi1 = self.obj_form.tw_integracion_cap.item(clickedIndex,1)
            fecha = QDate.fromString(twi1.text(), 'yyyy-MM-dd')
            twi2 = self.obj_form.tw_integracion_cap.item(clickedIndex,2)
            pesos =twi2.text()
            twi3 = self.obj_form.tw_integracion_cap.item(clickedIndex,3)
            tipo_aporte = twi3.text()
            twi4 = self.obj_form.tw_integracion_cap.item(clickedIndex,4)
            id_cap_integra = twi4.text()


            try:
                id_cap_integra = twi4.text()
            except:
                id_cap_integra =None

            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            if id_cap_integra != None:
                obj_cap_integra= E_capital_integracion()
                obj_cap_integra.borrar(id_cap_integra)

            self.obj_form.tw_integracion_cap.removeRow(clickedIndex)
            self.obj_form.lne_nro_cuota.setText(nro_cta)
            self.obj_form.lne_importe_cta.setText(pesos)
            index_tipo_aporte = self.obj_form.cbx_aporte_tipo.findText(tipo_aporte)
            self.obj_form.cbx_aporte_tipo.setCurrentIndex(index_tipo_aporte)
            self.obj_form.dte_fec_cuota.setDate(fecha)




    def agregar_inte_cap(self):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        rowPosition = self.obj_form.tw_integracion_cap.rowCount()
        self.obj_form.tw_integracion_cap.insertRow(rowPosition)
        self.obj_form.tw_integracion_cap.setItem(rowPosition , 0, QTableWidgetItem(self.obj_form.lne_nro_cuota.text()))
        self.obj_form.tw_integracion_cap.setItem(rowPosition , 1, QTableWidgetItem(self.obj_form.dte_fec_cuota.text()))
        self.obj_form.tw_integracion_cap.setItem(rowPosition , 2, QTableWidgetItem(self.obj_form.lne_importe_cta.text()))
        self.obj_form.tw_integracion_cap.setItem(rowPosition , 3, QTableWidgetItem(self.obj_form.cbx_aporte_tipo.currentText()))


    def actualizar_cap_suscripto(self):
        obj_capital_suscripto = E_capital_suscripto ()
        obj_capital_suscripto.id_asoc = self.id_asoc
        obj_capital_suscripto.nro_asamblea = self.obj_form.lne_asamble_cap_sus.text()
        obj_capital_suscripto.fec_asamblea = self.obj_form.dte_fec_asamblea_cap_sus.text()
        obj_capital_suscripto.cant_cuotas = self.obj_form.lne_cant_cta_soc_cap_sus.text()
        obj_capital_suscripto.pesos = self.obj_form.lne_pesos_cap_sus.text()
        obj_capital_suscripto.pesos_letras = self.obj_form.lne_pesos_letras_cap_sus.text()
        obj_capital_suscripto.actualizar(obj_capital_suscripto)
        msgBox = QMessageBox()
        msgBox.setWindowTitle("OK")
        msgBox.setText('Se actualizo correctamente el capital de suscripcion')
        msgBox.exec_()


    def buscar_asoc(self):

        if self.obj_form.lne_buscar_nro_asoc.text() !="" :
            a=1
        elif self.obj_form.lne_buscar_nro_doc.text() !="" :

            obj_E_party_party = E_party_party()
            obj_party = obj_E_party_party.buscar_asoc_dni(self.obj_form.lne_buscar_nro_doc.text())
            self.id_party = obj_party.id

            obj_E_asociado = E_asociado()
            obj_asoc = obj_E_asociado.get_datos_personales(self.id_party)
            self.id_asoc = obj_asoc.id

            #----------- party party incio --------------

            # falta actualizar fecha de nacimiento
            self.obj_form.lne_apellido_2.setText(obj_asoc.apellido)
            self.obj_form.lne_nombre_2.setText(obj_asoc.nombre)
            index_estado_civil= self.obj_form.cbx_estado_civil.findText(obj_asoc.estado_civil)
            self.obj_form.cbx_estado_civil.setCurrentIndex(index_estado_civil)
            index_tipo_doc = self.obj_form.cbx_tipo_doc.findText(obj_asoc.tipo_doc)
            self.obj_form.cbx_tipo_doc.setCurrentIndex(index_tipo_doc)
            self.obj_form.lne_nro_doc.setText(obj_asoc.nro_doc)
            self.obj_form.lne_nro_cuil.setText(obj_asoc.cuit_cuil)
            #----------- party party fin --------------

            #-------------asociado inicio----------------------
            self.obj_form.lne_nro_asoc.setText(str(obj_asoc.nro_asociado))
            self.obj_form.lne_nro_foja.setText(str(obj_asoc.nro_foja))
            self.obj_form.lne_nro_acta_ca.setText(str(obj_asoc.nro_acta_ingreso))
            self.obj_form.dte_ingreso.setDate(obj_asoc.fecha_ingreso)
            index_estado= self.obj_form.cbx_estado_asoc.findText(obj_asoc.estado)
            self.obj_form.cbx_estado_asoc.setCurrentIndex(index_estado)
            #-------------asociado fin----------------------

            #----------party addres inicio-------------------------
            self.obj_form.lne_domicilio.setText(obj_asoc.domicilio)
            self.obj_form.lne_nro_dom.setText(str(obj_asoc.nro))
            self.obj_form.lne_piso_domicilio.setText(obj_asoc.piso)
            self.obj_form.lne_depto.setText(obj_asoc.dpto)
            self.obj_form.lne_bloque.setText(obj_asoc.bloque)
            self.obj_form.lne_mzna.setText(obj_asoc.mzna)
            self.obj_form.lne_c_postal.setText(obj_asoc.cp)
            self.obj_form.lne_localidad.setText(obj_asoc.localidad)
            self.obj_form.lne_provincia.setText(obj_asoc.provincia)
            #----------party addres fin-------------------------

            #----------party contacto inicio--------------------
            self.obj_form.lne_tel_principal.setText(obj_asoc.tel_principal)
            self.obj_form.lne_tel_otro.setText(obj_asoc.tel_secundario)
            self.obj_form.lne_correo.setText(obj_asoc.email)
            #----------party contacto fin--------------------

            obj_E_capital_suscripto = E_capital_suscripto()
            obj_cap_sus = obj_E_capital_suscripto.get_capital_suscripto(self.id_asoc)
            self.obj_form.lne_asamble_cap_sus.setText(str(obj_cap_sus.nro_asamblea))
            self.obj_form.dte_fec_asamblea_cap_sus.setDate(obj_cap_sus.fec_asamblea)
            self.obj_form.lne_cant_cta_soc_cap_sus.setText(str(obj_cap_sus.cant_cuotas))
            self.obj_form.lne_pesos_cap_sus.setText(str(obj_cap_sus.pesos))
            self.obj_form.lne_pesos_letras_cap_sus.setText(obj_cap_sus.pesos_letras)

            obj_E_capital_integracion = E_capital_integracion()
            lista_cap_integra = obj_E_capital_integracion.get_cap_integra(self.id_asoc)
            for item in lista_cap_integra:
                rowPosition = self.obj_form.tw_integracion_cap.rowCount()
                self.obj_form.tw_integracion_cap.insertRow(rowPosition)
                self.obj_form.tw_integracion_cap.setItem(rowPosition , 0, QTableWidgetItem(str(item.nro_cuota)))
                self.obj_form.tw_integracion_cap.setItem(rowPosition , 1, QTableWidgetItem(str(item.fec_cuota)))
                self.obj_form.tw_integracion_cap.setItem(rowPosition , 2, QTableWidgetItem(str(item.pesos)))
                self.obj_form.tw_integracion_cap.setItem(rowPosition , 3, QTableWidgetItem(item.tipo_aporte))
                self.obj_form.tw_integracion_cap.setItem(rowPosition , 4, QTableWidgetItem(str(item.id)))
                self.obj_form.tw_integracion_cap.setItem(rowPosition , 5, QTableWidgetItem(str(item.estado)))

            obj_E_observaciones = E_observaciones()
            lista_observaciones = obj_E_observaciones.get_observaciones_suspension(self.id_asoc)

            for item in lista_observaciones:
                rowPosition = self.obj_form.tw_historia_susp.rowCount()
                self.obj_form.tw_historia_susp.insertRow(rowPosition)
                self.obj_form.tw_historia_susp.setItem(rowPosition , 0, QTableWidgetItem(str(item.fecha)))
                self.obj_form.tw_historia_susp.setItem(rowPosition , 1, QTableWidgetItem(str(item.nro_acta)))
                self.obj_form.tw_historia_susp.setItem(rowPosition , 2, QTableWidgetItem(str(item.detalle)))
                self.obj_form.tw_historia_susp.setItem(rowPosition , 3, QTableWidgetItem(str(item.id)))

            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            obj_renun = obj_E_observaciones.get_observaciones_renuncia(self.id_asoc)
            if obj_renun != None:
                self.obj_form.dte_fec_renuncia.setDate(obj_renun.fecha)
                self.obj_form.lne_nro_acta_Renuncia.setText(str(obj_renun.nro_acta))

            obj_expul = obj_E_observaciones.get_observaciones_expulsion(self.id_asoc)
            if obj_expul!= None:
                self.obj_form.dte_fec_exclusion.setDate(obj_expul.fecha)
                self.obj_form.lne_nro_acta_exclusion.setText(str(obj_expul.nro_acta))

            obj_E_capitalizacion = E_capitalizacion()
            lista_capitalizacion = obj_E_capitalizacion.get_capitalizacion(self.id_asoc)
            for item in lista_capitalizacion:
                rowPosition = self.obj_form.tw_historia_capitaliza.rowCount()
                self.obj_form.tw_historia_capitaliza.insertRow(rowPosition)
                self.obj_form.tw_historia_capitaliza.setItem(rowPosition , 0, QTableWidgetItem(str(item.fecha)))
                self.obj_form.tw_historia_capitaliza.setItem(rowPosition , 1, QTableWidgetItem(str(item.pesos)))
                self.obj_form.tw_historia_capitaliza.setItem(rowPosition , 2, QTableWidgetItem(str(item.nro_acta)))
                self.obj_form.tw_historia_capitaliza.setItem(rowPosition , 3, QTableWidgetItem(str(item.fec_acta)))
                self.obj_form.tw_historia_capitaliza.setItem(rowPosition , 4, QTableWidgetItem(str(item.id)))


    def actualizar_datos_personales(self):
        #----------- party party incio --------------

        obj_party= E_party_party()
        obj_party.id = self.id_party
        obj_party.apellido  =self.obj_form.lne_apellido_2.text()
        obj_party.nombre  = self.obj_form.lne_nombre_2.text()
        obj_party.estado_civil  = self.obj_form.cbx_estado_civil.currentText()
        obj_party.fec_nac  = self.obj_form.dte_fec_nac.text()

        obj_party.tipo_doc  = self.obj_form.cbx_tipo_doc.currentText()
        obj_party.nro_doc  = self.obj_form.lne_nro_doc.text()
        obj_party.cuit_cuil  = self.obj_form.lne_nro_cuil.text()
        obj_party.actualizar(obj_party)
        #----------- party party fin -----

        #-------------asociado inicio-------------------------------
        obj_asociado = E_asociado()
        obj_asociado.id = self.id_asoc
        obj_asociado.id_party = self.id_party
        obj_asociado.nro_asociado = self.obj_form.lne_nro_asoc.text()
        obj_asociado.nro_foja = self.obj_form.lne_nro_foja.text()
        obj_asociado.nro_acta_ingreso = self.obj_form.lne_nro_acta_ca.text()
        obj_asociado.fecha_ingreso = self.obj_form.dte_ingreso.text()
        obj_asociado.estado = self.obj_form.cbx_estado_asoc.currentText()
        obj_asociado.actualizar(obj_asociado)
        #-------------asociado fin ----------------------
        #----------party addres inicio-------------------------

        obj_party_address = E_party_address()
        obj_party_address.id_party =self.id_party
        obj_party_address.domicilio = self.obj_form.lne_domicilio.text()
        obj_party_address.nro = self.obj_form.lne_nro_dom.text()
        obj_party_address.piso = self.obj_form.lne_piso_domicilio.text()
        obj_party_address.dpto = self.obj_form.lne_depto.text()
        obj_party_address.bloque = self.obj_form.lne_bloque.text()
        obj_party_address.mzna = self.obj_form.lne_mzna.text()
        obj_party_address.cp = self.obj_form.lne_c_postal.text()
        obj_party_address.localidad = self.obj_form.lne_localidad.text()
        obj_party_address.provincia = self.obj_form.lne_provincia.text()
        obj_party_address.actualizar(obj_party_address)
        #----------party addres fin -------------------------
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        #----------party contacto inicio--------------------
        obj_party_contacto = E_party_contact()
        obj_party_contacto.id_party = self.id_party
        obj_party_contacto.tel_principal = self.obj_form.lne_tel_principal.text()
        obj_party_contacto.tel_secundario = self.obj_form.lne_tel_otro.text()
        obj_party_contacto.email = self.obj_form.lne_correo.text()
        obj_party_contacto.actualizar(obj_party_contacto)
        #----------party contacto fin--------------------
        msgBox = QMessageBox()
        msgBox.setWindowTitle("OK")
        msgBox.setText('Se actualizo correctamente el capital de datos personales')
        msgBox.exec_()


#app = QApplication(sys.argv)
#dialogo= asociado_actualizar()
#dialogo.show()
#app.exec_()


