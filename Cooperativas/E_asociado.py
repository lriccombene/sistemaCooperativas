# -*- coding: utf-8 -*-
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, Numeric,func,update,text
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion

base = declarative_base()
class E_asociado(base):

    __tablename__="asociado"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_party = Column(Integer)
    nro_asociado = Column(Integer)
    fecha_ingreso = Column(String)
    nro_acta_ingreso = Column(Integer)
    nro_foja = Column(Integer)
    estado = Column(String)
    session = ""

    def __init__(self):
        obj_conexion =  configuracion()
        engine=create_engine(obj_conexion.config())
        Session= sessionmaker(bind=engine)
        self.session=Session()

    @classmethod
    def guardar(cls, obj_E_asociado):
            new_record = cls()
            new_record.nro_asociado = obj_E_asociado.nro_asociado
            new_record.fecha_ingreso = str(obj_E_asociado.fecha_ingreso)
            new_record.id_party = obj_E_asociado.id_party
            new_record.nro_acta_ingreso = obj_E_asociado.nro_acta_ingreso
            new_record.nro_foja = obj_E_asociado.nro_foja
            new_record.estado = obj_E_asociado.estado


            try:
                new_record.session.add(new_record)
                new_record.session.commit()
                obj_asoc = new_record.get_E_asociado(obj_E_asociado.id_party)
                new_record.session.close()
                return obj_asoc.id
            except :
                new_record.session.rollback()
                new_record.session.close()
                return False

    def get_E_asociado(self, id_party):
            obj_asoc= self.session.query(E_asociado).filter_by(id_party=id_party).first()
            self.session.close()
            return obj_asoc

    def get_datos_personales(self, id_party):

        query= "select pp.nombre, pp.apellido, pp.estado_civil, pp.fec_nac, pp.cuit_cuil, "
        query= query + "pp.tipo_doc, pp.nro_doc, asoc.nro_asociado, asoc.fecha_ingreso, asoc.nro_acta_ingreso, asoc.estado, "
        query= query + "asoc.nro_foja,asoc.id ,pa.domicilio, pa.nro, pa.piso, pa.dpto, pa.bloque, pa.mzna, pa.cp, pa.localidad, "
        query= query + "pa.provincia,pc.tel_principal, pc.tel_secundario, pc.email "
        query= query + "from party_party pp left join asociado asoc on pp.id = asoc.id_party "
        query= query + "left join party_address pa on pp.id = pa.id_party "
        query= query + "left join party_contact pc on pp.id = pc.id_party "
        query= query + "where pp.id ="
        query= query + str(id_party)
        query=(query)

        result = self.session.execute(query)
        try:
            #elf.session.commit()

            for item in result:
                self.session.close()
                return item
        except :
            self.session.close()
            return False

    def actualizar(self, obj_asoc):
        new_record = self.get_E_asociado(obj_asoc.id_party)
        new_record.nro_asociado = obj_asoc.nro_asociado
        new_record.fecha_ingreso = str(obj_asoc.fecha_ingreso)
        new_record.nro_acta_ingreso = obj_asoc.nro_acta_ingreso
        new_record.nro_foja = obj_asoc.nro_foja
        new_record.estado = obj_asoc.estado

        try:
            self.session.add(new_record)
            self.session.commit()
            self.session.close()
            return True
        except :
            new_record.session.rollback()
            new_record.session.close()
            return False


    def reporte_asoc(self):

        query= "select asoc.id as asoc_id, pp.apellido, pp.nombre ,obs.tipo, "
        query= query + "(select sum(pesos) from capital_suscripto where id_asoc = asoc.id) as capital_suscripto, "
        query= query + "(select sum(pesos) from capital_integracion where id_asoc = asoc.id and estado='Pagado') as capital_integracion "
        query= query + ", asoc.fecha_ingreso"
        query= query + " from party_party pp "
        query= query + " left join asociado as asoc on pp.id = asoc.id_party "
        query= query + " left join observaciones as obs on asoc.id = obs.id_asoc "
        query= query + " where obs.tipo IS NULL"
        query=(query)

        result = self.session.execute(query)
        try:
            self.session.close()
            return result
        except :
            self.session.close()
            return False

