import math
def g(x):
    return math.sin(x) + math.sin(3*x)/3
def hill_climb(start, step=0.25):
    x = start                     
    while True:
        left  = x - step          
        right = x + step          
        best = left if g(left) > g(right) else right
        if g(best) <= g(x):       
            return x, g(x)        
        x = best                  
print("from x=0.5 :", hill_climb(0.5))
print("from x=4.0 :", hill_climb(4.0))