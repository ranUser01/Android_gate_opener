# this code is used to open a gate
# The two libraries below are used to both make a pause in code execution and to retrieve information about current
# time, which is saved in the log file.
import time
from datetime import datetime

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# An impulse must be send from from raspberry pi to a relay board in order to activate a relay. In order to close the
# relay switch, electricity must be send to it. Therefore, the pin is set up as an
# output pin and HIGH.
GPIO.setup(13, GPIO.OUT)
GPIO.output(13, GPIO.LOW)

try:
    # The pin is set up to HIGH, so it has big enough voltage across it to activate a relay.
    GPIO.output(13, GPIO.HIGH)
    # The execution stops for 1 second
    time.sleep(1)
    # After the pause the relay needs to be turned off, so the state of the pin is set back to LOW
    GPIO.output(13, GPIO.LOW)
    # All actions regarding opening/closing should be registered. Therefore, the txt.file is opened in append mode.
    # The application should not overwrite already saved data but just another line of it.
    logfile = open("/home/pi/test/log", "a")
    # The information saved is which button was clicked and what time it happened
    logfile.write(datetime.now().strftime("     Gate 2 button clicked -- %Y/%m/%d -- %H:%M\n"))
    logfile.close()

except KeyboardInterrupt:
    GPIO.cleanup()