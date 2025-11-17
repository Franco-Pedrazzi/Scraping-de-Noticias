from flask import Blueprint, request, jsonify,redirect
import requests,webbrowser
from bs4 import BeautifulSoup
import sys,os
from urllib.parse import urljoin
import os
import json


class Noticia():
    def __init__(self,titulo,autor,fecha,a):
        self.titulo=titulo
        self.autor= autor
        self.fecha=fecha
        self.a=a
    def to_dict(self):
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "fecha": self.fecha,
            "link": self.a
        }
def scraping(inicio=False):
    noticias=[]
    if inicio or  not os.path.exists("noticias.json") :
        inicio=False
        url="https://www.lanacion.com.ar/"

        resp = requests.get(url)
        resp.raise_for_status()

        soup = BeautifulSoup(resp.text, "lxml")

        articulos = soup.select("div",class_="grid-item --1 --col-8 --col-md-3 --col-lg-3 --col-xl-4")



        for articulo in articulos:

            titulo_tag = articulo.select_one("h2",class_="text ln-text title --prumo --font-medium --font-m-l")  # algunos usan h2, otros h3
            titulo = titulo_tag.get_text(strip=True) if titulo_tag else None
            autor_tag=None
            if len(noticias)!=0:
                if titulo!=noticias[len(noticias)-1].titulo:
                    autor_tag = articulo.select_one("strong")
            else:
                autor_tag = articulo.select_one("strong")
            autor = autor_tag.get_text(strip=True) if autor_tag else None

            a_tag = articulo.select_one("a",class_="link ln-link flex flex-column --unstyled")
            a = a_tag.get("href") if a_tag else None
            if titulo and autor and a:
                a = urljoin("https://www.lanacion.com.ar", a)
                resp2 = requests.get(a)
                resp2.raise_for_status()

                soup2 = BeautifulSoup(resp2.text, "lxml")
                fecha_tag= soup2.find("time",class_="com-date --twoxs")
                fecha = fecha_tag.get_text(strip=True) if fecha_tag else None
                if fecha:
                    noticias.append(Noticia(titulo,autor,fecha,a))
        if os.path.exists("noticias.json"):
            os.remove("noticias.json")
        with open("noticias.json", 'w', encoding="utf-8") as f:
            json.dump([n.to_dict() for n in noticias], f, indent=4, ensure_ascii=False)
    else:
        with open("noticias.json", 'r', encoding="utf-8") as f:
            noticias = json.load(f)

    return noticias
