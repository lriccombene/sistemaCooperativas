# -*- coding: utf-8 -*-

import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, Numeric,func,update,text
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion

base = declarative_base()
class E_capital_transferido(base):

    __tablename__="capital_transferido"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_asoc = Column(Integer)
    cant_cuotas = Column(Integer)
    pesos = Column(Numeric)
    fec = Column(Integer)
    nro_acta = Column(Integer)
    id_asoc_a = Column(Integer)
    id_asoc_de = Column(Integer)
    session = ""

    def __init__(self):
        obj_conexion =  configuracion()
        engine=create_engine(obj_conexion.config())
        Session= sessionmaker(bind=engine)
        self.session=Session()

    @classmethod
    def guardar(cls, obj_E_capitalizacion):
            new_record = cls(1)
            new_record.id_asoc = obj_E_capitalizacion.id_asoc
            new_record.cant_cuotas = obj_E_capitalizacion.cant_cuotas
            new_record.pesos = obj_E_capitalizacion.pesos
            new_record.fecha = str(obj_E_capitalizacion.fecha)
            new_record.nro_acta = obj_E_capitalizacion.nro_acta
            new_record.id_asoc_a = obj_E_capitalizacion.id_asoc_a
            new_record.id_asoc_de = obj_E_capitalizacion.id_asoc_de

            try:
                new_record.session.add(new_record)
                new_record.session.commit()
                new_record.session.close()
                return True
            except :
                new_record.session.rollback()
                new_record.session.close()
                return False
