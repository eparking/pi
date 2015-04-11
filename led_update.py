import requests
import json
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(4, GPIO.OUT) #pin4 = Green LED
GPIO.setup(17, GPIO.OUT) #pin17 = Red LED

r = requests.get('https://fathomless-wave-8947.herokuapp.com/read/0')
#print(r.url)

data = r.text

data_arr = json.loads(data)

print(data)
print(data_arr)

while 1==1: #This will pull from the server forever!
	if data_arr["vacant"] == True:
		print("True!")
		time.sleep(2)
		GPIO.output(4, 1)
		GPIO.output(17, 0)
	else:
		print("False!")
		time.sleep(2)
		GPIO.output(4, 0)
		GPIO.output(17, 1)

GPIO.cleanup()
