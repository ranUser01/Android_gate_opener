# this code is responsible for tracking states of the gates
# the process of opening and closing gates is carried out by individual pieces of code
import time
from datetime import datetime
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
# relay 1 setup
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, GPIO.HIGH)
# relay 2 setup
GPIO.setup(13, GPIO.OUT)
GPIO.output(13, GPIO.HIGH)
# Reed switch 1 setup
GPIO.setup(16, GPIO.IN, GPIO.PUD_UP)
# Reed switch 2 setup
GPIO.setup(18, GPIO.IN, GPIO.PUD_UP)

# Opening logfile and stating start time of the programme
logfile = open("/home/pi/test/log", "a")
logfile.write(datetime.now().strftime("     Program Starting -- %Y/%m/%d -- %H:%M\n"))
logfile.close()
try:
    while 1 >= 0:
        # Reed switch 1 closed

        if GPIO.input(16) == GPIO.HIGH:
            logfile = open("/home/pi/test/log", "a")
            logfile.write(datetime.now().strftime("     Gate 1 is open -- %Y/%m/%d -- %H:%M\n"))
            logfile.close()

        # Reed switch 2 closed
        if GPIO.input(18) == GPIO.HIGH:
            logfile = open("/home/pi/test/log", "a")
            logfile.write(datetime.now().strftime("     Gate 2 is open -- %Y/%m/%d -- %H:%M\n"))
            logfile.close()

        # Reed switch 1 open
        if GPIO.input(16) == GPIO.LOW:
            logfile = open("/home/pi/test/log", "a")
            logfile.write(datetime.now().strftime("     Gate 1 is closed -- %Y/%m/%d -- %H:%M\n"))
            logfile.close()

        # Reed switch 2 open
        if GPIO.input(18) == GPIO.LOW:
            logfile = open("/home/pi/test/log", "a")
            logfile.write(datetime.now().strftime("     Gate 2 is closed -- %Y/%m/%d -- %H:%M\n"))
            logfile.close()
        time.sleep(300)

except KeyboardInterrupt:
    logfile = open("/home/pi/test/log", "a")
    logfile.write(datetime.now().strftime("     Log Program Shutdown -- %Y/%m/%d -- %H:%M\n"))
    logfile.close()
    GPIO.cleanup()
