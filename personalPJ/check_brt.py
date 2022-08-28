#!/usr/bin/env python3

import ADC0832
import time

def init():
    ADC0832.setup()

def loop():
    while True:
        #The ADC0832 has two channels
        #res = ADC0832.getResult()   <-- It reads channel 0 by default. Equivalent to getResult(0)
        #res = ADC0832.getResult(1)  <-- Use this to read the second channel

        res = ADC0832.getResult() - 80
        if res < 0:
            res = 0
        if res > 100:
            res = 100
        print ('res = %d' % res)
        time.sleep(60)
        # 照度67以下なら照明ON
        if (res < 67):
            file_name = "/home/pi/light_on.py"
            content = open(file_name).read()
            exec(content)
            exit()

        #time.sleep(10)

if __name__ == '__main__':
    init()
    try:
        loop()
    except KeyboardInterrupt:
        ADC0832.destroy()
        print ('Cleanup ADC!')
