import os 
from sqlalchemy import create_engine
import urllib

class Config(object):
    SECRET_KEY='Clave nueva'
    SESION_COOKIE_SECURE=False

class DevelopmentConfig(Config):
        DEBUG=True
        SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:270901@127.0.0.1:3306/idgs803'
        SQLALCHEMY_TRACK_MODIFICATIONS=False
