import time
from socket import *
from datetime import datetime
from sense_hat import SenseHat

sense = SenseHat()


BROADCAST_TO_PORT = 7250
s = socket(AF_INET, SOCK_DGRAM)

s.setsockopt(SOL_SOCKET,SO_BROADCAST, 1)

while True:
  data = "Current time" + str(datatime.now)
  s.sendto(bytes(data,"UTF-8"), ('<broadcast>', BROADCAST_TO_PORT))
  print(data)
  time.sleep(4)
  sense.show_message("send")

