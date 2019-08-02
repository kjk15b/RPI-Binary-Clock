#!/bin/python
'''
This program serves as the main function to call the led clock class

Kolby Kiesling
kjk15b@acu.edu

07 / 14 / 2019
'''
import datetime
import led_clock_driver as clk
import time

def main():
	h0, h1, h2, h3, m0, m1, m2, m3, buzzer = 3, 7, 5, 8, 10, 12, 11, 13, 15
	clock = clk.clock(h0, h1, h2, h3, m0, m1, m2, m3, buzzer)
	clock.initializeGPIO()
	while True:
		now = datetime.datetime.now()
		if (now.minute == 0) or (now.minute == 15) or (now.minute == 30) or (now.minute == 45) or (now.minute == 60):
			clock.clock_start()

main()
