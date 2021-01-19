# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 00:13:56 2021

@author: Lenovo
"""

class _Car:
    def __init__(self,speed,color,name,is_police):
        self.speed=speed
        self.color=color
        self.name=name
        self.is_police=is_police
    
    def go(self):
        print('Автомобиль {0} поехал со скоростью {1} км/ч'.format(self.name,self.speed))
    
    def stop(self):
        print('Автомобиль {0} остановился'.format(self.name))
    
    def turn(self,direction):
        print('Автомобиль {0} повернул {1}'.format(self.name,direction))
    
    def show_speed(self):
        print('Автомобиль {0}. Скорость: {1} км/ч'.format(self.name,self.speed))
    
class _TownCar(_Car):
    speed_limit=60
    def show_speed(self):
        if self.speed>self.speed_limit:
            print("Автомобиль {0}. Скорость: {1} км/ч. Превышаем?".format(self.name,self.speed))
        else:
            print("Автомобиль {0}. Скорость: {1} км/ч".format(self.name,self.speed))
        
class _SportCar(_Car):
    pass

class _WorkCar(_TownCar):
    speed_limit=40

class _PoliceCar(_Car):
    pass


n_GTR=_SportCar(230,'Серебристый','Nissan Silvia',False)
n_Police=_PoliceCar(250, 'Красный', 'Toyota Supra',True)
n_Autobus=_TownCar(50,'Белый','Ikarus',False)
n_Kamaz_Uborschik=_WorkCar(45, 'Оранжевый', 'КАМАЗ-5320',False)

n_Autobus.go()
n_GTR.stop()
n_Kamaz_Uborschik.turn("Направо")
n_Police.show_speed()
n_Autobus.show_speed() #не отрабатывает по непонятной причине (все методы определены)
n_Kamaz_Uborschik.show_speed() #затт здесь измененный метод унаследовался