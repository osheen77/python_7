# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 22:06:49 2020

@author: Osheen
"""





def printing(unprinted_designs, completed_designs):
    while unprinted_designs:
         current_design = unprinted_designs.pop()
         print("The design : " +current_design + " is being printed.")
         completed_designs.append(current_design)

def complete(completed_designs):
    print("the following designs are complete; ")
    for completed in completed_designs:
        print(completed)
        

unprinted_designs=['i-phonoe', 'tablet','stand','chair','phone-book']
completed_designs=[]