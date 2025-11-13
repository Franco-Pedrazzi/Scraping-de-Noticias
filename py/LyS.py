from flask import render_template,Blueprint, request, jsonify, redirect, url_for
from collections import namedtuple

from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

from py.db import db

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

SyL = Blueprint('SyL', __name__,template_folder='templates')

login_manager = LoginManager()

GMAIL_USER = "renaultcup0@gmail.com"
GMAIL_PASS = "ywer mdum zooi zvxm"
email= ""
@login_manager.user_loader
def load_user(email):
    return Usuario.query.get(email)



class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuario'
    email = db.Column(db.String(40),primary_key=True)
    contraseña = db.Column(db.String(200))

    def get_id(self):
        return self.email 
    
    def is_active(self):
        return True
    
class Verificacion(db.Model):
    __tablename__ = 'Verificacion'
    email = db.Column(db.String(40))
    codigo = db.Column(db.String(20), primary_key=True)
    nombre = db.Column(db.String(40))
    contra_codificada = db.Column(db.String(200))
    rango = db.Column(db.String(20))

class Login(FlaskForm):
    user = StringField('user', validators=[DataRequired()])
    password=StringField('password', validators=[DataRequired()])

class Signup(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    user = StringField('user', validators=[DataRequired()])
    password=StringField('password', validators=[DataRequired()])
                                              
class VC(FlaskForm):
    cod = StringField('codigo', validators=[DataRequired()])

                  
def login(form):
    email = form.user.data
    contraseña = form.password.data
    if not (email and contraseña):
        return "Faltan campos"
    usuario = Usuario.query.filter_by(email=email).first()
    if usuario==None:
        return "Contraseña o Email incorrecta/o"
    if not check_password_hash(usuario.contraseña, contraseña):
        return "Contraseña o Email incorrecta/o"
        

    login_user(usuario)
    return True

@SyL.route("/login", methods=['GET', 'POST'])
def login_url():
    form = Login()
    info=""
    if form.validate_on_submit():
        info=login(form)
        if info==True:
            return redirect('/')

    return render_template('signup and login/login.html',form=form,info=info)

