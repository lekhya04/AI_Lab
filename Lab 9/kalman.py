x = 20.0              
P = 4.0               
Q = 1.0                
R = 4.0                
readings = [22.0, 21.0, 23.0]
for step in range(len(readings)):
    z = readings[step]    
    x_pred = x           
    P_pred = P + Q       
    K = P_pred / (P_pred + R)  
    difference = z - x_pred
    correction = K * difference
    x = x_pred + correction
    P = (1 - K) * P_pred
    print("Reading", step + 1, "sensor", z,
          "estimate", round(x, 4), "K", round(K, 4),
          "variance", round(P, 4))