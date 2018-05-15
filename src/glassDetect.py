#!/usr/bin/python
import RPi.GPIO as GPIO
import time
from datetime import datetime

crackInput = 27
crackOutput = 17
protectInput = 4
protectOutput = 22

def init():
    print '[' + str(datetime.now()) + '] Glass detection start'
    # using physical pin number
    # GPIO.setmode(GPIO.BOARD)
    # using Broadcom pun number
    GPIO.setmode(GPIO.BCM)
    # show which pin be used to detect glass
    GPIO.setup(crackInput, GPIO.IN)
    print '[' + str(datetime.now()) + '] Pin of glass detcet input is: ' + str(crackInput)
    GPIO.setup(crackOutput, GPIO.OUT)
    print '[' + str(datetime.now()) + '] Pin of glass detect output is: ' + str(crackOutput)
    GPIO.output(crackOutput, True)
    # show which pin be used to detect case
    GPIO.setup(protectInput, GPIO.IN)
    print '[' + str(datetime.now()) + '] Pin of case protect input is: ' + str(protectInput)
    GPIO.setup(protectOutput, GPIO.OUT)
    print '[' + str(datetime.now()) + '] Pin of case protect output is: ' + str(protectOutput)
    GPIO.output(protectOutput, True)
    # init finish
    print '[' + str(datetime.now()) + '] Glass detection initializated'

def breakCheck(input, output):
    # High = 1, Low = 0
    # NC/COM Always connect, if grass crack will make it disconnect.
    if GPIO.input(input) != 1:
        print '[' + str(datetime.now()) + '] Detect glass crack'

def caseProtect(input, output):
    # High = 1, Low = 0
    # NC/COM Always connect, if case open will make it disconnect.
    if GPIO.input(input) != 1:
        print '[' + str(datetime.now()) + '] Detect case open'

# Main function
init()
try:
    while True:
        breakCheck(crackInput, crackOutput)
        caseProtect(protectInput, protectOutput)
        time.sleep(.5)
except KeyboardInterrupt:
    # If CTRL+C is pressed, exit cleanly:
    print '[' + str(datetime.now()) + '] Glass detection close'
except Exception as e:
    # If others exception happened
    print '[' + str(datetime.now()) + '] Glass detection error: ' + e
finally:
    # cleanup all GPIO
    GPIO.cleanup()
    print '[' + str(datetime.now()) + '] Glass detection GPIO cleaned'