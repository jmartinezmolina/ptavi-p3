#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# Practica3 --- Ejercicio 3   JAVIER MARTINEZ MOLINA

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.width = ""
        self.height = ""
        self.background_color = ""
        self.region = ""
        self.id = ""
        self.top = ""
        self.bottom = ""
        self.left = ""
        self.right = ""
        self.img = ""
        self.src = ""
        self.begin = ""
        self.dur = ""
        self.end = ""
        self.audio = ""
        self.textstream = ""
        self.fill = ""
        
    def startElement(self, name, attrs):
    
        if name == 'root-layout':
            self.width = attrs.get('width', "")
            self.height = attrs.get('height', "")
            self.background_color = attrs.get('background-color', "")
            print self.width
            print self.height
            print self.background_color
            
        elif name == 'region':
            self.id = attrs.get('id', "")
            self.top = attrs.get('top', "")
            self.bottom = attrs.get('bottom', "")
            self.left = attrs.get('left', "")
            self.right = attrs.get('right', "")
            print self.id
            print self.top
            print self.bottom
            print self.left
            print self.right
            
        elif name == 'img':
            self.src = attrs.get('src', "")
            self.region = attrs.get('region', "")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur', "")
            self.end = attrs.get('end', "")
            print self.src
            print self.region
            print self.begin
            print self.dur
            print self.end

        elif name == 'audio':
            self.src = attrs.get('src', "")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur', "")
            print self.src
            print self.begin
            print self.dur
            
        elif name == 'textstream':
            self.src = attrs.get('src', "")
            self.region = attrs.get('region', "")
            self.fill = attrs.get('fill', "")
            print self.src
            print self.region
            print self.fill

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    chandler = SmallSMILHandler()
    parser.setContentHandler(chandler)
    parser.parse(open('karaoke.smil'))
