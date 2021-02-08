""" EE 250L Lab 02: GrovePi Sensors

Zhuoyao Chen

https://github.com/usc-ee250-spring2021/lab02-ZhuoyaoChen23
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
    PORT_rot = 0# A0: port connects encoder
    while True:
        #So we do not poll the sensors too quickly which may introduce noise,
        #sleep for a reasonable time of 200ms between each iteration.
        time.sleep(0.2)
	print(grovepi.ultrasonicRead(PORT)) # print sensor reading on terminal
	if grovepi.analogRead(PORT_rot) < grovepi.ultrasonicRead(PORT): # if no object within threshold
		setText_norefresh("%3dcm           \n%3dcm" % (grovepi.analogRead(PORT_rot),grovepi.ultrasonicRead(PORT)))
		setRGB(0,255,0)
        else: # if object falls within threshold
		setText_norefresh("%3dcm %s\n%3dcm" % (grovepi.analogRead(PORT_rot),"OBJ PRES",grovepi.ultrasonicRead(PORT)))
	        setRGB(255,0,0)
