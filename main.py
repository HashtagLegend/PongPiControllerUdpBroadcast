import time
from socket import *
from datetime import datetime
from sense_hat import SenseHat

sense = SenseHat()
sense.clear


BROADCAST_TO_PORT = 7250
s = socket(AF_INET, SOCK_DGRAM)

s.setsockopt(SOL_SOCKET,SO_BROADCAST, 1)

while True:
	acceleration = sense.get_accelerometer_raw()
	x = acceleration['x']
	y = acceleration['y']
	z = acceleration['z']
	x=round(x, 0)
	y=round(y, 0)
	z=round(z, 0)
	data = ("x={0}, y={1}, z={2}".format(x, y, z))
	s.sendto(bytes(data,"UTF-8"), ('<broadcast>', BROADCAST_TO_PORT))
	time.sleep(0)

  
  
