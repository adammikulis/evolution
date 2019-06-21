# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 11:05:55 2019

@author: ADBUser
"""
import numpy as np
from statemachine import StateMachine

class Entity(StateMachine):
    def __init__(self, size=100, health=100, max_health=100, energy=100,
                 max_energy=100, stomach=0, max_stomach=100, mobility=100,
                 max_mobility=100, mouth_size=100, max_mouth=100, temp=30, min_temp=25, max_temp=35):
        # States for ADB Orders
        self.entity = {'Resting' : {'rest':'Resting', 'gather':'Gathering'},
                       'Gathering' : {'gather':'Gathering', 'rest':'Resting', 'eat':'Eating'},
                       'Eating' : {'eat':'Eating', 'gather':'Gathering', 'rest':'Resting'}}
        self.initial_state = 'Resting'
        self.health = health
        self.energy = energy
        self.stomach = stomach
        self.mobility = mobility
        self.mouth_size = mouth_size
        super().__init__(self.entity)

