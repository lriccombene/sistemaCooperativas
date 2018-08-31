import sys, os,datetime
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox,QTableWidgetItem,QWidget,QFileDialog
from PyQt5 import uic
from form_reportes_asociados import Ui_form_reporte_asoc
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
from E_cooperativa_address import E_cooperativa_address
from E_cooperativa import E_cooperativa
from E_asociado import E_asociado
from E_configuracion import configuracion
from E_capital_suscripto import E_capital_suscripto
import subprocess


class reporte_asoc(QDialog):
    obj_form= Ui_form_reporte_asoc()
    id_party=0
    id_asoc=0

    def __init__(self):
        QDialog.__init__(self)
        self.obj_form= Ui_form_reporte_asoc()
        self.obj_form.setupUi(self)
        self.obj_form.boton_reporte_asoc_imprimir.clicked.connect(self.reporte_asoc)



    def reporte_asoc(self):

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
                  [Paragraph('<font size=8> <b> Listado de asociados </b><br/></font>',estilo_texto)]]

        tcabezal=Table(cabezal, (590))
        tcabezal.setStyle(TableStyle([
                                    ('INNERGRID', (0,1), (-1,-1), 0.25, colors.black),
                                    ('BOX', (0,1), (-1,-1), 0.25, colors.black),
                                    ('BACKGROUND',(0,1),(-1,1),colors.white)
                                    ]))
        story.append(tcabezal)
        story.append(Spacer(0,-15))

        integrantes = [[Paragraph('''<font size=10> <b> </b></font>''',styleSheet["BodyText"])],
                       [Paragraph('''<font size=10> <b> </b>Nombre </font>''',estilo_texto),
                        Paragraph('''<font size=10> <b> </b>Cap Integrado</font>''',estilo_texto),
                        Paragraph('''<font size=10> <b> </b>Cap Suscripto</font>''',estilo_texto),
                        Paragraph('''<font size=10> <b> </b>Derechos Soc</font>''',estilo_texto)]]

        obj_E_asociado = E_asociado()
        lista_asoc = obj_E_asociado.reporte_asoc()
        hoy= datetime.datetime.now()
        obj_E_coope = E_cooperativa()
        obj_coope = obj_E_coope.get_cooperativa()

        for item in lista_asoc:
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            obj_E_cap_sus = E_capital_suscripto()
            obj_cap_sus = obj_E_cap_sus.get_capital_suscripto(item.asoc_id)
            pesos=""

            try:
                pesos = obj_cap_sus.pesos
            except:
                pesos =0

            if  pesos >0 :

                hoy_mes = int(hoy.year * 12 )+ int(hoy.month)
                fec_ingreso_mes = int(item.fecha_ingreso.year * 12 ) + item.fecha_ingreso.month
                total_mes = hoy_mes- fec_ingreso_mes

                if total_mes > obj_coope.cant_cta_obliga:
                    try :
                        capital_suscripto =float(item.capital_suscripto)
                    except:
                        capital_suscripto =0

                    try :
                        capital_integracion = float(item.capital_integracion)
                    except:
                        capital_integracion = 0

                    total_asoc = capital_integracion + capital_suscripto
                    total_valor=obj_coope.pesos_obliga

                else:
                    total_valor = total_mes * (obj_coope.pesos_obliga/obj_coope.cant_cta_obliga)
                    capital_suscripto=""
                    capital_integracion=""
                    try :
                        capital_suscripto =float(item.capital_suscripto)
                    except:
                        capital_suscripto =0

                    try :
                        capital_integracion = float(item.capital_integracion)
                    except:
                        capital_integracion = 0

                    total_asoc = capital_integracion + capital_suscripto

                if total_asoc >= total_valor:

                    estiloape_nom= " <font size=8>" + str(item.apellido+" " +item.nombre) + "</font>"
                    estilocap_inte= " <font size=8>" + str(item.capital_integracion) + "</font>"
                    estilocap_sus = " <font size=8>" + str(item.capital_suscripto) + "</font>"
                    estiloderechos = " <font size=8>" + str("Habilitado") + "</font>"


                    integrantes.append([Paragraph(estiloape_nom,estilo_texto),
                                        Paragraph(estilocap_inte,estilo_texto),
                                        Paragraph(estilocap_sus,estilo_texto),
                                        Paragraph(estiloderechos,estilo_texto)])

                    tintegrantes=Table(integrantes,(60,60,60,70))
                    tintegrantes.setStyle(TableStyle([
                                            ('INNERGRID', (0,1), (-1,-1), 0.25, colors.black),
                                            ('BOX', (0,1), (-1,-1), 0.25, colors.black),
                                            ('BACKGROUND',(0,1),(-1,1),colors.lightgrey)
                                            ]))
        story.append(tintegrantes)
        #cant_list = len(self.lista_ticket)
        #if(cant_list <10):
        #    result = 11-cant_list
        #    for item in range(1,result):
        #        story.append(Spacer(0,8))

        #story.append(Spacer(0,1))

        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()

        #---------------------------------------CAMBIAR RUTA (LA PALABRA slam2016 POR LA RUTA DESEADA DE LA PC)------------------------------------------------#

        obj_config = configuracion()
        cadena = obj_config.ruta()

        file_path = (cadena  + "/pdf")
        #---EJEMPLO de windows: c:/Users/tatilu-----------------------------------------------------------------------#
        if not os.path.exists(file_path):
               os.makedirs(file_path)
        doc = SimpleDocTemplate(file_path + "listado_asoc_coope.pdf", pagesize=A4, rightMargin=0.5,leftMargin=0.5, topMargin=5,bottomMargin=18)

        doc.build(story )

        msgBox = QMessageBox()
        msgBox.setWindowTitle("Estado de Ticket")
        msgBox.setText("El Listado se ha generado correctamente" )
        msgBox.exec_()

        if sys.platform == 'linux':
            subprocess.call(["xdg-open", file_path + "listado_asoc_coope.pdf"])
        else:
            os.startfile( file_path + "listado_asoc_coope.pdf")

