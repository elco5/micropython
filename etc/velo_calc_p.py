
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

print(T_2_mph(0.125))

print(mph_2_T(40))


