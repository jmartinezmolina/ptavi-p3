#!/usr/bin/python
# -*- coding: utf-8 -*-

# Ejercicio4 --- Práctica 3 JAVIER MARTÍNEZ MOLINA

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import os
import sys
import smallsmilhandler


if len(sys.argv) != 2:
    print('Usage: python karaoke.py file.smil.\n')
    raise SystemExit

parser = make_parser()
chandler = smallsmilhandler.SmallSMILHandler()
parser.setContentHandler(chandler)
parser.parse(open(sys.argv[1]))
lista_dic = chandler.get_tags()


for dic in lista_dic:
    for etiqueta in dic:
        if etiqueta == "src":
            recurso = dic[etiqueta]
            os.system("wget -q " + recurso)
            elem_div = recurso.split('/')
            dic[etiqueta] = elem_div[-1]

for dic in lista_dic:
    print dic["name"] + "\t",
    for etiqueta in dic:
        if dic["name"] != dic[etiqueta] and dic[etiqueta] != "":
            print etiqueta + "=" + '"' + dic[etiqueta] + '"' + "\t",
    print 
            




