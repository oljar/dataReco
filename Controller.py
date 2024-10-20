#!/usr/bin/python
import matplotlib
import threading, time, subprocess, logging, minimalmodbus
from time import sleep
import serial
import re
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
import collections
import time
import csv
import sys
from threading import Thread
import os
import subprocess
import datetime
from tkinter.filedialog import asksaveasfile




class Controller:
    def __init__(self, model, view):

        self.instrument_1 = None
        self.instrument_2 = None
        self.instrument_3 = None
        self.instrument_4 = None
        self.instrument_5 = None
        self.instrument_6 = None
        self.instrument_7 = None
        self.instrument_8 = None
        self.instrument_9 = None
        self.instrument_10 = None
        self.instrument_11 = None
        self.instrument_12 = None
        self.instrument_13 = None
        self.instrument_14 = None
        self.instrument_15 = None

        self.time_out = 0.5


        self.writer = None
        self.parameter = tk.StringVar()
        self.model = model
        self.view = view
        self.model.mod_1_adr_var = tk.StringVar()

        self.t1 = time.time()
       
        ###
        

        self.model.save_control.set(True)

        self.conn_repeat_nr = 10

        self.n_header = 0

        self.led = 40








        
        


    def my_function(self):
        self.t2 = time.time()
        self.delta_t = (self.t2 - self.t1)
        self.time_s.popleft()
        self.time_s.append(self.delta_t)
        self.cycle_data()

        #  modbus settings

        

    ##########################################################################################################################################

   

    ##########################################################################################################################

   
   
    # Energy meter 1
    def settings_1(self):

        if self.view.radio_button_change_1_var.get() == 1:
            port_nr_win = str('com'+str(self.view.serial_port_var.get()))
            self.instrument_1 = minimalmodbus.Instrument(port_nr_win , 1)
        elif self.view.radio_button_change_1_var.get() == 2:
            self.instrument_1 = minimalmodbus.Instrument("/dev/ttyUSB"+str(self.view.serial_port_var.get()),1)
        self.instrument_1.serial.baudrate = 9600  # Baud
        self.instrument_1.serial.bytesize = 8
        self.instrument_1.serial.parity = serial.PARITY_NONE
        self.instrument_1.serial.stopbits = 1
        self.instrument_1.serial.timeout = self.time_out # second
        self.instrument_1.mode = minimalmodbus.MODE_RTU  # rtu or ascii mode
        # self.instrument_1.ers_before_each_transaction = True
        # self.instrument_1.close_port_after_each_call = True
  
    # Energy meter 2
    def settings_2(self):

        if self.view.radio_button_change_1_var.get() == 1:
            port_nr_win = str('com'+str(self.view.serial_port_var.get()))
            self.instrument_2 = minimalmodbus.Instrument(port_nr_win, 3)
        elif self.view.radio_button_change_1_var.get() == 2:
            self.instrument_2 = minimalmodbus.Instrument("/dev/ttyUSB"+str(self.view.serial_port_var.get()), 3)
        
        self.instrument_2.serial.baudrate = 9600  # Baud
        self.instrument_2.serial.bytesize = 8
        self.instrument_2.serial.parity = serial.PARITY_NONE
        self.instrument_2.serial.stopbits = 1
        self.instrument_2.serial.timeout = self.time_out # second
        self.instrument_2.mode = minimalmodbus.MODE_RTU  # rtu or ascii mode
        # self.instrument_1.ers_before_each_transaction = True
        # self.instrument_1.close_port_after_each_call = True
    


    def transfer_data(self):
        self.model.mod_1_adr_var = self.view.mod_1_adr_var.get()
        #self.model.dev_1_adr_var = self.view.dev_1_adr_var.get()

        self.model.mod_2_adr_var = self.view.mod_2_adr_var.get()
        #self.model.dev_2_adr_var = self.view.dev_2_adr_var.get()

        self.model.mod_3_adr_var = self.view.mod_3_adr_var.get()
        #self.model.dev_3_adr_var = self.view.dev_3_adr_var.get()

        self.model.mod_4_adr_var = self.view.mod_4_adr_var.get()
        #self.model.dev_4_adr_var = self.view.dev_4_adr_var.get()

        self.model.mod_5_adr_var = self.view.mod_5_adr_var.get()
        #self.model.dev_5_adr_var = self.view.dev_5_adr_var.get()

        self.model.mod_6_adr_var = self.view.mod_6_adr_var.get()
        #self.model.dev_6_adr_var = self.view.dev_6_adr_var.get()

        self.model.mod_7_adr_var = self.view.mod_7_adr_var.get()
        #self.model.dev_7_adr_var = self.view.dev_7_adr_var.get()


        self.model.mod_8_adr_var = self.view.mod_8_adr_var.get()
        #self.model.dev_8_adr_var = self.view.dev_8_adr_var.get()

        self.model.mod_9_adr_var = self.view.mod_9_adr_var.get()
        #self.model.dev_9_adr_var = self.view.dev_9_adr_var.get()

        self.model.mod_10_adr_var = self.view.mod_10_adr_var.get()
        self.model.mod_10_adr_var = str(int(self.model.mod_10_adr_var)-1)+'9'
        #self.model.dev_10_adr_var = self.view.dev_10_adr_var.get()

        self.model.mod_11_adr_var = self.view.mod_11_adr_var.get()
        self.model.mod_11_adr_var = str(int(self.model.mod_11_adr_var)-1)+'9'
        #self.model.dev_11_adr_var = self.view.dev_11_adr_var.get()

        self.model.mod_12_adr_var = self.view.mod_12_adr_var.get()
        self.model.mod_12_adr_var = str(int(self.model.mod_12_adr_var)-1)+'9'
        #self.model.dev_12_adr_var = self.view.dev_12_adr_var.get()

        self.model.mod_13_adr_var = self.view.mod_13_adr_var.get()
        self.model.mod_13_adr_var = str(int(self.model.mod_13_adr_var)-1)+'9'
        #self.model.dev_13_adr_var = self.view.dev_13_adr_var.get()

        self.model.mod_14_adr_var = self.view.mod_14_adr_var.get()
        self.model.mod_14_adr_var = str(int(self.model.mod_14_adr_var)-1)+'9'
        #self.model.dev_14_adr_var = self.view.dev_14_adr_var.get()

        self.model.mod_15_adr_var = self.view.mod_15_adr_var.get()
        self.model.mod_15_adr_var = str(int(self.model.mod_15_adr_var)-1)+'9'
        #self.model.dev_15_adr_var = self.view.dev_15_adr_var.get()

        self.model.mod_16_adr_var = self.view.mod_16_adr_var.get()
        self.model.mod_16_adr_var = str(int(self.model.mod_16_adr_var)-1)+'9'
        #self.model.dev_16_adr_var = self.view.dev_16_adr_var.get()

        self.model.mod_17_adr_var = self.view.mod_17_adr_var.get()
        self.model.mod_17_adr_var = str(int(self.model.mod_17_adr_var)-1)+'9'
        #self.model.dev_17_adr_var = self.view.dev_17_adr_var.get()

        self.model.mod_18_adr_var = self.view.mod_18_adr_var.get()
        self.model.mod_18_adr_var = str(int(self.model.mod_18_adr_var)-1)+'9'
        #self.model.dev_18_adr_var = self.view.dev_18_adr_var.get()


    def cycle_data(self):
        if self.view.chk_btn1_var.get() == 1 :

            for i in range(self.conn_repeat_nr):
                    
                try:
                    #self.settings_1()
                    #self.model.data_1 = self.instrument_1.read_float(registeraddress = (int(self.model.mod_1_adr_var)),functioncode = 4 )
                    self.model.data_1 = 1
                    break
                except Exception:
                    print(f'Błąd pobrania data_1 {i}')
                

            
            for i in range(self.conn_repeat_nr):
                try:
                    #self.settings_1()
                    #self.model.data_2 = self.instrument_1.read_float(registeraddress = (int(self.model.mod_2_adr_var)),functioncode = 4 )
                    self.model.data_2 = 2
                    break
                except Exception:
                    print(f'Błąd pobrania data_2 {i}')


            for i in range(self.conn_repeat_nr):
                try:
                    #self.settings_1()
                    #self.model.data_3 = self.instrument_1.read_float(registeraddress = (int(self.model.mod_3_adr_var)),functioncode = 4 )
                    self.model.data_3 = 3
                    break
                except Exception:
                    print(f'Błąd pobrania data_3 {i}')

            for i in range(self.conn_repeat_nr):
                
                try:
                    #self.settings_1()
                    #self.model.data_4 = self.instrument_1.read_float(registeraddress = (int(self.model.mod_4_adr_var)),functioncode = 4 )
                    self.model.data_4 = 4
                    break
                except Exception:
                    print(f'Błąd pobrania data_4 {i}')

            for i in range(self.conn_repeat_nr):
                
                try:
                    #self.settings_1()
                    #self.model.data_5 = self.instrument_1.read_float(registeraddress = (int(self.model.mod_5_adr_var)),functioncode = 4 )
                    self.model.data_5 = 5
                    break
                except Exception:
                    print(f'Błąd pobrania data_5 {i}')

            for i in range(self.conn_repeat_nr):

                try:
                    #self.settings_1()
                    #self.model.data_6 = self.instrument_1.read_float(registeraddress =  (int(self.model.mod_6_adr_var)),functioncode = 4 )
                    self.model.data_6 = 6
                    break
                except Exception:
                    print(f'Błąd pobrania data_6 {i}')

    
        
            for i in range(self.conn_repeat_nr):
                try:
                    #self.settings_1()
                    #self.model.data_7 = self.instrument_1.read_float(registeraddress =  (int(self.model.mod_7_adr_var)),functioncode = 4 )
                    self.model.data_7 = 7
                    break
                except Exception:
                    print(f'Błąd pobrania data_7 {i}')
                    
                
                    
            for i in range(self.conn_repeat_nr):
                try:
                    #self.settings_1()
                    #self.model.data_8 = self.instrument_1.read_float(registeraddress =  (int(self.model.mod_8_adr_var)),functioncode = 4 )
                    self.model.data_8 = 8
                    break
                except Exception:
                    print(f'Błąd pobrania data_8 {i}')
        

       
           
            for i in range(self.conn_repeat_nr):
                try:
                    #self.settings_1()
                    #self.model.data_9 = self.instrument_1.read_float(registeraddress = int(self.model.mod_9_adr_var),functioncode = 4 )
                    self.model.data_9 = 9
                    break
                except Exception:
                    print(f'Błąd pobrania data_9 {i}')


        if self.view.chk_btn2_var.get() == 1 :

            for i in range(self.conn_repeat_nr):

                try:
                    #self.settings_2()
                    #self.model.data_10 = self.instrument_2.read_register(registeraddress = (int(self.model.mod_10_adr_var)),functioncode = 3 )
                    self.model.data_10 = 10
                    break
                except Exception:
                    print(f'Błąd pobrania data_10 {i}')

            for i in range(self.conn_repeat_nr):
                try:
                    #self.settings_2()
                    #self.model.data_11 = self.instrument_2.read_register(registeraddress = (int(self.model.mod_11_adr_var)),functioncode = 3 )
                    self.model.data_11 = 11
                    break
                except Exception:
                    print(f'Błąd pobrania data_11 {i}')

            for i in range(self.conn_repeat_nr):

                try:
                    #self.settings_2()
                    #self.model.data_12 = self.instrument_2.read_register(registeraddress =  (int(self.model.mod_12_adr_var)),functioncode = 3 )
                    self.model.data_12 = 12
                    break
                except Exception:
                
                    print(f'Błąd pobrania data_12 {i}')

        

            for i in range(self.conn_repeat_nr):

                try:
                    #self.settings_2()
                    #self.model.data_13 = self.instrument_2.read_register(registeraddress = int(self.model.mod_13_adr_var),functioncode = 3 )
                    self.model.data_13 = 13
                    break
                except Exception:
                    print(f'Błąd pobrania data_13 {i}')

            for i in range(self.conn_repeat_nr):
                try:
                    #self.settings_2()
                    #self.model.data_14 = self.instrument_2.read_register(registeraddress = int(self.model.mod_14_adr_var),functioncode = 3 )
                    self.model.data_14 = 14
                    break
                except Exception:
                    print(f'Błąd pobrania data_14 {i}')
        

        
            for i in range(self.conn_repeat_nr):
                try:
                    #self.settings_2()
                    #self.model.data_15 = self.instrument_2.read_register(registeraddress = int(self.model.mod_15_adr_var) ,functioncode = 3 )
                    self.model.data_15 = 15
                    break
                except Exception:
                    print(f'Błąd pobrania data_15 {i}')

            for i in range(self.conn_repeat_nr):
                try:
                    #self.settings_2()
                    #self.model.data_16 = self.instrument_2.read_register(registeraddress =  int(self.model.mod_16_adr_var) ,functioncode = 3 )
                    self.model.data_16 = 16
                    break
                except Exception:
                    print(f'Błąd pobrania data_16 {i}')

            for i in range(self.conn_repeat_nr):
                try:
                    #self.settings_2()
                    #self.model.data_17 = self.instrument_2.read_register(registeraddress =  int(self.model.mod_17_adr_var) ,functioncode = 3 )
                    self.model.data_17 = 17
                    break
                except Exception:
                    print(f'Błąd pobrania data_17 {i}')

            for i in range(self.conn_repeat_nr):
                try:
                    #self.settings_2()
                    #self.model.data_18 = self.instrument_2.read_register(registeraddress =  int(self.model.mod_18_adr_var) ,functioncode = 3 )
                    self.model.data_18 = 18
                    break
                except Exception:
                    print(f'Błąd pobrania data_18 {i}')



    def start_save(self):
        self.t2s = time.time()
        print('start')

    


 
    
        
    def usb_name(self):
        rpistr = "ls /media/pi/"
        proc = subprocess.Popen(rpistr, shell=True, preexec_fn=os.setsid, stdout=subprocess.PIPE)

 
        line = proc.stdout.readline()
        dysk_name = str(line.decode().strip()) 
        return dysk_name


    
    def save_data(self):
        
        self.t1s = time.time()
        self.cycle_data()
        date_time_split = datetime.datetime.strptime(self.view.must_time_target.get(), "%Y-%m-%d %H:%M:%S")
        time_string = (f'{date_time_split.hour:02d}:{date_time_split.minute:02d}:{date_time_split.second:02d}')
        date_string = (f'{date_time_split.year}-{date_time_split.month:02d}-{date_time_split.day:02d}')
        t = self.t1s - self.t2s
        t = str(round(t, 1))
        t = t.replace('.', ',')

        if self.view.chk_btn1_var.get() == 1 and self.view.time_overtake_signal.get():

            self.model.data_1 = 0
            self.model.data_2 = 0
            self.model.data_3 = 0
            self.model.data_4 = 0
            self.model.data_5 = 0
            self.model.data_6 = 0
            self.model.data_7 = 0
            self.model.data_8 = 0
            self.model.data_9 = 0

        elif self.view.chk_btn1_var.get() == 1 and not self.view.time_overtake_signal.get():
        
            self.model.data_1 = round(self.model.data_1, 2)
            self.model.data_1 = str(self.model.data_1).replace('.', ',')

            self.model.data_2 = round(self.model.data_2, 2)
            self.model.data_2 = str(self.model.data_2).replace('.', ',')

            self.model.data_3 = round(self.model.data_3, 2)
            self.model.data_3 = str(self.model.data_3).replace('.', ',')

            self.model.data_4 = round(self.model.data_4, 2)
            self.model.data_4 = str(self.model.data_4).replace('.', ',')

            self.model.data_5 = round(self.model.data_5, 2)
            self.model.data_5 = str(self.model.data_5).replace('.', ',')

            self.model.data_6 = round(self.model.data_6, 2)
            self.model.data_6 = str(self.model.data_6).replace('.', ',')

            self.model.data_7 = round(self.model.data_7, 2)
            self.model.data_7 = str(self.model.data_7).replace('.', ',')

            self.model.data_8 = round(self.model.data_8, 2)
            self.model.data_8 = str(self.model.data_8).replace('.', ',')

            self.model.data_9 = round(self.model.data_9, 2)
            self.model.data_9 = str(self.model.data_9).replace('.', ',')
        
        else:
            self.model.data_1 = 'nb'
            self.model.data_2 = 'nb'
            self.model.data_3 = 'nb'
            self.model.data_4 = 'nb'
            self.model.data_5 = 'nb'
            self.model.data_6 = 'nb'
            self.model.data_7 = 'nb'
            self.model.data_8 = 'nb'
            self.model.data_9 = 'nb'

        
     
        if self.view.chk_btn2_var.get() == 1 and  self.view.time_overtake_signal.get():
            
            self.model.data_10 = 0
            self.model.data_11 = 0
            self.model.data_12 = 0
            self.model.data_13 = 0
            self.model.data_14 = 0
            self.model.data_15 = 0
            self.model.data_16 = 0
            self.model.data_17 = 0
            self.model.data_18 = 0


        elif self.view.chk_btn2_var.get() == 1 and not self.view.time_overtake_signal.get():
         
            self.model.data_10 = round(self.model.data_10, 2)
            self.model.data_10 = str(self.model.data_10).replace('.', ',')

            self.model.data_11 = round(self.model.data_11, 2)
            self.model.data_11 = str(self.model.data_11).replace('.', ',')

            self.model.data_12 = round(self.model.data_12, 2)
            self.model.data_12 = str(self.model.data_12).replace('.', ',')
            
            self.model.data_13 = round(self.model.data_13, 2)
            self.model.data_13 = str(self.model.data_13).replace('.', ',')

            self.model.data_14 = round(self.model.data_14, 2)
            self.model.data_14 = str(self.model.data_14).replace('.', ',')

                    
            self.model.data_15 = round(self.model.data_15,2)
            self.model.data_15 = str(self.model.data_15).replace('.', ',')

            self.model.data_16 = round(self.model.data_16,2)
            self.model.data_16 = str(self.model.data_16).replace('.', ',')

            self.model.data_17 = round(self.model.data_17,2)
            self.model.data_17 = str(self.model.data_17).replace('.', ',')

            self.model.data_18 = round(self.model.data_18,2)
            self.model.data_18 = str(self.model.data_18).replace('.', ',')

        else:
           
            self.model.data_10 = 'nb'
            self.model.data_11 = 'nb'
            self.model.data_12 = 'nb'
            self.model.data_13 = 'nb'
            self.model.data_14 = 'nb'
            self.model.data_15 = 'nb'
            self.model.data_16 = 'nb'
            self.model.data_17 = 'nb'
            self.model.data_18 = 'nb'

        print(f'zapisano - {self.model.data_1}')
        print(f'zapisano - {self.model.data_2}')           
        print(f'zapisano - {self.model.data_3}')
        print(f'zapisano - {self.model.data_4}')
        print(f'zapisano - {self.model.data_5}')
        print(f'zapisano - {self.model.data_6}')           
        print(f'zapisano - {self.model.data_7}')
        print(f'zapisano - {self.model.data_8}')
        print(f'zapisano - {self.model.data_9}')
        print(f'zapisano - {self.model.data_10}')           
        print(f'zapisano - {self.model.data_11}')
        print(f'zapisano - {self.model.data_12}')
        print(f'zapisano - {self.model.data_13}')
        print(f'zapisano - {self.model.data_14}')           
        print(f'zapisano - {self.model.data_15}')
        print(f'zapisano - {self.model.data_16}')
        print(f'zapisano - {self.model.data_17}')
        print(f'zapisano - {self.model.data_18}')


        self.data = [date_string,time_string,t, self.model.data_1, self.model.data_2, self.model.data_3,
                     self.model.data_4, self.model.data_5, self.model.data_6, self.model.data_7,
                     self.model.data_8, self.model.data_9, self.model.data_10, self.model.data_11, self.model.data_12,
                     self.model.data_13, self.model.data_14, self.model.data_15 , self.model.data_16,self.model.data_17,
                     self.model.data_18]
        
        #self.led_blinking_on()

        # with open('/media/pi/'+self.usb_name()+'/data.csv', mode='a', newline='') as file:
        #     header = ['date','time','t',int(self.model.mod_1_adr_var),int(self.model.mod_2_adr_var),int(self.model.mod_3_adr_var),int(self.model.mod_4_adr_var), int(self.model.mod_5_adr_var),
        #               int(self.model.mod_6_adr_var), int(self.model.mod_7_adr_var), int(self.model.mod_8_adr_var), int(self.model.mod_9_adr_var), int(self.model.mod_10_adr_var), int(self.model.mod_11_adr_var),
        #               int(self.model.mod_12_adr_var), int(self.model.mod_13_adr_var), int(self.model.mod_14_adr_var), int(self.model.mod_15_adr_var),int(self.model.mod_16_adr_var),int(self.model.mod_17_adr_var),
        #               int(self.model.mod_18_adr_var)]
        #     writer = csv.writer(file, delimiter=';')
        #     self.n_header += 1
        #     if self.n_header == 1:
        #         writer.writerow(header)
        #     writer.writerow(self.data)

        print(self.data)
