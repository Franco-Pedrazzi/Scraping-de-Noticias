# py/rutas.py
from flask import render_template,Blueprint
import base64
from py.db import db
from py.Scraping import scraping
import requests,webbrowser
from bs4 import BeautifulSoup
import sys,os
from urllib.parse import urljoin

rutas = Blueprint('rutas', __name__, template_folder='templates')
noticias=[]
@rutas.route("/")
def Index():
    noticias=scraping()
    return render_template(
        'Index.html',noticias=noticias,
        Len=len(noticias)
                )



