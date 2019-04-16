import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
import time    # Import the sleep function from the time module

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14, GPIO.OUT)    # Red cable
GPIO.setup(18, GPIO.OUT)    # Green cable

for i in range(0, 1):
    GPIO.output(18,GPIO.LOW)
    GPIO.output(14,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(14, GPIO.LOW)  # Turn off red
    
    time.sleep(5)
    GPIO.output(14,GPIO.LOW)
    GPIO.output(18,GPIO.HIGH)   # Turn on green
    print("Green on, red off")
    time.sleep(8)
    GPIO.output(18,GPIO.LOW)
                 # Wait 1s

    #GPIO.output(14, GPIO.HIGH)  # Turn on red
    #GPIO.output(18,GPIO.LOW)   # Turn off green
    #print("Green on, red off")
    
                # Wait 1s

GPIO.output(14, GPIO.LOW)

