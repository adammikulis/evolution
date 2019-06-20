# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 13:05:28 2019

@author: ADBUser
"""
class Entity:
    
    def __init__(self, type='player', x_init=0, y_init=0):
        self.type = type
        self.x_init = x_init
        self.y_init = y_init

class Endocrine(Entity):

    def __init__(self, min_estrogen=0, max_estrogen=100):
        super().__init__(self)
        self.min_estrogen = min_estrogen
        self.max_estrogen = max_estrogen

test = Endocrine()
print(test.x_init, test.y_init, test.min_estrogen, test.max_estrogen)