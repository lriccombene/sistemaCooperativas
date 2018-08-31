import sys, os
import subprocess
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox,QTableWidgetItem,QWidget,QFileDialog
from PyQt5 import uic
from form_notas import Ui_form_notas
from PyQt5.QtCore import pyqtRemoveInputHook
from E_notas import E_notas
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.platypus import Spacer, SimpleDocTemplate, Table, TableStyle
from reportlab.platypus import Paragraph, Image,Flowable
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.shapes import String, Line
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.units import inch
from reportlab.lib import colors
from E_configuracion import configuracion
from E_cooperativa_address import E_cooperativa_address

class notas(QDialog):
    obj_form= Ui_form_notas()
    titulo = ""
    fecha = ""
    descripcion = ""
    tipo = ""

    def __init__(self):
        QDialog.__init__(self)
        self.obj_form= Ui_form_notas()
        self.obj_form.setupUi(self)
        self.obj_form.boton_notas_imprimir.clicked.connect(self.imprimir)
        self.obj_form.boton_notas_guardar.clicked.connect(self.notas_guardar)
        self.obj_form.tw_lista_notas.cellClicked.connect(self.seleccion_item_tabla)
        obj_notas = E_notas()
        list_notas = obj_notas.get_notas()
        for item in list_notas:
            rowPosition = self.obj_form.tw_lista_notas.rowCount()
            self.obj_form.tw_lista_notas.insertRow(rowPosition)
            self.obj_form.tw_lista_notas.setItem(rowPosition , 0, QTableWidgetItem(str(item.titulo)))
            self.obj_form.tw_lista_notas.setItem(rowPosition , 1, QTableWidgetItem(str(item.fecha)))
            self.obj_form.tw_lista_notas.setItem(rowPosition , 2, QTableWidgetItem(str(item.descripcion)))
            self.obj_form.tw_lista_notas.setItem(rowPosition , 3, QTableWidgetItem(str(item.tipo)))


    def notas_guardar(self):
        obj_notas = E_notas()
        obj_notas.titulo = self.obj_form.lne_notas_titulo.text()
        obj_notas.fecha =  self.obj_form.dte_fec_notas.text()
        obj_notas.descripcion =  self.obj_form.txt_detalle_notas.toPlainText()
        obj_notas.tipo = self.obj_form.cbx_nota_tipo.currentText()
        obj_notas.guardar(obj_notas)
        rowPosition = self.obj_form.tw_lista_notas.rowCount()
        self.obj_form.tw_lista_notas.insertRow(rowPosition)
        self.obj_form.tw_lista_notas.setItem(rowPosition , 0, QTableWidgetItem(str(obj_notas.titulo)))
        self.obj_form.tw_lista_notas.setItem(rowPosition , 1, QTableWidgetItem(str(obj_notas.fecha)))
        self.obj_form.tw_lista_notas.setItem(rowPosition , 2, QTableWidgetItem(str(obj_notas.descripcion)))
        self.obj_form.tw_lista_notas.setItem(rowPosition , 3, QTableWidgetItem(str(obj_notas.tipo)))
        msgBox = QMessageBox()
        msgBox.setWindowTitle("OK")
        msgBox.setText('Se creo correctamente la nota: ' + obj_notas.titulo)
        msgBox.exec_()

    def seleccion_item_tabla(self, clickedIndex):

        self.obj_form.txt_notas_busqueda.setPlainText(self.obj_form.tw_lista_notas.item(clickedIndex,2).text())
        self.titulo = self.obj_form.tw_lista_notas.item(clickedIndex,0).text()
        self.fecha = self.obj_form.tw_lista_notas.item(clickedIndex,1).text()
        self.descripcion = self.obj_form.tw_lista_notas.item(clickedIndex,2).text()
        self.tipo = self.obj_form.tw_lista_notas.item(clickedIndex,3).text()



    def imprimir(self):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        styleSheet=getSampleStyleSheet()
        img=Image("cabezal3.png",150,35)
        img.hAlign = "RIGHT"
        otro_estilo= ParagraphStyle('',fontSize =6,textColor = '#000',leftIndent = 0,rightIndent = 100)

        style_barra= ParagraphStyle('',fontSize =10,textColor = '#000',leftIndent = 0,rightIndent = 50)
        texto_principal = ""
        texto_secundario = ParagraphStyle('',fontSize =10,textColor = '#000',leftIndent = 0,rightIndent = 0)
        texto_banner2 = ParagraphStyle('',fontSize =6,textColor = '#000',leftIndent =-150,rightIndent = 0)

        estilo_texto = ParagraphStyle('',
                fontSize = 5,
                        alignment = 0,
                        spaceBefore = 0,
                        spaceAfter = 0,
            #backColor = '#fff',
            textColor = '#000',
            leftIndent = 5 )

        h = ""#Paragraph("<br/><br/><br/>aa<br/><b>Buenos Aires 53 -Local 2 y 3 -Tel.:02920-432424/ Cel.:02920-15695353</b>  ",texto_banner2)
        banner = [ [ img,h] ]
        obj_E_cooperativa_address = E_cooperativa_address()
        obj_coope_address = obj_E_cooperativa_address.get_coop_address()


        banner2 = [[Paragraph('''<font size=3> <b> </b></font>''',styleSheet["BodyText"])],
                    [Paragraph("<b> "+obj_coope_address.domicilio + " " + obj_coope_address.nro
                    +" telefono: " +obj_coope_address.telefono+"</b>"+
                     obj_coope_address.localidad + " - " +
                     obj_coope_address.provincia + "- E-mail: "
                     + str(obj_coope_address.email) ,texto_banner2)]]

        options = QFileDialog.Options()
        story=[]

        ban = Table( banner, colWidths=300, rowHeights=70,hAlign = "RIGHT")
        ban2 = Table( banner2, colWidths=300, rowHeights=10)

        #story.append(Spacer(100,10))
        ##superior
        d = Drawing(100, 1)
        d.add(Line(-5, -15, 585, -15))
        story.append(d)
        #izquierda
        d = Drawing(100, 1)
        d.add(Line(-5, -15, -5, -94))
        story.append(d)

        story.append(ban)
        story.append(Spacer(0,1))
        story.append(ban2)
        story.append(Spacer(0,-150))

        #centro
        d = Drawing(100, 1)
        d.add(Line(250, -2, 250, 79))
        story.append(d)
        #derecha
        d = Drawing(100, 1)
        d.add(Line(585, -1, 585, 79))
        story.append(d)
        #inferior
        d = Drawing(100, 1)
        d.add(Line(-5, 0, 585, 0))
        story.append(d)
        story.append(Spacer(150,-10))

        cabezal =[[Paragraph('''<font size=8> <b> </b></font>''',styleSheet["BodyText"])],
                  [Paragraph('<font size=8> <b> Listado '+ self.tipo + " "+ self.titulo +" " + str(self.fecha)  + '</b><br/></font>',estilo_texto)]]

        tcabezal=Table(cabezal, (590))
        tcabezal.setStyle(TableStyle([
                                    ('INNERGRID', (0,1), (-1,-1), 0.25, colors.black),
                                    ('BOX', (0,1), (-1,-1), 0.25, colors.black),
                                    ('BACKGROUND',(0,1),(-1,1),colors.white)
                                    ]))
        story.append(tcabezal)
        story.append(Spacer(0,140))
        detalle =[[Paragraph('''<font size=8> <b> </b></font>''',styleSheet["BodyText"])],
                  [Paragraph('<font size=8> <b>'+self.descripcion+ '</b><br/></font>',estilo_texto)]]

        tdetalle=Table(detalle, (590))
        tdetalle.setStyle(TableStyle([
                                    ('INNERGRID', (0,1), (-1,-1), 0.25, colors.black),
                                    ('BOX', (0,1), (-1,-1), 0.25, colors.black),
                                    ('BACKGROUND',(0,1),(-1,1),colors.white)
                                    ]))
        story.append(tdetalle)

        obj_config = configuracion()
        cadena = obj_config.ruta()

        file_path = (cadena  + "/pdf")
        #---EJEMPLO de windows: c:/Users/tatilu-----------------------------------------------------------------------#
        if not os.path.exists(file_path):
               os.makedirs(file_path)
        doc = SimpleDocTemplate(file_path + "nota"+self.tipo+".pdf", pagesize=A4, rightMargin=0.5,leftMargin=0.5, topMargin=5,bottomMargin=18)

        doc.build(story )

        msgBox = QMessageBox()
        msgBox.setWindowTitle("Estado de Ticket")
        msgBox.setText("El Listado se ha generado correctamente" )
        msgBox.exec_()

        if sys.platform == 'linux':
            subprocess.call(["xdg-open", file_path + "nota_"+self.tipo+".pdf"])
        else:
            os.startfile( file_path + "nota_"+self.tipo+".pdf")




#app = QApplication(sys.argv)
#dialogo= notas()
#dialogo.show()
#app.exec_()
