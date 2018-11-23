import time
from socket import *
from datetime import datetime
from sense_hat import SenseHat

sense = SenseHat()


BROADCAST_TO_PORT = 7250
s = socket(AF_INET, SOCK_DGRAM)

s.setsockopt(SOL_SOCKET,SO_BROADCAST, 1)

while True:
  print(sense.accell_raw)
  time.sleep(1)


#while True:
  #s.sendto(bytes(data,"UTF-8"), ('<broadcast>', BROADCAST_TO_PORT))
  #acceleration = sense.get_accelerometer_raw()
  #print(sense.accel_raw)

	#print("x={0}, y={1}, z={2}".format(x, y, z))
	#time.sleep(1)
  
  

