# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, Numeric,func,update,text
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion

base = declarative_base()
class E_notas(base):

    __tablename__="notas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String)
    fecha = Column(String)
    descripcion = Column(String)
    tipo = Column(String)
    session = ""

    def __init__(self):
        obj_conexion =  configuracion()
        engine=create_engine(obj_conexion.config())
        Session= sessionmaker(bind=engine)
        self.session=Session()

    @classmethod
    def guardar(cls, obj_notas):
        new_record = cls()
        new_record.titulo = obj_notas.titulo
        new_record.fecha = obj_notas.fecha
        new_record.descripcion = obj_notas.descripcion
        new_record.tipo = obj_notas.tipo
        try:
            new_record.session.add(new_record)
            new_record.session.commit()
            new_record.session.close()
            return True
        except :
            new_record.session.rollback()
            new_record.session.close()
            return False

    def get_notas(self):
        obj_coop= self.session.query(E_notas).all()
        self.session.close()
        return obj_coop

    def actualizar(self,obj_notas):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        new_record = self.obj_notas()
        new_record.titulo = obj_notas.titulo
        new_record.fecha = obj_notas.fecha
        new_record.descripcion = obj_notas.descripcion
        new_record.tipo = obj_notas.tipo

        try:
            self.session.add(new_record)
            self.session.commit()
            self.session.close()
            return True
        except :
            self.session.rollback()
            self.session.close()
            return False






