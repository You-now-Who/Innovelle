# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from app         import db
from flask_login import UserMixin

class Users(db.Model, UserMixin):

    __tablename__ = 'Users'

    id       = db.Column(db.Integer,     primary_key=True)
    user     = db.Column(db.String(64),  unique = True)
    name     = db.Column(db.String(64),  unique = False)
    age     = db.Column(db.Integer,     unique = False)
    email    = db.Column(db.String(120), unique = True)
    password = db.Column(db.String(500))

    def __init__(self, user, email, password):
        self.user       = user
        self.password   = password
        self.email      = email
        # self.name      = name
        # self.age      = age

    def __repr__(self):
        return str(self.id) + ' - ' + str(self.user)

    def save(self):

        # inject self into db session    
        db.session.add ( self )

        # commit change and save the object
        db.session.commit( )

        return self 
