# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 13:45:07 2019

@author: ADBUser
"""
from entity import Entity
import numpy as np
import random

class Activations:
    def step(self, x):
        if x > 0:
            return 1
        else:
            return 0
        return x
    def sigmoid(self, x):
        return 1.0 / (1 + np.exp(-x))
    
    def relu(self, x):
        if x >= 0:
            return x
        else:
            return 0

class Brain(Entity, Activations):
    def __init__(self):
        pass
    def sigmoid(self, x):
        return "test"
    def other(self, x):
        return super().sigmoid(x)
    



animal = Brain()
print(animal.sigmoid(10))
