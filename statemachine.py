# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:19:30 2019

@author: ADBUser
"""
# Takes a dictionary of states/transitions and initial state

class StateMachine:

    # Dict format: {'state0': {'action1':'state1', 'action2':'state2'},
    #               'state1': {'action2':'state2'}.
    #               'state2': {'action0':'state0'}}
    
    def __init__(self, states={}, initial_state=''):
        self.states = states
        if initial_state == '':
            self.current_state = list(self.states.keys())[0]
        else:
            self.current_state = initial_state
        self.inputs = []
        self.running = True
        print(self.report())
    
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
        # Prevent runtime error from unavailable action
        try:
            self.current_state = self.states[self.current_state][input]
            self.report()
        except KeyError:
            print("No such transition!")
    
    # Returns the actions that are possible at current state
    def avail_actions(self):
        # Return available actions
        if (self.states[self.current_state]):
            return (list(self.states[self.current_state].keys()))
        # If there are no more actions available
        else:
            return "No more actions"
    
    def avail_states(self):
        if (self.states[self.current_state]):
            return (list(self.states[self.current_state].values()))
        # If there are no more states to transition to
        else:
            self.running = False
            return "Terminal state"
    # Prints current state and available actions
    def report(self):
        print("\nCurrent state: %s\nAvailable actions: %s\nAvailable states: %s\n" 
              % (self.current_state, self.avail_actions(), self.avail_states()))
        
    def get_action(self):
        choice = input("What action to take? ")
        self.action(choice)