#        self.led_blinking_off()

 
    


    def save_cfg(self):
        dict_to_save = {}
        dict_to_save['1'] = str(self.view.mod_1_adr_var.get())
        dict_to_save['2'] = str(self.view.mod_2_adr_var.get())
        dict_to_save['3'] = str(self.view.mod_3_adr_var.get())
        dict_to_save['4'] = str(self.view.mod_4_adr_var.get())
        dict_to_save['5'] = str(self.view.mod_5_adr_var.get())
        dict_to_save['6'] = str(self.view.mod_6_adr_var.get())
        dict_to_save['7'] = str(self.view.mod_7_adr_var.get())
        dict_to_save['8'] = str(self.view.mod_8_adr_var.get())
        dict_to_save['9'] = str(self.view.mod_9_adr_var.get())
        dict_to_save['10'] = str(self.view.mod_10_adr_var.get())
        dict_to_save['11'] = str(self.view.mod_11_adr_var.get())
        dict_to_save['12'] = str(self.view.mod_12_adr_var.get())
        dict_to_save['13'] = str(self.view.mod_13_adr_var.get())
        dict_to_save['14'] = str(self.view.mod_14_adr_var.get())
        dict_to_save['15'] = str(self.view.mod_15_adr_var.get())
        dict_to_save['16'] = str(self.view.mod_16_adr_var.get())
        dict_to_save['17'] = str(self.view.mod_17_adr_var.get())
        dict_to_save['18'] = str(self.view.mod_18_adr_var.get())


        file55 = asksaveasfile(initialdir='C:\\Users\oljar\PycharmProjects\jupiter02', defaultextension='.txt',mode='w', filetypes=[('TXT Files', '*.txt')])
        with open(file55.name, 'w', encoding='utf-8') as f:
            for key, value in dict_to_save.items():
                f.write(f'{key}={value}\n')

    def set_save_control(self):

        self.model.save_control.set(False)

    def start_thread(self):
        self.model.save_control = True

    def stop_thread(self):
        self.model.save_control = False

        # self.settings()
        # self.make()
    