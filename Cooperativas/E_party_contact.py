# -*- coding: utf-8 -*-

import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, Numeric,func,update,text
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion

base = declarative_base()
class E_party_contact(base):

    __tablename__="party_contact"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_party = Column(Integer)
    tel_principal = Column(String)
    tel_secundario = Column(String)
    email = Column(String)
    session = ""

    def __init__(self):
        obj_conexion =  configuracion()
        engine=create_engine(obj_conexion.config())
        Session= sessionmaker(bind=engine)
        self.session=Session()

    @classmethod
    def guardar(cls, obj_E_party_contact):
            new_record = cls()
            new_record.id_party = obj_E_party_contact.id_party
            new_record.tel_principal = obj_E_party_contact.tel_principal
            new_record.tel_secundario = obj_E_party_contact.tel_secundario
            new_record.email = obj_E_party_contact.email

            try:
                new_record.session.add(new_record)
                new_record.session.commit()
                new_record.session.close()
                return True
            except :
                new_record.session.rollback()
                new_record.session.close()
                return False

    def get_party_contact(self, id_party):
        obj_party = self.session.query(E_party_contact).filter_by(id_party=id_party).first()
        self.session.close()
        return obj_party


    def actualizar(self, obj_E_party_contact):
        new_record = self.get_party_contact(obj_E_party_contact.id_party)
        new_record.id_party = obj_E_party_contact.id_party
        new_record.tel_principal = obj_E_party_contact.tel_principal
        new_record.tel_secundario = obj_E_party_contact.tel_secundario
        new_record.email = obj_E_party_contact.email

        try:
            self.session.add(new_record)
            self.session.commit()
            self.session.close()
            return True
        except :
            self.session.rollback()
            self.session.close()
            return False
