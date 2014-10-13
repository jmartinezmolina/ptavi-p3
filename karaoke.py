#!/usr/bin/python
# -*- coding: utf-8 -*-

# Ejercicios 4, 5, 6 --- Práctica 3 JAVIER MARTÍNEZ MOLINA

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import os
import sys
import smallsmilhandler


class KaraokeLocal(smallsmilhandler.SmallSMILHandler):

    def __init__(self, fichero):
        parser = make_parser()
        chandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(chandler)
        parser.parse(open(fichero))
        self.lista_dic = chandler.get_tags()

    def __str__(self):
        salida = ""
        for dic in self.lista_dic:
            salida += dic["name"] + "\t"
            for etiqueta in dic:
                if dic["name"] != dic[etiqueta] and dic[etiqueta] != "":
                    salida += etiqueta + "=" + '"' + dic[etiqueta] + '"' + "\t"
            salida += "\n"
        return salida

    def do_local(self):
        for dic in self.lista_dic:
            for etiqueta in dic:
                if etiqueta == "src":
                    recurso = dic[etiqueta]
                    os.system("wget -q " + recurso)
                    elem_div = recurso.split('/')
                    dic[etiqueta] = elem_div[-1]

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Usage: python karaoke.py file.smil.\n')
        raise SystemExit

    karaoke = KaraokeLocal(sys.argv[1])
    print karaoke
    karaoke.do_local()
    print karaoke
