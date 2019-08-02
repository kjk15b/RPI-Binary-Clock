import time
import RPi.GPIO as GPIO
import datetime

'''
This class is a simple driver to convert time to binary values and to display
them to an LED matrix

Kolby Kiesling
kjk15b@acu.edu

07 / 14 / 2019

'''

class clock():
	def __init__(self, hour0, hour1, hour2, hour3, min0, min1, min2, min3, buzzer):
		self.hour0 = hour0
		self.hour1 = hour1
		self.hour2 = hour2
		self.hour3 = hour3
		self.min0 = min0
		self.min1 = min1
		self.min2 = min2
		self.min3 = min3
		self.buzzer = buzzer

	def initializeGPIO(self):
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.hour0, GPIO.OUT)
		GPIO.setup(self.hour2, GPIO.OUT)
		GPIO.setup(self.hour3, GPIO.OUT)
		GPIO.setup(self.min0, GPIO.OUT)
		GPIO.setup(self.min1, GPIO.OUT)
		GPIO.setup(self.min2, GPIO.OUT)
		GPIO.setup(self.min3, GPIO.OUT)
		GPIO.setup(self.buzzer, GPIO.OUT)
		return

	def clear_clock(self):
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.hour0, GPIO.OUT)
		GPIO.setup(self.hour2, GPIO.OUT)
		GPIO.setup(self.hour3, GPIO.OUT)
		GPIO.setup(self.min0, GPIO.OUT)
		GPIO.setup(self.min1, GPIO.OUT)
		GPIO.setup(self.min2, GPIO.OUT)
		GPIO.setup(self.min3, GPIO.OUT)
		GPIO.setup(self.buzzer, GPIO.OUT)
		GPIO.output(self.hour0, GPIO.LOW)
		GPIO.output(self.hour1, GPIO.LOW)
		GPIO.output(self.hour2, GPIO.LOW)
		GPIO.output(self.hour3, GPIO.LOW)
		GPIO.output(self.min0, GPIO.LOW)
		GPIO.output(self.min1, GPIO.LOW)
		GPIO.output(self.min2, GPIO.LOW)
		GPIO.output(self.min3, GPIO.LOW)
		return

	def chime(self, chirps):
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.hour0, GPIO.OUT)
		GPIO.setup(self.hour2, GPIO.OUT)
		GPIO.setup(self.hour3, GPIO.OUT)
		GPIO.setup(self.min0, GPIO.OUT)
		GPIO.setup(self.min1, GPIO.OUT)
		GPIO.setup(self.min2, GPIO.OUT)
		GPIO.setup(self.min3, GPIO.OUT)
		GPIO.setup(self.buzzer, GPIO.OUT)
		for i in range(chirps):
			GPIO.output(self.buzzer, GPIO.HIGH)
			time.sleep(1)
			GPIO.output(self.buzzer, GPIO.LOW)
			return

	def clock_start(self):
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.hour0, GPIO.OUT)
		GPIO.setup(self.hour2, GPIO.OUT)
		GPIO.setup(self.hour3, GPIO.OUT)
		GPIO.setup(self.min0, GPIO.OUT)
		GPIO.setup(self.min1, GPIO.OUT)
		GPIO.setup(self.min2, GPIO.OUT)
		GPIO.setup(self.min3, GPIO.OUT)
		GPIO.setup(self.buzzer, GPIO.OUT)
		now = datetime.datetime.now() # collect the current time
		self.clear_clock(self)
		if (now.hour == 0) or (now.hour == 12):
			GPIO.output(self.hour3, GPIO.HIGH)
			GPIO.output(self.hour2, GPIO.HIGH)
		elif (now.hour == 1) or (now.hour == 13):
			GPIO.output(self.hour0, GPIO.HIGH)
		elif (now.hour == 2) or (now.hour == 14):
			GPIO.output(self.hour1, GPIO.HIGH)
		elif (now.hour == 3) or (now.hour == 15):
			GPIO.output(self.hour0, GPIO.HIGH)
			GPIO.output(self.hour1, GPIO.HIGH)
		elif (now.hour == 4) or (now.hour == 16):
			GPIO.output(self.hour2, GPIO.HIGH)
		elif (now.hour == 5) or (now.hour == 17):
			GPIO.output(self.hour2, GPIO.HIGH)
			GPIO.output(self.hour0, GPIO.HIGH)
		elif (now.hour == 6) or (now.hour == 18):
			GPIO.output(self.hour2, GPIO.HIGH)
			GPIO.output(self.hour1, GPIO.HIGH)
		elif (now.hour == 7) or (now.hour == 19):
			GPIO.output(self.hour2, GPIO.HIGH)
			GPIO.output(self.hour1, GPIO.HIGH)
			GPIO.output(self.hour0, GPIO.HIGH)
		elif (now.hour == 8) or (now.hour == 20):
			GPIO.output(self.hour3, GPIO.HIGH)
		elif (now.hour == 9) or (now.hour == 21):
			GPIO.output(self.hour3, GPIO.HIGH)
			GPIO.output(self.hour0, GPIO.HIGH)
		elif (now.hour == 10) or (now.hour == 22):
			GPIO.output(self.hour3, GPIO.HIGH)
			GPIO.output(self.hour1, GPIO.HIGH)
		elif (now.hour == 11) or (now.hour == 23):
			GPIO.output(self.hour3, GPIO.HIGH)
			GPIO.output(self.hour1, GPIO.HIGH)
			GPIO.output(self.hour0, GPIO.HIGH)

		if (now.minute >= 0) and (now.minute < 15):
			GPIO.output(self.min0, GPIO.HIGH)
			self.chime(now.hour)
		elif (now.minute >= 15) and (now.minute < 30):
			GPIO.output(self.min1, GPIO.HIGH)
		elif (now.minute >= 30) and (now.minute < 45):
			GPIO.output(self.min2, GPIO.HIGH)
		elif (now.minute >= 45) and (now.minute < 60):
			GPIO.output(self.min3, GPIO.HIGH)

		time.sleep(60)
		return
