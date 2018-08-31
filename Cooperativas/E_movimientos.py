
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, Numeric,func,update,text,Boolean
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion

base = declarative_base()
class E_movimientos(base):

    __tablename__="movimientos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nro_factura = Column(String)
    total = Column(Numeric)
    concepto = Column(String)
    detalle = Column(String)
    fecha = Column(DateTime)
    iva = Column(Boolean)
    tipo = Column(String)
    session = ""

    def __init__(self):
        obj_conexion =  configuracion()
        engine=create_engine(obj_conexion.config())
        Session= sessionmaker(bind=engine)
        self.session=Session()

    @classmethod
    def guardar(cls, obj_movimientos):
        new_record = cls()
        new_record.nro_factura = obj_movimientos.nro_factura
        new_record.total = obj_movimientos.total
        new_record.concepto = obj_movimientos.concepto
        new_record.detalle = obj_movimientos.detalle
        new_record.fecha = obj_movimientos.fecha
        new_record.iva = obj_movimientos.iva
        new_record.tipo = obj_movimientos.tipo

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
        obj_coop= self.session.query(E_movimientos).all()
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






