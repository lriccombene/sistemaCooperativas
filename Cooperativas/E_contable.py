# -*- coding: utf-8 -*-

import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, Numeric,func,update,text
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion

base = declarative_base()
class E_contable(base):

    __tablename__="contable"
    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(Integer)
    pesos = Column(Numeric)
    nro_acta = Column(Integer)
    fec_acta = Column(DateTime)
    id_asoc = Column(Integer)
    session = ""

    def __init__(self):
        obj_conexion =  configuracion()
        engine=create_engine(obj_conexion.config())
        Session= sessionmaker(bind=engine)
        self.session=Session()

    @classmethod
    def guardar(cls, obj_E_capitalizacion):
            new_record = cls(1)
            new_record.fecha = obj_E_capitalizacion.fecha
            new_record.pesos = obj_E_capitalizacion.pesos
            new_record.nro_acta = str(obj_E_capitalizacion.nro_acta)
            new_record.fec_acta = obj_E_capitalizacion.fec_acta
            new_record.id_asoc = obj_E_capitalizacion.id_asoc

            try:
                new_record.session.add(new_record)
                new_record.session.commit()
                new_record.session.close()
                return True
            except :
                new_record.session.rollback()
                new_record.session.close()
                return False
