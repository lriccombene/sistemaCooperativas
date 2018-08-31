# -*- coding: utf-8 -*-

import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, Numeric,func,update,text
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion

base = declarative_base()
class E_party_party(base):

    __tablename__="party_party"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    apellido = Column(String)
    estado_civil = Column(String)
    fec_nac = Column(DateTime)
    cuit_cuil = Column(String)
    tipo_doc = Column(String)
    nro_doc = Column(String)
    session = ""

    def __init__(self):
        obj_conexion =  configuracion()
        engine=create_engine(obj_conexion.config())
        Session= sessionmaker(bind=engine)
        self.session=Session()

    @classmethod
    def guardar(cls, obj_E_party_party):
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            new_record = cls()
            new_record.nombre = obj_E_party_party.nombre.upper()
            new_record.apellido = obj_E_party_party.apellido.upper()
            new_record.estado_civil = obj_E_party_party.estado_civil
            new_record.fec_nac = obj_E_party_party.fec_nac
            new_record.cuit_cuil = obj_E_party_party.cuit_cuil
            new_record.tipo_doc = obj_E_party_party.tipo_doc
            new_record.nro_doc = obj_E_party_party.nro_doc
            try:
                new_record.session.add(new_record)
                new_record.session.commit()
                obj_party_party = new_record.session.query(E_party_party).filter_by(nro_doc=str(obj_E_party_party.nro_doc)).first()
                new_record.session.close()
                return obj_party_party.id
            except :
                new_record.session.rollback()
                new_record.session.close()
                return False

    def buscar_asoc_apellido(self, apellido):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        obj_party = self.session.query(E_party_party).filter_by(apellido=str(apellido)).first()
        self.session.close()
        return obj_party

    def buscar_asoc_dni(self, nro_doc):
        obj_party = self.session.query(E_party_party).filter_by(nro_doc=str(nro_doc)).first()
        self.session.close()
        return obj_party


    def actualizar(self, obj_party):
            new_record = self.session.query(E_party_party).filter_by(id=obj_party.id).first()
            new_record.nombre = obj_party.nombre.upper()
            new_record.apellido = obj_party.apellido.upper()
            new_record.estado_civil = obj_party.estado_civil
            new_record.fec_nac = obj_party.fec_nac
            new_record.cuit_cuil = obj_party.cuit_cuil
            new_record.tipo_doc = obj_party.tipo_doc
            new_record.nro_doc = obj_party.nro_doc
            try:
                self.session.add(new_record)
                self.session.commit()
                self.session.close()
                return True
            except :
                new_record.session.rollback()
                new_record.session.close()
                return False


