# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 00:02:34 2021

@author: Lenovo
"""

money={
       "wage": 0,
       "bonus": 0
}

class Worker:    
    def __init__(self,name,surname,position,wage,bonus):
        self.name=name
        self.surname=surname
        self.position=position
        self._money=money
        self._money["wage"]=wage
        self._money["bonus"]=bonus
    

class Position(Worker):    
    def get_full_name(self):
        print(self.surname+" "+self.name)
    
    def calcul_income(self):
        print("Общий доход: {0} р.".format(self._money["wage"]+self._money["bonus"]))

i=Position("Ivan","Ivanov","Programmer",60000,8000)
i.get_full_name()
i.calcul_income()