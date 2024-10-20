import matplotlib
import re
import tkinter as tk
from tkinter import ttk
import tkinter.font as font
import time, subprocess
import data_source
from Controller import Controller
from Model import Model
from data_source import *
import datetime
from TimeGenerator import *
import time

from tkinter.filedialog import asksaveasfile
from tkinter import messagebox

window = tk.Tk()

window.title("AHU_exam  ver-1.1.2")
window.geometry('455x600')

tab_parent = ttk.Notebook(window)
tab0 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)

get_data = GetData()


class View(ttk.Frame):
    def __init__(self, parent):

        self.generator = None
        self.time_generator = None
        self.time_system_switch = tk.BooleanVar()
        self.time_system_switch.set(False)
        self.first_loop = tk.BooleanVar()
        self.first_loop.set(False)

        super().__init__(parent)

        self.file_name = None

        self.dev_1_adr_var = tk.StringVar()
        self.mod_1_adr_var = tk.StringVar()

        self.dev_2_adr_var = tk.StringVar()
        self.mod_2_adr_var = tk.StringVar()

        self.dev_3_adr_var = tk.StringVar()
        self.mod_3_adr_var = tk.StringVar()

        self.dev_4_adr_var = tk.StringVar()
        self.mod_4_adr_var = tk.StringVar()

        self.dev_5_adr_var = tk.StringVar()
        self.mod_5_adr_var = tk.StringVar()

        self.dev_6_adr_var = tk.StringVar()
        self.mod_6_adr_var = tk.StringVar()

        self.dev_7_adr_var = tk.StringVar()
        self.mod_7_adr_var = tk.StringVar()

        self.dev_8_adr_var = tk.StringVar()
        self.mod_8_adr_var = tk.StringVar()

        self.dev_9_adr_var = tk.StringVar()
        self.mod_9_adr_var = tk.StringVar()

        self.dev_10_adr_var = tk.StringVar()
        self.mod_10_adr_var = tk.StringVar()

        self.dev_11_adr_var = tk.StringVar()
        self.mod_11_adr_var = tk.StringVar()

        self.dev_12_adr_var = tk.StringVar()
        self.mod_12_adr_var = tk.StringVar()

        self.dev_13_adr_var = tk.StringVar()
        self.mod_13_adr_var = tk.StringVar()

        self.dev_14_adr_var = tk.StringVar()
        self.mod_14_adr_var = tk.StringVar()

        self.dev_15_adr_var = tk.StringVar()
        self.mod_15_adr_var = tk.StringVar()

        self.dev_16_adr_var = tk.StringVar()
        self.mod_16_adr_var = tk.StringVar()

        self.dev_17_adr_var = tk.StringVar()
        self.mod_17_adr_var = tk.StringVar()

        self.dev_18_adr_var = tk.StringVar()
        self.mod_18_adr_var = tk.StringVar()

        self.chk_btn1_var = tk.IntVar()
        self.chk_btn1_var.set(1)
        self.chk_btn2_var = tk.IntVar()
        self.chk_btn2_var.set(1)

        self.stop_check = tk.BooleanVar()

        self.radio_button_change_1_var = tk.IntVar(value=2)

        self.must_time_target = tk.StringVar()
        self.auxilary_time_stop = tk.StringVar()

        self.dist = ttk.Label(tab0, width=5)
        self.dist.grid(row=0, column=0)

        self.labelframe01 = tk.LabelFrame(tab0, text="")
        self.labelframe01.grid(row=1, column=1, sticky=tk.NSEW)

        self.serial_port_var = tk.IntVar(value=0)

        self.stop_check = tk.BooleanVar()

        self.rpm = tk.StringVar()

        self.HE_signal = tk.StringVar()
        self.fan_signal_supp = tk.StringVar()
        self.fan_signal_exh = tk.StringVar()
        self.rpm.set('10')

        self.time_interval = tk.IntVar()
        self.time_interval.set(2)

        self.lbl = tk.StringVar()
        self.lbl.set('')

        self.time_stop = 0
        self.time_start = 0

        self.time_overtake_signal = tk.BooleanVar()

        self.hour_start_variable = tk.StringVar()

        self.minute_start_variable = tk.StringVar()

        self.second_start_variable = tk.StringVar()

        self.start_time_info = tk.StringVar()

        self.start_time_value = None

        self.time_to_start = None

        self.count_down_ID = None

        self.button_count_down_ID = None
        #######################################################################################################################
        #######################################################################################################################
        self.label = ttk.Label(self.labelframe01, text='LP')
        self.label.grid(row=1, column=2)

        self.label = ttk.Label(self.labelframe01, text='Adres rejestru  ')
        self.label.grid(row=1, column=3)

        #######################################################################################################################
        self.label = ttk.Label(self.labelframe01, textvariable=self.lbl, font=('Helvetica', 12))
        self.label.grid(row=2, column=5)
        #######################################################################################################################
        self.label = ttk.Label(self.labelframe01, text='')
        self.label.grid(row=2, column=2)
        #######################################################################################################################
        my_font = font.Font(family='Helvetica', size=8)
        self.label = ttk.Label(self.labelframe01, text="ELP 11R32L", font=my_font)
        self.label.grid(row=2, column=3)

        self.chk_btn1 = tk.Checkbutton(self.labelframe01, variable=self.chk_btn1_var)
        self.chk_btn1.grid(row=2, column=4)

        self.label = ttk.Label(self.labelframe01, text='1')
        self.label.grid(row=6, column=2)
        self.mod_1_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_1_adr_var)
        self.mod_1_adr_entry.grid(row=6, column=3)
        self.mod_1_adr_entry.insert(0, get_data.mod_adress_1.get())
        self.dist = ttk.Label(self.labelframe01, width=5)
        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        # self.label.grid(row=6, column=5)
        self.dev_1_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_1_adr_var)
        # self.dev_1_adr_entry.grid(row=6, column=6)
        self.dev_1_adr_entry.insert(0, "2")
        self.dev_1_adr_entry.config(state="disabled")
        self.dist = ttk.Label(self.labelframe01)
        # self.dist.grid(row=7, column=0)

        ########################################################################################################################

        self.label = ttk.Label(self.labelframe01, text='2')
        self.label.grid(row=10, column=2)

        self.mod_2_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_2_adr_var)
        self.mod_2_adr_entry.grid(row=10, column=3)

        self.mod_2_adr_entry.insert(0, get_data.mod_adress_2.get())
        # self.mod_2_adr_entry.config(state="disabled")

        self.dist = ttk.Label(self.labelframe01, width=5)
        self.dist.grid(row=10, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        # self.label.grid(row=10, column=5)

        self.dev_2_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_2_adr_var)
        # self.dev_2_adr_entry.grid(row=10, column=6)
        self.dev_2_adr_entry.insert(0, "2")
        self.dev_2_adr_entry.config(state="disabled")

        self.dist = ttk.Label(self.labelframe01)
        # self.dist.grid(row=11, column=0)

        #######################################################################################################################

        self.label = ttk.Label(self.labelframe01, text='3')
        self.label.grid(row=15, column=2)

        self.mod_3_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_3_adr_var)
        self.mod_3_adr_entry.grid(row=15, column=3)
        self.mod_3_adr_entry.insert(0, get_data.mod_adress_3.get())
        # self.mod_3_adr_entry.config(state="disabled")

        self.dist = ttk.Label(self.labelframe01, width=5)
        # self.dist.grid(row=15, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        # self.label.grid(row=15, column=5)

        self.dev_3_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_3_adr_var)
        # self.dev_3_adr_entry.grid(row=15, column=6)
        self.dev_3_adr_entry.insert(0, "2")
        self.dev_3_adr_entry.config(state="disabled")

        self.dist = ttk.Label(self.labelframe01)
        # self.dist.grid(row=16, column=0)

        #######################################################################################################################
        self.label = ttk.Label(self.labelframe01, text='4')
        self.label.grid(row=20, column=2)

        self.mod_4_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_4_adr_var)
        self.mod_4_adr_entry.grid(row=20, column=3)

        self.mod_4_adr_entry.insert(0, get_data.mod_adress_4.get())
        # self.mod_4_adr_entry.config(state="disabled")

        self.dist = ttk.Label(self.labelframe01, width=5)
        # self.dist.grid(row=20, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        # self.label.grid(row=20, column=5)

        self.dev_4_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_4_adr_var)
        # self.dev_4_adr_entry.grid(row=20, column=6)
        self.dev_4_adr_entry.insert(0, "2")
        self.dev_4_adr_entry.config(state="disabled")

        self.dist = ttk.Label(self.labelframe01)
        # self.dist.grid(row=21, column=0)

        ###########################################################################################################################

        self.label = ttk.Label(self.labelframe01, text='5')
        self.label.grid(row=30, column=2)

        self.mod_5_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_5_adr_var)
        self.mod_5_adr_entry.grid(row=30, column=3)
        self.mod_5_adr_entry.insert(0, get_data.mod_adress_5.get())
        # self.mod_5_adr_entry.config(state="disabled")

        self.dist = ttk.Label(self.labelframe01, width=5)
        # self.dist.grid(row=30, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        # self.label.grid(row=30, column=5)

        self.dev_5_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_5_adr_var)
        # self.dev_5_adr_entry.grid(row=30, column=6)
        self.dev_5_adr_entry.insert(0, "2")
        self.dev_5_adr_entry.config(state="disabled")

        self.dist = ttk.Label(self.labelframe01)
        # self.dist.grid(row=31, column=0)
        ########################################################################################################################

        self.label = ttk.Label(self.labelframe01, text='6')
        self.label.grid(row=40, column=2)

        self.mod_6_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_6_adr_var)
        self.mod_6_adr_entry.grid(row=40, column=3)
        self.mod_6_adr_entry.insert(0, get_data.mod_adress_6.get())
        # self.mod_6_adr_entry.config(state="disabled")

        self.dist = ttk.Label(self.labelframe01, width=5)
        # self.dist.grid(row=40, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        # self.label.grid(row=40, column=5)

        self.dev_6_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_6_adr_var)
        # self.dev_6_adr_entry.grid(row=40, column=6)
        self.dev_6_adr_entry.insert(0, "2")
        self.dev_6_adr_entry.config(state="disabled")

        self.dist = ttk.Label(self.labelframe01)
        # self.dist.grid(row=41, column=0)

        ############################################################################################################################

        self.label = ttk.Label(self.labelframe01, text='7')
        self.label.grid(row=50, column=2)

        self.mod_7_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_7_adr_var)
        self.mod_7_adr_entry.grid(row=50, column=3)
        self.mod_7_adr_entry.insert(0, get_data.mod_adress_7.get())
        # self.mod_7_adr_entry.config(state="disabled")
        self.dist = ttk.Label(self.labelframe01, width=5)
        # self.dist.grid(row=50, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        # self.label.grid(row=50, column=5)

        self.dev_7_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_7_adr_var)
        # self.dev_7_adr_entry.grid(row=50, column=6)

        self.dev_7_adr_entry.insert(0, "2")
        self.dev_7_adr_entry.config(state="disabled")

        self.dist = ttk.Label(self.labelframe01)
        # self.dist.grid(row=51, column=0)

        ############################################################################################################################

        self.label = ttk.Label(self.labelframe01, text='8')
        self.label.grid(row=60, column=2)

        self.mod_8_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_8_adr_var)
        self.mod_8_adr_entry.grid(row=60, column=3)
        self.mod_8_adr_entry.insert(0, get_data.mod_adress_8.get())
        # self.mod_8_adr_entry.config(state="disabled")

        self.dist = ttk.Label(self.labelframe01, width=5)
        # self.dist.grid(row=60, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        # self.label.grid(row=60, column=5)

        self.dev_8_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_8_adr_var)
        # self.dev_8_adr_entry.grid(row=60, column=6)

        self.dev_8_adr_entry.insert(0, "1")

        self.dist = ttk.Label(self.labelframe01)
        # self.dist.grid(row=61, column=0)

        ############################################################################################################################

        self.label = ttk.Label(self.labelframe01, text='9')
        self.label.grid(row=70, column=2)

        self.mod_9_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_9_adr_var)
        self.mod_9_adr_entry.grid(row=70, column=3)
        self.mod_9_adr_entry.insert(0, get_data.mod_adress_9.get())
        # self.mod_9_adr_entry.config(state="disabled")

        self.dist = ttk.Label(self.labelframe01, width=5)
        # self.dist.grid(row=70, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        # self.label.grid(row=70, column=5)

        self.dev_9_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_9_adr_var)
        # self.dev_9_adr_entry.grid(row=70, column=6)
        self.dev_9_adr_entry.insert(0, "1")

        self.dist = ttk.Label(self.labelframe01)
        # self.dist.grid(row=71, column=0)

        ############################################################################################################################

        my_font = font.Font(family='Helvetica', size=8)
        self.label = ttk.Label(self.labelframe01, text="Falownik", font=my_font)
        self.label.grid(row=75, column=3)

        self.chk_btn2 = tk.Checkbutton(self.labelframe01, variable=self.chk_btn2_var)
        self.chk_btn2.grid(row=75, column=4)

        self.label = ttk.Label(self.labelframe01, text='10')
        self.label.grid(row=80, column=2)
        self.mod_10_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_10_adr_var)
        self.mod_10_adr_entry.grid(row=80, column=3)
        self.mod_10_adr_entry.insert(0, get_data.mod_adress_10.get())
        # self.mod_10_adr_entry.config(state="disabled")
        self.dist = ttk.Label(self.labelframe01, width=5)
        # self.dist.grid(row=80, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        # self.label.grid(row=80, column=5)

        self.dev_10_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_10_adr_var)
        # self.dev_10_adr_entry.grid(row=80, column=6)
        self.dev_10_adr_entry.insert(0, "1")

        self.dist = ttk.Label(self.labelframe01)
        # self.dist.grid(row=81, column=0)

        ############################################################################################################################

        self.label = ttk.Label(self.labelframe01, text='11')
        self.label.grid(row=90, column=2)

        self.mod_11_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_11_adr_var)
        self.mod_11_adr_entry.grid(row=90, column=3)
        self.mod_11_adr_entry.insert(0, get_data.mod_adress_11.get())
        # self.mod_11_adr_entry.config(state="disabled")

        self.dist = ttk.Label(self.labelframe01, width=5)
        # self.dist.grid(row=90, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        # self.label.grid(row=90, column=5)

        self.dev_11_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_11_adr_var)
        # self.dev_11_adr_entry.grid(row=90, column=6)
        self.dev_11_adr_entry.insert(0, "1")

        self.dist = ttk.Label(self.labelframe01)
        # self.dist.grid(row=91, column=0)

        ###########################################################################################################################

        self.label = ttk.Label(self.labelframe01, text='12')
        self.label.grid(row=100, column=2)

        self.mod_12_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_12_adr_var)
        self.mod_12_adr_entry.grid(row=100, column=3)
        self.mod_12_adr_entry.insert(0, get_data.mod_adress_12.get())

        self.dist = ttk.Label(self.labelframe01, width=5)
        self.dist.grid(row=100, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')

        self.dev_12_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_12_adr_var)

        self.dev_12_adr_entry.insert(0, "1")

        self.dist = ttk.Label(self.labelframe01)

        ###########################################################################################################################

        self.label = ttk.Label(self.labelframe01, text='13')
        self.label.grid(row=120, column=2)

        self.mod_13_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_13_adr_var)
        self.mod_13_adr_entry.grid(row=120, column=3)
        self.mod_13_adr_entry.insert(0, get_data.mod_adress_13.get())
        # self.mod_13_adr_entry.config(state="disabled")
        self.dist = ttk.Label(self.labelframe01, width=5)
        # self.dist.grid(row=120, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        # self.label.grid(row=120, column=5)

        # self.label = ttk.Label(self.labelframe01, text='Pa')
        # self.label.grid(row=120, column=5)

        self.dev_13_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_13_adr_var)
        # self.dev_13_adr_entry.grid(row=120, column=6)
        self.dev_13_adr_entry.insert(0, "1")

        self.dist = ttk.Label(self.labelframe01)
        # self.dist.grid(row=121, column=0)

        ###########################################################################################################################

        self.label = ttk.Label(self.labelframe01, text='14')
        self.label.grid(row=130, column=2)

        self.mod_14_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_14_adr_var)
        self.mod_14_adr_entry.grid(row=130, column=3)
        self.mod_14_adr_entry.insert(0, get_data.mod_adress_14.get())
        # self.mod_14_adr_entry.config(state="disabled")
        self.dist = ttk.Label(self.labelframe01, width=5)
        # self.dist.grid(row=130, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')

        self.dev_14_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_14_adr_var)
        # self.dev_14_adr_entry.grid(row=130, column=6)

        self.dev_14_adr_entry.insert(0, "1")

        self.dist = ttk.Label(self.labelframe01)
        # self.dist.grid(row=131, column=0)

        ###########################################################################################################################

        self.label = ttk.Label(self.labelframe01, text='15')
        self.label.grid(row=140, column=2)

        self.mod_15_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_15_adr_var)
        self.mod_15_adr_entry.grid(row=140, column=3)
        self.mod_15_adr_entry.insert(0, get_data.mod_adress_15.get())
        # self.mod_15_adr_entry.config(state="disabled")

        self.dist = ttk.Label(self.labelframe01, width=5)
        # self.dist.grid(row=140, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        # self.label.grid(row=140, column=5)

        # self.label = ttk.Label(self.labelframe01, text='Pa')
        # self.label.grid(row=140, column=5)

        self.dev_15_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_15_adr_var)
        # self.dev_15_adr_entry.grid(row=140, column=6)
        self.dev_15_adr_entry.insert(0, "1")

        self.dist = ttk.Label(self.labelframe01)
        # self.dist.grid(row=141, column=0)

        ###########################################################################################################################
        self.label = ttk.Label(self.labelframe01, text='16')
        self.label.grid(row=150, column=2)

        self.mod_16_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_16_adr_var)
        self.mod_16_adr_entry.grid(row=150, column=3)
        self.mod_16_adr_entry.insert(0, get_data.mod_adress_16.get())
        # self.mod_16_adr_entry.config(state="disabled")

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        self.dev_16_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_16_adr_var)
        self.dev_16_adr_entry.insert(0, "1")
        self.label = ttk.Label(self.labelframe01)

        ####################################################################################################################################

        self.label = ttk.Label(self.labelframe01, text='17')
        self.label.grid(row=160, column=2)

        self.mod_17_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_17_adr_var)
        self.mod_17_adr_entry.grid(row=160, column=3)
        self.mod_17_adr_entry.insert(0, get_data.mod_adress_17.get())

        ####################################################################################################################################
        self.label = ttk.Label(self.labelframe01, text='18')
        self.label.grid(row=170, column=2)

        self.mod_18_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_18_adr_var)
        self.mod_18_adr_entry.grid(row=170, column=3)
        self.mod_18_adr_entry.insert(0, get_data.mod_adress_18.get())

        ######################################################################################################################################
        self.label = ttk.Label(self.labelframe01, text='')
        self.label.grid(row=180, column=2)

        self.cfg_button = ttk.Button(self.labelframe01, text="cfg", width=2, command=self.exe_cfg)
        self.cfg_button.grid(row=205, column=3, ipadx=50)

        ########################################################################################################################
        self.change_file_button = ttk.Button(self.labelframe01, text="save cfg", width=2, command=self.save_cfg)
        self.change_file_button.grid(row=205, column=5, ipadx=50)

        #######################################################################################################################

        self.start_save_button = ttk.Button(self.labelframe01, text="start -zapis", width=2, command=self.start_save)
        self.start_save_button.grid(row=210, column=3, ipadx=50)

        ######################################################################################################################

        self.stop_save_button = ttk.Button(self.labelframe01, text="stop - zapis", width=2, command=self.stop_save)
        self.stop_save_button.grid(row=210, column=5, ipadx=50)

        ##########################################################################################################################
        ########################################################################################################################

        self.labelframe02 = tk.LabelFrame(tab2, text="")
        self.labelframe02.grid(row=1, column=1, sticky=tk.NSEW)
        ########################################################################################################################

        self.dist = ttk.Label(self.labelframe02, text="").grid(row=70, columns=1)

        self.dist = ttk.Label(self.labelframe02, text="Czas tr[s] miedzy rekordami ")
        self.dist.grid(row=75, column=5)

        self.fan_signal_entry = ttk.Entry(self.labelframe02, textvariable=self.time_interval)
        self.fan_signal_entry.grid(row=75, column=10)

        self.dist = ttk.Label(self.labelframe02, text="").grid(row=80, columns=1)

        ########################################################################################################################
        # switch time system
        self.system_time_switch = tk.Radiobutton(self.labelframe02, text='czas RTC', variable=self.time_system_switch,
                                                 value=True)
        self.system_time_switch.grid(row=85, column=5)

        self.RTC_time_switch = tk.Radiobutton(self.labelframe02, text='czas systemowy',
                                              variable=self.time_system_switch, value=False)
        self.RTC_time_switch.grid(row=85, column=10)

        ############################################################################################################################
        ############################################################################################################################
        self.labelframe03 = tk.LabelFrame(tab2, text="")
        self.labelframe03.grid(row=3, column=1, sticky=tk.NSEW)

        self.dist = ttk.Label(self.labelframe03, text="")
        self.dist.grid(row=1, column=1)

        self.dist = ttk.Label(self.labelframe03, text="Czas startu ")
        self.dist.grid(row=2, column=2)

        self.hour_start_entry = ttk.Entry(self.labelframe03, textvariable=self.hour_start_variable, width=3)
        self.hour_start_entry.grid(row=2, column=3)

        self.dist = ttk.Label(self.labelframe03, text=":")
        self.dist.grid(row=2, column=4)

        self.minute_start_entry = ttk.Entry(self.labelframe03, textvariable=self.minute_start_variable, width=3)
        self.minute_start_entry.grid(row=2, column=5)

        self.dist = ttk.Label(self.labelframe03, text=":")
        self.dist.grid(row=2, column=6)

        self.second_start_entry = ttk.Entry(self.labelframe03, textvariable=self.second_start_variable, width=3)
        self.second_start_entry.grid(row=2, column=7)

        self.dist = ttk.Label(self.labelframe03, text="", width=5)
        self.dist.grid(row=2, column=9)

        self.accept_start_button = ttk.Button(self.labelframe03, text="set", width=5, command=self.start_time)
        self.accept_start_button.grid(row=2, column=10)



        ##################################################################################
        ##################################################################################
        self.labelframe04 = tk.LabelFrame(tab2, text="")
        self.labelframe04.grid(row=4, column=1, sticky=tk.NSEW)

        self.dist = ttk.Label(self.labelframe04, width=5, text="")  # dystans
        self.dist.grid(row=1, column=1)

        self.labelframe04_in_1 = tk.LabelFrame(self.labelframe04, text="system choice")
        self.labelframe04_in_1.grid(row=2, column=1)

        self.dist = ttk.Label(self.labelframe04, width=5, text="")  # dystans
        self.dist.grid(row=3, column=1)

        self.labelframe04_in_2 = tk.LabelFrame(self.labelframe04, text="Wpisz numer portu")
        self.labelframe04_in_2.grid(row=4, column=1)

        ########################################################################################################################

        self.radio_button_change_1 = tk.Radiobutton(self.labelframe04_in_1, text='windows',
                                                    variable=self.radio_button_change_1_var, value=1)
        self.radio_button_change_1.grid(row=1, column=1)
        self.radio_button_change_2 = tk.Radiobutton(self.labelframe04_in_1, text='Linux',
                                                    variable=self.radio_button_change_1_var, value=2)
        self.radio_button_change_2.grid(row=1, column=2)

        ##############################################################################################################################################

        ###############################################################################################################################################

        self.entry_port = ttk.Entry(self.labelframe04_in_2, textvariable=self.serial_port_var)
        self.entry_port.grid(row=1, column=1)

        ###############################################################################################################################################

    def start_time(self):
        current_datetime = datetime.datetime.now()

    def exe_cfg(self):

        try:
            get_data.dicto_paresr()

            self.mod_1_adr_entry.delete(0, END)
            self.mod_2_adr_entry.delete(0, END)
            self.mod_3_adr_entry.delete(0, END)
            self.mod_4_adr_entry.delete(0, END)
            self.mod_5_adr_entry.delete(0, END)
            self.mod_6_adr_entry.delete(0, END)
            self.mod_7_adr_entry.delete(0, END)
            self.mod_8_adr_entry.delete(0, END)
            self.mod_9_adr_entry.delete(0, END)
            self.mod_10_adr_entry.delete(0, END)
            self.mod_11_adr_entry.delete(0, END)
            self.mod_12_adr_entry.delete(0, END)
            self.mod_13_adr_entry.delete(0, END)
            self.mod_14_adr_entry.delete(0, END)
            self.mod_15_adr_entry.delete(0, END)
            self.mod_16_adr_entry.delete(0, END)
            self.mod_17_adr_entry.delete(0, END)
            self.mod_18_adr_entry.delete(0, END)

            self.mod_1_adr_entry.insert(0, get_data.mod_adress_1.get())
            self.mod_2_adr_entry.insert(0, get_data.mod_adress_2.get())
            self.mod_3_adr_entry.insert(0, get_data.mod_adress_3.get())
            self.mod_4_adr_entry.insert(0, get_data.mod_adress_4.get())
            self.mod_5_adr_entry.insert(0, get_data.mod_adress_5.get())
            self.mod_6_adr_entry.insert(0, get_data.mod_adress_6.get())
            self.mod_7_adr_entry.insert(0, get_data.mod_adress_7.get())
            self.mod_8_adr_entry.insert(0, get_data.mod_adress_8.get())
            self.mod_9_adr_entry.insert(0, get_data.mod_adress_9.get())
            self.mod_10_adr_entry.insert(0, get_data.mod_adress_10.get())
            self.mod_11_adr_entry.insert(0, get_data.mod_adress_11.get())
            self.mod_12_adr_entry.insert(0, get_data.mod_adress_12.get())
            self.mod_13_adr_entry.insert(0, get_data.mod_adress_13.get())
            self.mod_14_adr_entry.insert(0, get_data.mod_adress_14.get())
            self.mod_15_adr_entry.insert(0, get_data.mod_adress_15.get())
            self.mod_16_adr_entry.insert(0, get_data.mod_adress_16.get())
            self.mod_17_adr_entry.insert(0, get_data.mod_adress_16.get())
            self.mod_18_adr_entry.insert(0, get_data.mod_adress_16.get())

        except:
            messagebox.showinfo('info', 'Odczyt nieudany')

    def choose_file(self):
        self.file_name = asksaveasfile(initialdir='C:\\Users\oljar\PycharmProjects\jupiter02', defaultextension='*.csv',
                                       mode='w', filetypes=[('CSV Files', '*.csv')])

        print(self.file_name.name)

    def start_time_point(self):
        time_now = self.actual_time_system()
        time_operat = time_now.replace(second=0)
        delta = datetime.timedelta(minutes=1)
        start_point = time_operat + delta
        return start_point

    def start_save(self):
        self.start_time_value = self.start_time_point()
        self.time_leveling()

    def go_ahead(self):
        self.stop_check.set(False)
        self.controller.transfer_data()
        #

        self.controller.start_save()

        self.start_save_button.config(state="disabled")
        self.stop_save_button.config(state="enabled")
        time_gen = Generator(int(self.time_interval.get()), self.actual_time_system())
        self.generator = time_gen.infinite_time_generator()
        self.start_loop()

    def time_leveling(self):
        a = (self.actual_time_system())
        a1 = int(a.timestamp())
        b = self.start_time_value
        b1 = int(b.timestamp())
        self.time_to_start = b1 - a1
        self.count_down_ID = self.labelframe01.after(self.time_to_start * 1000, self.go_ahead)
        self.button_count_down()

    def button_count_down(self):
        self.stop_save_button.config(state="disabled")
        self.start_save_button.config(text=self.time_to_start)
        self.time_to_start -= 1
        self.button_count_down_ID = self.labelframe01.after(1000, self.button_count_down)
        if self.time_to_start <= 0:
            self.start_save_button.config(text="zapis-trwa")
            self.labelframe01.after_cancel(self.button_count_down_ID)
            return

    def actual_time_system(self):

        while True:
            try:
                if bool(self.time_system_switch.get()):
                    date_time_all = subprocess.getoutput('sudo hwclock -r')

                    try:
                        date_time_split = datetime.datetime.strptime(date_time_all, "%Y-%m-%d %H:%M:%S.%f%z")
                    except:
                        date_time_split = datetime.datetime.strptime(date_time_all, "%Y-%m-%d %H:%M:%S.%f")
                    return date_time_split.replace(microsecond=0, tzinfo=None)
                else:
                    date_time_all = str(datetime.datetime.now())

                    try:
                        date_time_split = datetime.datetime.strptime(date_time_all, "%Y-%m-%d %H:%M:%S.%f")
                    except:
                        date_time_split = datetime.datetime.strptime(date_time_all, "%Y-%m-%d %H:%M:%S")
                    return date_time_split.replace(microsecond=0, tzinfo=None)

            except:
                self.actual_time_system()

    def start_loop(self):

        self.must_time_target.set(next(self.generator))

        must_time_target_str = self.must_time_target.get()
        must_time_target = datetime.datetime.strptime(must_time_target_str, "%Y-%m-%d %H:%M:%S")
        must_time_target = must_time_target.replace(microsecond=0)

        while True:
            actual_time_system_before = self.actual_time_system()

            if actual_time_system_before == must_time_target:
                self.time_overtake_signal.set(False)  # save value of modbus  in CSV
                self.controller.save_data()
                time.sleep(0.2)  # here set frequency of sampling
                break
            elif actual_time_system_before > must_time_target:
                self.time_overtake_signal.set(True)

                self.controller.save_data()
                print('czas przekroczony 02')
                break

        if self.stop_check.get():
            return
        print("#########################################")

        if self.stop_check.get():
            return
        self.labelframe01.after(200, self.start_loop)  # here set frequency of sampling

        if self.stop_check.get():
            return

    def exit_loop(self):
        if self.stop_check.get():
            return

    def stop_save(self):
        self.lbl.set(f'')
        self.stop_check.set(True)
        self.stop_save_button.config(state="disabled")
        self.start_save_button.config(state="enabled")
        self.start_save_button.config(text="start-zapis")
        self.labelframe01.after_cancel(self.count_down_ID)
        self.labelframe01.after_cancel(self.button_count_down_ID)



    def save_cfg(self):
        try:
            self.controller.save_cfg()

        except:
            messagebox.showinfo('info', 'zapis nieudany')

    ##########################################################################################################################################

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

        self.start_save()
