# -*- coding: utf-8 -*-

import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, Numeric,func,update,text
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion

base = declarative_base()
class E_observaciones(base):

    __tablename__= "observaciones"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_asoc = Column(Integer)
    tipo = Column(String)
    fecha = Column(DateTime)
    nro_acta = Column(Integer)
    detalle = Column(String)
    session = ""

    def __init__(self):
        obj_conexion =  configuracion()
        engine=create_engine(obj_conexion.config())
        Session= sessionmaker(bind=engine)
        self.session=Session()

    @classmethod
    def guardar(cls, obj_E_observaciones):
            new_record = cls()
            new_record.id_asoc = obj_E_observaciones.id_asoc
            new_record.tipo = obj_E_observaciones.tipo
            new_record.fecha = obj_E_observaciones.fecha
            new_record.nro_acta = obj_E_observaciones.nro_acta
            new_record.detalle = obj_E_observaciones.detalle


            try:
                new_record.session.add(new_record)
                new_record.session.commit()
                new_record.session.close()
                return True
            except :
                new_record.session.rollback()
                new_record.session.close()
                return False

    def get_observaciones_suspension(self, id_asoc):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        lista_observaciones = self.session.query(E_observaciones).filter_by(id_asoc=id_asoc,tipo='Suspencion').all()
        self.session.close()
        return lista_observaciones


    def get_observaciones_renuncia(self, id_asoc):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        lista_observaciones = self.session.query(E_observaciones).filter_by(id_asoc=id_asoc,tipo='Renuncia').first()
        self.session.close()
        return lista_observaciones

    def get_observaciones_expulsion(self, id_asoc):

        lista_observaciones = self.session.query(E_observaciones).filter_by(id_asoc=id_asoc,tipo='Exclusion').first()
        self.session.close()
        return lista_observaciones

    def borrar(self,id_observacion):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        obj=self.session.query(E_observaciones).filter(E_observaciones.id==id_observacion).first()
        self.session.delete(obj)
        self.session.commit()

    def actualizar_renuncia(self, obj_observacion):
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            new_record = self.session.query(E_observaciones).filter_by(id_asoc=obj_observacion.id_asoc,tipo='Renuncia').first()
            if new_record ==None:
                obj_observacion.tipo ="Renuncia"
                self.guardar(obj_observacion)
                self.session.close()
                return True
            else:
                new_record.id_asoc = obj_observacion.id_asoc
                new_record.tipo = "Renuncia"
                new_record.fecha = obj_observacion.fecha
                new_record.nro_acta = obj_observacion.nro_acta
                new_record.detalle = ""
                try:
                    self.session.add(new_record)
                    self.session.commit()
                    self.session.close()
                    return True
                except :
                    self.session.rollback()
                    self.session.close()
                    return False



    def actualizar_exclusion(self, obj_observacion):

            new_record = self.session.query(E_observaciones).filter_by(id_asoc=obj_observacion.id_asoc,tipo='Exclusion').first()
            if new_record ==None:
                obj_observacion.tipo ="Exclusion"
                self.guardar(obj_observacion)
                self.session.close()
                return True
            else:
                new_record.id_asoc = obj_observacion.id_asoc
                new_record.tipo = "Exclusion"
                new_record.fecha = obj_observacion.fecha
                new_record.nro_acta = obj_observacion.nro_acta
                new_record.detalle = ""

                try:
                    self.session.add(new_record)
                    self.session.commit()
                    self.session.close()
                    return True
                except :
                    self.session.rollback()
                    self.session.close()
                    return False








