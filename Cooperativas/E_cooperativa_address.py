# -*- coding: utf-8 -*-

import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, Numeric,func,update,text
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion

base = declarative_base()
class E_cooperativa_address(base):

    __tablename__="cooperativa_address"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_cooperativa = Column(Integer)
    domicilio = Column(String)
    piso = Column(String)
    nro = Column(String)
    cp = Column(String)
    localidad = Column(String)
    provincia = Column(String)
    telefono = Column(String)
    email = Column(String)
    session = ""

    def __init__(self):
        obj_conexion =  configuracion()
        engine=create_engine(obj_conexion.config())
        Session= sessionmaker(bind=engine)
        self.session=Session()

    @classmethod
    def guardar(cls, obj_E_cooperativa_address):
            new_record = cls()
            new_record.id_cooperativa = obj_E_cooperativa_address.id_cooperativa
            new_record.domicilio = obj_E_cooperativa_address.domicilio
            new_record.piso = obj_E_cooperativa_address.piso
            new_record.nro = obj_E_cooperativa_address.nro
            new_record.cp = obj_E_cooperativa_address.cp
            new_record.localidad = obj_E_cooperativa_address.localidad
            new_record.provincia = obj_E_cooperativa_address.provincia
            new_record.telefono = obj_E_cooperativa_address.telefono
            new_record.email = obj_E_cooperativa_address.email

            try:
                new_record.session.add(new_record)
                new_record.session.commit()
                new_record.session.close()
                return True
            except :
                new_record.session.rollback()
                new_record.session.close()
                return False

    def get_coop_address(self):
        obj_coop= self.session.query(E_cooperativa_address).first()
        self.session.close()
        return obj_coop

    def actualizar(self,coop_address):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        new_record = self.get_coop_address()
        new_record.domicilio = coop_address.domicilio
        new_record.piso = coop_address.piso
        new_record.nro = coop_address.nro
        new_record.cp = coop_address.cp
        new_record.localidad = coop_address.localidad
        new_record.provincia = coop_address.provincia
        new_record.telefono = coop_address.telefono
        new_record.email = coop_address.email

        try:
            self.session.add(new_record)
            self.session.commit()
            self.session.close()
            return True
        except :
            self.session.rollback()
            self.session.close()
            return False






