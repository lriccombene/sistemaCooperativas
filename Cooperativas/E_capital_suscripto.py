# -*- coding: utf-8 -*-

import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, Numeric,func,update,text
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion

base = declarative_base()
class E_capital_suscripto(base):

    __tablename__="capital_suscripto"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_asoc = Column(Integer)
    nro_asamblea = Column(Integer)
    fec_asamblea = Column(DateTime)
    cant_cuotas = Column(Integer)
    pesos = Column(Numeric)
    pesos_letras= Column(String)
    session = ""

    def __init__(self):
        obj_conexion =  configuracion()
        engine=create_engine(obj_conexion.config())
        Session= sessionmaker(bind=engine)
        self.session=Session()

    @classmethod
    def guardar(cls, obj_E_cooperativa):
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            new_record = cls()
            new_record.id_asoc = obj_E_cooperativa.id_asoc
            new_record.nro_asamblea = obj_E_cooperativa.nro_asamblea
            new_record.fec_asamblea = str(obj_E_cooperativa.fec_asamblea)
            new_record.cant_cuotas = obj_E_cooperativa.cant_cuotas
            new_record.pesos = obj_E_cooperativa.pesos
            new_record.pesos_letras = obj_E_cooperativa.pesos_letras
            try:
                new_record.session.add(new_record)
                new_record.session.commit()
                new_record.session.close()
                return True
            except :
                new_record.session.rollback()
                new_record.session.close()
                return False

    def get_capital_suscripto(self,id_asoc):
        obj_asoc= self.session.query(E_capital_suscripto).filter_by(id_asoc=id_asoc).first()
        self.session.close()
        return obj_asoc

    def actualizar(self, obj_E_cooperativa):
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            new_record = self.get_capital_suscripto(obj_E_cooperativa.id_asoc)
            new_record.nro_asamblea = obj_E_cooperativa.nro_asamblea
            new_record.fec_asamblea = str(obj_E_cooperativa.fec_asamblea)
            new_record.cant_cuotas = obj_E_cooperativa.cant_cuotas
            new_record.pesos = obj_E_cooperativa.pesos
            new_record.pesos_letras = obj_E_cooperativa.pesos_letras
            try:
                self.session.add(new_record)
                self.session.commit()
                self.session.close()
                return True
            except :
                self.session.rollback()
                self.session.close()
                return False
