# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 22:27:53 2021

@author: Lenovo
"""

from time import time, sleep

class TrafficLight:
    color='Красный'
    
    def __init__(self,time_r,time_y,time_g):
        self.time_r=time_r
        self.time_y=time_y
        self.time_g=time_g
        self.run()
    
    def run(self):
        self.curtime=time()
        while True:
            if self.color=='Красный':
                while time()-self.curtime<self.time_r:
                    print(self.color)
                    sleep(1)
                
                
                self.color='Желтый' 
                self.curtime=time()
            elif self.color=='Желтый':
                while time()-self.curtime<self.time_y:
                    print(self.color)
                    sleep(1)
                    
                self.color='Зеленый'
                self.curtime=time()
            else: #зеленый
                while time()-self.curtime<self.time_g:
                    print(self.color)
                    sleep(1)
                    
                self.color='Красный'
                self.curtime=time()
                
            
        
    
t_r=7
t_y=2
t_g=15
obj=TrafficLight(t_r, t_y, t_g)
                    