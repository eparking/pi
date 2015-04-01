import RPi.GPIO()
#import time - Necessary only if timer is going to be used

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 4 # This is the pin number. Most likely it
#		  will be adjusted
GPIO.setup(led, GPIO.OUT)

GPIO.output(led, 1) # args: (pin #, 1 = ON or 0 = OFF)
#time.sleep(5) - Need import time for this line
GPIO.output(led, 0) # args: (pin #, 1 = ON or 0 = OFF)

GPIO.cleanup() # No idea what this does, but it's good
#				 to have, apparently