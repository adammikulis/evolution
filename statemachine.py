# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:19:30 2019

@author: ADBUser
"""

class StateMachine:
    # Takes a dictionary of states/transitions and initial state
    def __init__(self, states={}, initial_state=''):
        self.states = states
        self.current_state = initial_state
        self.inputs = []
    
    # Other manner of initializing state dictionary
    def load_states(self, states):
        self.states = states
    
    # View current state
    def view_state(self):
        return self.current_state
    
    # Manually set the current state
    def set_state(self, state):
        self.current_state = state
        self.report()
    
    # Perform an action
    def action(self, input):
        try:
            self.current_state = self.states[self.current_state][input]
            self.report()
        except KeyError:
            print("No such transition!")
    
    # Returns the actions that are possible at current state
    def avail_actions(self):
        for value in self.states:
            if (self.states[self.current_state]):
                return (list(self.states[self.current_state]))
            else:
                return "Terminal state"
    
    # Prints current state and available actions
    def report(self):
        print("Current state: %s, Available actions: %s" % (self.current_state, self.avail_actions()))