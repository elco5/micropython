two_pi_f = 2*3.14159*60
E = 240

def vars_2_C(vars):
    vars = abs(vars)
    Xc = (E**2)/vars
    C =  1/(two_pi_f*Xc)
    return C 

def vars_2_L(vars):
   
    Xl = (E**2)/vars
    L =  Xl/two_pi_f
    return L


def vars_2_X(vars):
   
    if vars < 0:
        ret = vars_2_C(vars)
        print(ret, 'Farad')
        return  ret
         
    if vars >= 0:
        ret = vars_2_L(vars)
        print(ret, 'Henry')
        return  ret 




vars_2_X(1754)