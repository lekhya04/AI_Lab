import math, random
def g(x):
    return math.sin(x) + math.sin(3*x)/3
def simulated_annealing(start, T=1.5, cool=0.82, T_min=0.03):
    random.seed(2)            
    x = start
    while T > T_min:          
        candidate = x + random.uniform(-1, 1)   
        candidate = max(0.0, min(6.0, candidate))   
        dE = g(candidate) - g(x)      
        if dE > 0:
            accept = True             
        else:
            P = math.exp(dE / T)      
            accept = random.random() < P
        if accept:
            x = candidate
        T = T * cool                  
    return x, g(x)
print("SA from x=4.75 :", simulated_annealing(4.75))