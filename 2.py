# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 22:54:10 2021

@author: Lenovo
"""

class Road:
    
    mass=0 #в кг
    
    def __init__(self,leng,width):
        #ВСЕ ИЗМЕРЕНИЯ В МЕТРАХ
        self.leng=leng
        self.width=width
    
    def calcul_mass_asph(self,thk,density):
        #вычисление массы асфальта для покрытия дороги
        #thk - толщина слоя асфальта в сантиметрах, density - масса 1 м^2 асфальта и толщиной 1 см
        self.mass=self.leng*self.width*thk*density
    
obj=Road(5000,20)
obj.calcul_mass_asph(5,25)
print('Масса асфальта для покрытия дороги: {0} т.'.format(obj.mass/1000))