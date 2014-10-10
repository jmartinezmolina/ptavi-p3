#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# Practica3 --- Ejercicio 3   JAVIER MARTINEZ MOLINA

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.etiquetas = {
            'root-layout': ['width', 'height', 'background-color'],
            'region': ['id', 'top', 'bottom', 'left', 'right'],
            'img': ['src', 'region', 'begin', 'dur', 'end'],
            'audio': ['src', 'begin', 'dur'],
            'textstream': ['src', 'region', 'fill']}

        self.list_etiquetas = []

    def startElement(self, name, attrs):

        dic = {}
        if name in self.etiquetas:
            dic["name"] = name
            for atributo in self.etiquetas[name]:
                dic[atributo] = attrs.get(atributo, "")
            self.list_etiquetas.append(dic)

    def get_tags(self):

        return self.list_etiquetas

if __name__ == "__main__":

    parser = make_parser()
    chandler = SmallSMILHandler()
    parser.setContentHandler(chandler)
    parser.parse(open('karaoke.smil'))
    print chandler.get_tags()
