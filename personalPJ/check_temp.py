import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=16)

while True:
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)

    time.sleep(60)

	 # 26.5度以上なら扇風機ON
    if (result.temperature >= 27.5):
        file_name = "/home/pi/dyson_on_swing.py"
        content = open(file_name).read()
        exec(content)
        exit()

    #time.sleep(600)
