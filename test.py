# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 17:59:19 2019

@author: ADBUser
"""

from statemachine import StateMachine


door = {'locked' : {'key_right':'unlocked'},
        'unlocked' : {'key_left':'locked', 'open':'enter'},
        'enter': {}}

initial_state = 'locked'
dfa = StateMachine(door, initial_state)
dfa.report()
dfa.action('key_right')
dfa.action('open')