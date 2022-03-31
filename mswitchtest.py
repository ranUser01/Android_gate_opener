# This code is checks the states of gates
# The RPi.GPIO is the library designed for straight-forward use of GPIO pins in a raspberry pi
import RPi.GPIO as GPIO

# Setmode functions sets the mode in which the pins are called. In this work I use pins' number on the board as a
# referencing method.

GPIO.setmode(GPIO.BOARD)

# setwarnings disables inherit warnings, which are automatically generated whenever an attempt to use GPIO board is
# detected by the raspberry

GPIO.setwarnings(False)

# The following two lines initialise pins usage and determine the way they are used.Pins 16 and 18 are connected to
# the reed switches, so they are set as input pins.  In this case they are used as input pins. Thus, GPIO.IN is
# declared. Correspondingly, If they are used as output pins, then the GPIO.OUT would be declared. Pins 16 and 18 are
# connected to the reed switches, so they are set as input pins.

# GPIO.PUD_UP defines what should be amount of voltage delivered to the pins. It is essential in this case since they
# detect changes. When the circuit is closed, the voltage at the pin will remain constant, but when the circuit is
# closed then it will drop to 0 because the other end of switch is connected to the ground. If the initial voltage was
# set to be 0 in the beginning, then closing the circuit would not change the voltage. Hence, the change would be
# undetectable.

GPIO.setup(16, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, GPIO.PUD_UP)

# The code below checks whether the circuit is closed or open. In this case it identifies if the gate is closed.
# Whenever the voltage at the pin is 0, it means the circuit is closed, so the gate is closed. Otherwise the gate is
# open. After identification it prints the state of the gate and that information is later used in the phone
# application and such design made verifying the wiring much simple since this code can be used to do that.
try:
    if GPIO.input(16) == GPIO.LOW:
        print("Garage 1 is Closed")
    else:
        print("Garage 1 is open")

    if GPIO.input(18) == GPIO.LOW:
        print("Garage 2 is Closed")
    else:
        print("Garage 2 is open")


# KeyboardInterrupt is a combination of ctrl+C. Normally it is used to break the loop, but in this case where there
# is no loop it only is used because the try: function requires it.
except KeyboardInterrupt:

    # Cleanup resets all pins to the default state.
    GPIO.cleanup()
