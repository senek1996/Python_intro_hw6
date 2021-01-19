# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 00:50:55 2021

@author: Lenovo
"""

class Stationery:
    def draw(self,title):
        self.title=title
        print("Я вывожу "+self.title)
    
class Pen:
    def draw(self,title):
        self.title=title
        print("Ручка: я вывожу "+self.title)

class Pencil:
    def draw(self,title):
        self.title=title
        print("Карандаш: я вывожу "+self.title)

class Handle:
    def draw(self,title):
        self.title=title
        print("Маркер: я вывожу "+self.title)
    
a=Pen()
b=Pencil()
c=Handle()

a.draw("бла")
b.draw("блабла")
c.draw("блаблабла")