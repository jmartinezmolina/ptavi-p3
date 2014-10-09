#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# Practica3 --- Ejercicio 3   JAVIER MARTINEZ MOLINA

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

#root-layout (width, height, background-color)
#region (id, top, bottom, left, right)
#img (src, region, begin, dur)
#audio (src, begin, dur)
#textstream (src, region)
    def __init__(self):

        self.width = ''
        self.height = ''
        self.background-color = ''
        self.region = ''
        self.id = ''
        self.top = ''
        self.bottom = ''
        self.left = ''
        self.right = ''
        self.img = ''
        self.src = ''
        self.begin = ''
        self.dur = ''
        self.audio = ''
        self.textstream = ''
        
    def startElement(self, name, attrs):
    
        if name == 'root-layout':
            self.width = attrs.get('width', "")
            self.height = attrs.get('height', "")
            self.background-color = attrs.get('background-color', "")
            
        elif name == 'region':
            self.id = attrs.get('id', "")
            self.top = attrs.get('top', "")
            self.bottom = attrs.get('bottom', "")
            self.left = attrs.get('left', "")
            self.right = attrs.get('right', "")
            
        elif name == 'img':
            self.src = attrs.get('src', "")
            self.region = attrs.get('region', "")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur', "")
            
        elif name == 'audio':
        elif name == 'textstream':
            
            
            
