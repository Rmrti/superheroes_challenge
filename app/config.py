# app/config.py
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///superheroes.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
