# https://docs.micropython.org/en/latest/reference/isr_rules.html?highlight=timer%20callback

print('Simple Schedule demo...')

from machine import Timer
import micropython
import time



def program_function(prog_func_args):
    ''' This function will run in normal program time.
    It cannot be a bound method of an object because
    the interrupt handler cannot allocate memory. To get
    around this, call a reference to the bound method and 
    define the reference in the class definition of the object '''
    # 'code to execute in main program goes here'
    print('program_function with args: ', prog_func_args)


def interrupt_handler(tim):  # Hard IRQ
    '''This function handles the hard IRQ by
    by scheduling a call to another
    higher-level function that  
    runs in normal program time.
    '''
    micropython.schedule(program_function, 'prog_func_args')




t1 = Timer(1)

t1.init(period=1000, mode=Timer.PERIODIC, callback=interrupt_handler) 

