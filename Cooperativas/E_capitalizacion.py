# -*- coding: utf-8 -*-

import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, Numeric,func,update,text
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion

base = declarative_base()
class E_capitalizacion(base):

    __tablename__="capitalizacion"
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
            new_record = cls()
            new_record.fecha = obj_E_capitalizacion.fecha
            new_record.pesos = obj_E_capitalizacion.pesos
            new_record.nro_acta = obj_E_capitalizacion.nro_acta
            new_record.fec_acta = str(obj_E_capitalizacion.fec_acta)
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

    def get_capitalizacion(self, id_asoc):
            obj_asoc= self.session.query(E_capitalizacion).filter_by(id_asoc=id_asoc).all()
            self.session.close()
            return obj_asoc

    def borrar(self,id_capitalizacion):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        obj=self.session.query(E_capitalizacion).filter(E_capitalizacion.id==id_capitalizacion).first()
        try:
            self.session.delete(obj)
            self.session.commit()
        except :
            self.session.rollback()
            self.session.close()
            return False
