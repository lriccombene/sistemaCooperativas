# -*- coding: utf-8 -*-

import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, Numeric,func,update,text
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion

base = declarative_base()
class E_cargos(base):

    __tablename__="cargos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_asoc = Column(Integer)
    cargo = Column(String)
    fec_desde = Column(DateTime)
    fec_hasta = Column(DateTime)
    observacion = Column(String)
    session = ""

    def __init__(self):
        obj_conexion =  configuracion()
        engine=create_engine(obj_conexion.config())
        Session= sessionmaker(bind=engine)
        self.session=Session()

    @classmethod
    def guardar(cls, obj_E_cargos):
            new_record = cls()
            new_record.id_asoc = obj_E_cargos.id_asoc
            new_record.cargo = obj_E_cargos.cargo
            new_record.fec_desde = obj_E_cargos.fec_desde
            new_record.fec_hasta = obj_E_cargos.fec_hasta
            new_record.observacion = obj_E_cargos.observacion

            try:
                new_record.session.add(new_record)
                new_record.session.commit()
                new_record.session.close()
                #pyqtRemoveInputHook()
                #import pdb; pdb.set_trace()
                return new_record.buscar_cargo(obj_E_cargos.id_asoc)
            except :
                new_record.session.rollback()
                new_record.session.close()
                return False

    def get_cargos(self):
        lista_cargos= self.session.query(E_cargos).all()
        self.session.close()
        return lista_cargos

    def get_grilla_form_cargos(self):
            sql = text('select pp.nombre, pp.apellido, pp.nro_doc, asoc.nro_asociado, cg.cargo, cg.fec_desde, cg.fec_hasta, cg.observacion, cg.id from party_party pp inner join asociado asoc on pp.id = asoc.id_party inner join cargos cg on asoc.id =cg.id_asoc ')
            result = self.session.execute(sql)
            try:
                return result
            except :
                self.session.close()
                return False

    def buscar_cargo(self,id_asoc):
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            result= self.session.query(E_cargos).filter_by(id_asoc=id_asoc).first()
            self.session.commit()
            try:
                return result
            except :
               return False

    def borrar_cargo(self,id_cargo):
            result= self.session.query(E_cargos).filter_by(id=id_cargo).delete()
            self.session.commit()
            try:
                return result
            except :
               return False
