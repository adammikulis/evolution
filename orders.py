# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 16:46:43 2019

@author: ADBUser
"""

from statemachine import StateMachine

class Orders(StateMachine):
    def __init__(self):
        # States for ADB Orders
        self.order_system = {'New' : {'place order':'In-Progress', 'delete':'Deleted'},
                        'Canceled' : {},
                        'Deleted' : {},
                        'In-Progress' : {'cancel':'Canceled', 'missed':'Missed',
                                         'fingerprinted':'Pending ABI Review'},
                        'Missed' : {'reschedule':'In-Progress', 'cancel':'Canceled'},
                        'Pending ABI Review' : {'approve':'Submitted to CBI', 'reject':'Rejected by ABI'},
                        'Rejected by ABI' : {},
                        'Submitted to CBI' : {'approve':'Completed', 'reject':'Rejected by CBI'},
                        'Rejected by CBI' : {},
                        'Completed' : {}}
        
        self.initial_state = 'New'
        super().__init__(self.order_system)


order = Orders()

# Main loop
while True:
    while order.running:
        order.get_action()
    choice = input('New order (y/n)? ')
    if choice == 'y' or choice == 'Y':
        order.current_state = order.initial_state
        order.report()
        order.running = True
    else:
        break