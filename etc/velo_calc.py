
import numpy as np
pi = np.pi


def mph_2_T(mph):
    d = 0.7
    v_ms = mph/2.23694
    return np.round((pi*d)/v_ms,3)


def T_2_mph(T):
    d = 0.7
    v = (pi*d)/T
    return np.round(v*2.23694,3)
    

''' conclusion: sample switch and 
accept intterupts in at least
120 ms
'''

print(f'bike is restricted to 19 mph. interval: {mph_2_T(19)}')
# 19mph -> 259 ms
print(f'hack the sensor so bike thinks it is going 15 mph. interval: {mph_2_T(15)}') 
# 15mph -> 328 ms
print(T_2_mph(0.180))



