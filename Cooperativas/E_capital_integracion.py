# -*- coding: utf-8 -*-

import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, Numeric,func,update,text
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion

base = declarative_base()
class E_capital_integracion(base):

    __tablename__="capital_integracion"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_asoc = Column(Integer)
    pesos = Column(Numeric)
    fec_cuota = Column(DateTime)
    nro_cuota = Column(Integer)
    tipo_aporte = Column(String)
    estado = Column(String)
    session = ""

    def __init__(self):
        obj_conexion =  configuracion()
        engine=create_engine(obj_conexion.config())
        Session= sessionmaker(bind=engine)
        self.session=Session()

    @classmethod
    def guardar(cls, obj_E_cooperativa):
            new_record = cls()
            new_record.id_asoc = obj_E_cooperativa.id_asoc
            new_record.pesos = obj_E_cooperativa.pesos
            new_record.fec_cuota = str(obj_E_cooperativa.fec_cuota)
            new_record.nro_cuota = obj_E_cooperativa.nro_cuota
            new_record.tipo_aporte = obj_E_cooperativa.tipo_aporte
            new_record.estado = obj_E_cooperativa.estado

            try:
                new_record.session.add(new_record)
                new_record.session.commit()
                new_record.session.close()
                return True
            except :
                new_record.session.rollback()
                new_record.session.close()
                return False


    def get_cap_integra(self,id_asoc):
        list_cap_integra = self.session.query(E_capital_integracion).filter_by(id_asoc=id_asoc).order_by(E_capital_integracion.nro_cuota).all()
        self.session.close()
        return list_cap_integra

    def borrar(self,id_cap_integra):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        obj=self.session.query(E_capital_integracion).filter(E_capital_integracion.id==id_cap_integra).first()
        self.session.delete(obj)
        self.session.commit()

    def pagar(self, nro_cuota,aporte_tipo,id_asoc):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        new_record = self.session.query(E_capital_integracion).filter_by(nro_cuota=nro_cuota,
                                                                         id_asoc=id_asoc).first()

        new_record.tipo_aporte = aporte_tipo
        new_record.estado = "Pagada"

        try:
            self.session.add(new_record)
            self.session.commit()
            self.session.close()
            return True
        except:
            new_record.session.rollback()
            new_record.session.close()
            return False
