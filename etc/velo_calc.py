
import numpy as np
pi = np.pi


def mph_2_T(mph):
    d = 0.7
    v_ms = mph/2.23694
    return (pi*d)/v_ms


def T_2_mph(T):
    d = 0.7
    v = (pi*d)/T
    return v*2.23694
    

''' conclusion: sample switch and 
accept intterupts in at least
120 ms
'''

<<<<<<< HEAD
print(T_2_mph(0.125))
=======
print(f'bike is restricted to 19 mph. interval: {mph_2_T(19)}')
print(f'hack the sensor so bike thinks it is going 15 mph. interval: {mph_2_T(15)}')



print(T_2_mph(0.12))
>>>>>>> 4d1e0c9b68d774f1344467670b59a3d1384ffbf0

print(mph_2_T(40))


