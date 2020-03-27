import suitceyes
import time

with suitceyes.Vest("COM3") as vest:  
    vest.set_pin_value(0,255)
    time.sleep(2)