import numpy as np

def setup_pixels():
    update_np_pixels()
    
def setup():
    global s
    size(200,200)
    s = [[]]
    
    background(0)
    load_np_pixels()
    setup_pixels()
    #code
    
def evaluate():
    global s
    #code to update neightbors-state
    
def transition():
    #code to apply the rules from
    #neighbors state
    update_np_pixels()
    
def draw():
    evaluate()
    transition()