# -*- coding: utf-8 -*-

import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, Numeric,func,update,text
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion

base = declarative_base()
class E_party_address(base):

    __tablename__="party_address"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_party = Column(Integer)
    domicilio = Column(String)
    nro = Column(String)
    piso = Column(String)
    dpto = Column(String)
    bloque = Column(String)
    mzna = Column(String)
    cp = Column(String)
    localidad = Column(String)
    provincia = Column(String)
    session = ""

    def __init__(self):
        obj_conexion =  configuracion()
        engine=create_engine(obj_conexion.config())
        Session= sessionmaker(bind=engine)
        self.session=Session()

    @classmethod
    def guardar(cls, obj_E_party_address):
            new_record = cls()
            new_record.id_party = obj_E_party_address.id_party
            new_record.domicilio = obj_E_party_address.domicilio
            new_record.nro = obj_E_party_address.nro
            new_record.piso = obj_E_party_address.piso
            new_record.dpto = obj_E_party_address.dpto
            new_record.bloque = obj_E_party_address.bloque
            new_record.mzna = obj_E_party_address.mzna
            new_record.cp = obj_E_party_address.cp
            new_record.localidad = obj_E_party_address.localidad
            new_record.provincia = obj_E_party_address.provincia

            try:
                new_record.session.add(new_record)
                new_record.session.commit()
                new_record.session.close()
                return True
            except :
                new_record.session.rollback()
                new_record.session.close()
                return False


    def get_party_address(self, id_party):
        obj_party = self.session.query(E_party_address).filter_by(id_party=id_party).first()
        self.session.close()
        return obj_party


    def actualizar(self, obj_E_party_address):
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            new_record = self.get_party_address(obj_E_party_address.id_party)
            new_record.id_party = obj_E_party_address.id_party
            new_record.domicilio = obj_E_party_address.domicilio
            new_record.nro = obj_E_party_address.nro
            new_record.piso = obj_E_party_address.piso
            new_record.dpto = obj_E_party_address.dpto
            new_record.bloque = obj_E_party_address.bloque
            new_record.mzna = obj_E_party_address.mzna
            new_record.cp = obj_E_party_address.cp
            new_record.localidad = obj_E_party_address.localidad
            new_record.provincia = obj_E_party_address.provincia

            try:
                self.session.add(new_record)
                self.session.commit()
                self.session.close()
                return True
            except :
                self.session.rollback()
                self.session.close()
                return False
