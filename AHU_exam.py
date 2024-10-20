import matplotlib
import re
import tkinter as tk
from tkinter import ttk
from Controller import Controller
from Model import Model
from View import View
import View as V
import threading



class Application(tk.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)

        # create a model


mod_1_adr_var = tk.StringVar()
dev_1_adr_var = tk.StringVar()
mod_2_adr_var = tk.StringVar()
dev_2_adr_var = tk.StringVar()
mod_3_adr_var = tk.StringVar()
dev_3_adr_var = tk.StringVar()
mod_4_adr_var = tk.StringVar()
dev_4_adr_var = tk.StringVar()
mod_5_adr_var = tk.StringVar()
dev_5_adr_var = tk.StringVar()
mod_6_adr_var = tk.StringVar()
dev_6_adr_var = tk.StringVar()
mod_7_adr_var = tk.StringVar()
dev_7_adr_var = tk.StringVar()
mod_8_adr_var = tk.StringVar()
dev_8_adr_var = tk.StringVar()
mod_9_adr_var = tk.StringVar()
dev_9_adr_var = tk.StringVar()
mod_10_adr_var = tk.StringVar()
dev_10_adr_var = tk.StringVar()
mod_11_adr_var = tk.StringVar()
dev_11_adr_var = tk.StringVar()
mod_12_adr_var = tk.StringVar()
dev_12_adr_var = tk.StringVar()
mod_13_adr_var = tk.StringVar()
dev_13_adr_var = tk.StringVar()
mod_14_adr_var = tk.StringVar()
dev_14_adr_var = tk.StringVar()
mod_15_adr_var = tk.StringVar()
dev_15_adr_var = tk.StringVar()
mod_16_adr_var = tk.StringVar()
dev_16_adr_var = tk.StringVar()
mod_17_adr_var = tk.StringVar()
dev_17_adr_var = tk.StringVar()
mod_18_adr_var = tk.StringVar()
dev_18_adr_var = tk.StringVar()




t = tk.StringVar()
delta_t = tk.StringVar()
save_control = tk.BooleanVar()

fan_signal = tk.StringVar()
HE_signal = tk.StringVar()

data_1 = None
data_2 = None
data_3 = None
data_4 = None
data_5 = None
data_6 = None
data_7 = None
data_8 = None
data_9 = None
data_10 = None
data_11 = None
data_12 = None
data_13 = None
data_14 = None
data_15 = None
data_16 = None
data_17 = None
data_18 = None

model = Model(t, save_control, delta_t, mod_1_adr_var, dev_1_adr_var, mod_2_adr_var, dev_2_adr_var, mod_3_adr_var,
              dev_3_adr_var,mod_4_adr_var, dev_4_adr_var, mod_5_adr_var, dev_5_adr_var, mod_6_adr_var, dev_6_adr_var,
              mod_7_adr_var,dev_7_adr_var, mod_8_adr_var, dev_8_adr_var, mod_9_adr_var, dev_9_adr_var, mod_10_adr_var,
              dev_10_adr_var, mod_11_adr_var, dev_11_adr_var, mod_12_adr_var, dev_12_adr_var, mod_13_adr_var,
              dev_13_adr_var, mod_14_adr_var, dev_14_adr_var, mod_15_adr_var, dev_15_adr_var,
              mod_16_adr_var, dev_16_adr_var, mod_17_adr_var, dev_17_adr_var,mod_18_adr_var, dev_18_adr_var,
              data_1, data_2, data_3, data_4, data_5, data_6, data_7, data_8, data_9, data_10, data_11, data_12, data_13,
              data_14, data_15, data_16, data_17, data_18)

view = View(V.window)

controller = Controller(model, view)
view.set_controller(controller)
V.tab_parent.add(V.tab0, text='parametry')
V.tab_parent.add(V.tab2, text='ustawienia')

V.tab_parent.pack(expand=1, fill='both')

app = Application(V.window)

V.window.mainloop()


