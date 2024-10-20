import minimalmodbus
import serial
import time
import RPi.GPIO as GPIO
instrument_3 = minimalmodbus.Instrument("/dev/ttyUSB0",3)
#self.instrument_1 = minimalmodbus.Instrument('com4', self.model.dev_8_adr_var)
instrument_3.serial.baudrate = 9600  # Baud
instrument_3.serial.bytesize = 8
instrument_3.serial.parity = serial.PARITY_NONE
instrument_3.serial.stopbits = 1
instrument_3.serial.timeout = 0.5# second
instrument_3.mode = minimalmodbus.MODE_RTU  # rtu or ascii mode

#data_1 = instrument_3.read_float(registeraddress = (0),functioncode = 4 )  
data_9 = instrument_3.read_register(registeraddress = 16109 ,functioncode = 3 )#
print(data_9)
# import RPi.GPIO as GPIO

# instrument_4 = minimalmodbus.Instrument("/dev/ttyUSB0",1)
# #self.instrument_1 = minimalmodbus.Instrument('com4', self.model.dev_8_adr_var)
# instrument_4.serial.baudrate = 9600  # Baud
# instrument_4.serial.bytesize = 8
# instrument_4.serial.parity = serial.PARITY_NONE
# instrument_4.serial.stopbits = 1
# instrument_4.serial.timeout = 0.5# second
# instrument_4.mode = minimalmodbus.MODE_RTU  # rtu or ascii mode




# content = 'okjhihih'

# #destination = "bbb.txt" 
# destination = '/media/pi/DYSK/a.txt'

# with open(destination, "w") as usb_file:
#         usb_file.write(content)

# file = open('/media/pi/DYSK/b.txt',"r",encoding = "utf-8")
# print(file.read())

# print('ok')#!/usr/bin/env python

########################################
# import os
# import subprocess

# rpistr = "ls /media/pi"
# proc = subprocess.Popen(rpistr, shell=True, preexec_fn=os.setsid,stdout=subprocess.PIPE)
# line = proc.stdout.readline()
# print (line.rstrip())


import subprocess
import os

rpistr = "ls /media/pi/"
proc = subprocess.Popen(rpistr, shell=True, preexec_fn=os.setsid, stdout=subprocess.PIPE)

# Odczytaj wszystkie linie z wyj�cia procesu
# for line in proc.stdout:
#     print(line.decode().strip())  # Dekoduj bajty na ci�g znak�w i usu� znak nowej linii

line = proc.stdout.readline()
#print(line.decode().strip()) 

#############################################

# def usb_name():
#         rpistr = "ls /media/pi/"
#         proc = subprocess.Popen(rpistr, shell=True, preexec_fn=os.setsid, stdout=subprocess.PIPE)

#         # Odczytaj wszystkie linie z wyj�cia procesu
#         # for line in proc.stdout:
#         #     print(line.decode().strip())  # Dekoduj bajty na ci�g znak�w i usu� znak nowej linii
#         line = proc.stdout.readline()
#         dysk_name = str(line.decode().strip()) 
#         return dysk_name

# print(usb_name())



# self.instrument_1.ers_before_each_transaction = True
# self.instrument_1.close_port_after_each_call = True

#a=instrument_3.read_register(registeraddress = 16139,functioncode=3)
# a=instrument_3.read_float(registeraddress = 20 ,functioncode=3)
# print (a)
# # instrument_3.write_float(registeraddress = 20, value=2)


# b=instrument_4.read_float(registeraddress = 20 ,functioncode=3)
# print (b)