# -*- coding: utf-8 -*-

import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, Numeric,func,update,text
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion

base = declarative_base()
class E_datos_personales(base):

    __tablename__="datos_personales"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_asociado= Column(Integer)
    domicilio = Column(String)
    nor_domicilio = Column(String)
    piso = Column(String)
    dpto = Column(String)
    bloque = Column(String)
    manzana = Column(String)
    cp = Column(String)
    localidad = Column(String)
    provincia = Column(String)
    tel_principal = Column(String)
    otro_telefono = Column(String)
    email = Column(String)
    session = ""

    def __init__(self):
        obj_conexion =  configuracion()
        engine=create_engine(obj_conexion.config())
        Session= sessionmaker(bind=engine)
        self.session=Session()

    @classmethod
    def guardar(cls, obj_E_cooperativa_address):
            new_record = cls(1)
            new_record.id_asociado = E_cooperativa_address.id_cooperativa
            new_record.domicilio = E_cooperativa_address.domicilio
            new_record.domicilio = E_cooperativa_address.nor_domicilio
            new_record.piso = str(E_cooperativa_address.piso)
            new_record.dpto = E_cooperativa_address.nro
            new_record.cp = E_cooperativa_address.cp
            new_record.manzana = E_cooperativa_address.id_cooperativa
            new_record.cod_postal = E_cooperativa_address.domicilio
            new_record.localidad = str(E_cooperativa_address.piso)
            new_record.provincia = E_cooperativa_address.nro
            new_record.bloque = E_cooperativa_address.bloque
            new_record.tel_principal = str(E_cooperativa_address.tel_principal)
            new_record.otro_telefono = E_cooperativa_address.otro_telefono
            new_record.email = E_cooperativa_address.email


            try:
                new_record.session.add(new_record)
                new_record.session.commit()
                new_record.session.close()
                return True
            except :
                new_record.session.rollback()
                new_record.session.close()
                return False
