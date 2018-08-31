# -*- coding: utf-8 -*-

import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, Numeric,func,update,text
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion

base = declarative_base()
class E_cooperativa(base):

    __tablename__="cooperativa"
    id = Column(Integer, primary_key=True, autoincrement=True)
    denominacion = Column(String)
    matricula = Column(String)
    nro_reg_prov = Column(String)
    fec = Column(DateTime)
    cuit = Column(String)
    pesos_obliga = Column(Numeric)
    cant_cta_obliga = Column(Integer)
    session = ""

    def __init__(self):
        obj_conexion =  configuracion()
        engine=create_engine(obj_conexion.config())
        Session= sessionmaker(bind=engine)
        self.session=Session()

    @classmethod
    def guardar(cls, obj_E_cooperativa):
            new_record = cls()
            new_record.denominacion = obj_E_cooperativa.denominacion
            new_record.matricula = obj_E_cooperativa.matricula
            new_record.nro_reg_prov = obj_E_cooperativa.nro_reg_prov
            new_record.fec = obj_E_cooperativa.fec
            new_record.cuit = obj_E_cooperativa.cuit
            new_record.pesos_obliga= obj_E_cooperativa.pesos_obliga
            new_record.cant_cta_obliga= obj_E_cooperativa.cant_cta_obliga

            try:
                new_record.session.add(new_record)
                new_record.session.commit()
                new_record.session.close()
                return True
            except :
                new_record.session.rollback()
                new_record.session.close()
                return False

    def get_cooperativa(self):
        obj_coop= self.session.query(E_cooperativa).first()
        self.session.close()
        return obj_coop


    def actualizar(self,obj_coop):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        new_record = self.get_cooperativa()
        new_record.denominacion = obj_coop.denominacion
        new_record.matricula = obj_coop.matricula
        new_record.nro_reg_prov = obj_coop.nro_reg_prov
        new_record.fec = obj_coop.fec
        new_record.cuit = obj_coop.cuit
        new_record.pesos_obliga = obj_coop.pesos_obliga
        new_record.cant_cta_obliga = obj_coop.cant_cta_obliga

        try:
            self.session.add(new_record)
            self.session.commit()
            self.session.close()
            return True
        except :
            self.session.rollback()
            self.session.close()
            return False

