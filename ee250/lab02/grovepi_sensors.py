""" EE 250L Lab 02: GrovePi Sensors

List team members here.

Insert Github repository link here.
"""

"""python3 interpreters in Ubuntu (and other linux distros) will look in a 
default set of directories for modules when a program tries to `import` one. 
Examples of some default directories are (but not limited to):
  /usr/lib/python3.5
  /usr/local/lib/python3.5/dist-packages

The `sys` module, however, is a builtin that is written in and compiled in C for
performance. Because of this, you will not find this in the default directories.
"""
import sys
import time
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')
from grove_rgb_lcd import*
import grovepi
setRGB(0,255,0)
"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 grovepi_sensors.py` in terminal, this if-statement will 
be true"""
if __name__ == '__main__':
    PORT = 4    # D4: port connects sensor
    PORT_rot = 0; # A0: port connects encoder
    grovepi.pinMode(PORT_rot,"INPUT") # new code
    message = " " # string contains message to be displayed on LCD
    flag_obj_pres = 0 # flag: when there's object within threshold, set to 1; otherwise set to 0
    while True:
        #So we do not poll the sensors too quickly which may introduce noise,
        #sleep for a reasonable time of 200ms between each iteration.
        time.sleep(0.2)
	#print(grovepi.analogRead(PORT_rot)) # test code: print encoder reading
	print(grovepi.ultrasonicRead(PORT)) # print sensor reading on terminal
	if grovepi.analogRead(PORT_rot) < grovepi.ultrasonicRead(PORT): # if no object within threshold
		if flag_obj_pres == 1: # if there was object within threshold
			setText(" ") # clear display
		flag_obj_pres = 0
		setText_norefresh("%3dcm\n%3dcm" % (grovepi.ultrasonicRead(PORT),grovepi.analogRead(PORT_rot)))
		setRGB(0,255,0)
	else:
		if flag_obj_pres == 0: # if there was object within threshold
			setText(" ") # clear display
		flag_obj_pres = 1
		setText_norefresh("%3dcm %s\n%3dcm" % (grovepi.ultrasonicRead(PORT),"OBJ PRES",grovepi.analogRead(PORT_rot)))
		setRGB(255,0,0)
