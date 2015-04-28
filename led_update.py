import requests
import json
import RPi.GPIO as GPIO
import time
import math

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(3, GPIO.OUT) #pin3 = Green LED
GPIO.setup(4, GPIO.OUT) #pin4 = Red LED
GPIO.setup(17, GPIO.OUT) #pin17 = Blue LED

end = time.time()
start_time = 0
x = True
temp = 0

#make sure to check the commented conditional statement!
#it's to make sure the user is not allowed to go overboard!

while True: #This will pull from the server forever!
	# if total_time < end:
		r = requests.get('https://fathomless-wave-8947.herokuapp.com/read/0')
		if r.status_code == 200: # this checks for internet connection
			#print(r.url)
			data = r.text
			data_arr = json.loads(data)
			#print(data)
			print(data_arr)
			print(data_arr["vacant"])
			total_time = end - start_time
			#print(total_time)
			days = total_time // 86400
			hours = total_time // 3600 % 24
			mins = total_time // 60 % 60
			seconds = total_time % 60
			print(str(math.ceil(days)) + ' day(s)')
			print(str(math.ceil(hours)) + ' hour(s)')
			print(str(math.ceil(mins)) + ' minute(s)')
			print(str(math.ceil(seconds)) + ' second(s)')
			if str(data_arr["vacant"]) == "True":
				if x == True:
					start_time = end
					x = False
				#this is if the spot is available (GREEN LIGHT)
				#using pin 3 to correspond to available
				print("true!")
				GPIO.output(3, 1) # green light is on
				GPIO.output(4, 0) # red light is off
				GPIO.output(17,0) # blue light is off
			elif str(data_arr["vacant"]) == "False":
				end = time.time()
				#this is if the spot is occupied (RED LIGHT)
				#using pin 4 to correspond to occupied
				print("false!")
				GPIO.output(3, 0) # green light is off
				GPIO.output(4, 1) # red light is on
				GPIO.output(17,0) # blue light is off
				x = True
			#else: # used for error checking
			#	print("error on " + data_arr["vacant"])
		else: # this confirms out of order
			GPIO.output(3, 0) # green light is off
			GPIO.output(4, 0) # red light is off
			GPIO.output(17,1) # blue light is on
	# else: #the time is up, need to set a way to reset this!
	# 	temp += 1
	# 	print(temp)
	# 	if temp > 10000: #turns the red light on to indicate time is up
	# 		GPIO.output(3,0)
	# 		GPIO.output(4,1)
	# 		GPIO.output(17,0)
GPIO.cleanup()
