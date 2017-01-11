from .import db


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(25))
    modelo = db.Column(db.String(25))
    tipo = db.Column(db.String(20))
    cilindrada = db.Column(db.String(10))
    cilindros = db.Column(db.String(5))
    cantidadpuertas = db.Column(db.String(10))
    capacidad = db.Column(db.String(10))