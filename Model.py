import csv
import tkinter as tk

class Model:


    def __init__(self, save_control,t, delta_t, mod_1_adr_var, dev_1_adr_var, mod_2_adr_var,
                 dev_2_adr_var,
                 mod_3_adr_var, dev_3_adr_var, mod_4_adr_var, dev_4_adr_var, mod_5_adr_var, dev_5_adr_var,
                 mod_6_adr_var, dev_6_adr_var, mod_7_adr_var, dev_7_adr_var, mod_8_adr_var, dev_8_adr_var,
                 mod_9_adr_var, dev_9_adr_var, mod_10_adr_var, dev_10_adr_var, mod_11_adr_var, dev_11_adr_var,
                 mod_12_adr_var, dev_12_adr_var, mod_13_adr_var, dev_13_adr_var, mod_14_adr_var, dev_14_adr_var,
                 mod_15_adr_var,dev_15_adr_var,  mod_16_adr_var, dev_16_adr_var, mod_17_adr_var, dev_17_adr_var,
                 mod_18_adr_var, dev_18_adr_var,
                 data_1, data_2, data_3, data_4, data_5, data_6, data_7, data_8, data_9, data_10,
                 data_11, data_12, data_13, data_14, data_15, data_16, data_17, data_18):


        self.mod_1_adr_var = mod_1_adr_var.get()
        self.dev_1_adr_var = dev_1_adr_var.get()

        self.mod_2_adr_var = mod_2_adr_var.get()
        self.dev_2_adr_var = dev_2_adr_var.get()

        self.mod_3_adr_var = mod_3_adr_var.get()
        self.dev_3_adr_var = dev_3_adr_var.get()

        self.mod_4_adr_var = mod_4_adr_var.get()
        self.dev_4_adr_var = dev_4_adr_var.get()

        self.mod_5_adr_var = mod_5_adr_var.get()
        self.dev_5_adr_var = dev_5_adr_var.get()

        self.mod_6_adr_var = mod_6_adr_var.get()
        self.dev_6_adr_var = dev_6_adr_var.get()

        self.mod_7_adr_var = mod_7_adr_var.get()
        self.dev_7_adr_var = dev_7_adr_var.get()

        self.mod_8_adr_var = mod_8_adr_var.get()
        self.dev_8_adr_var = dev_8_adr_var.get()

        self.mod_9_adr_var = mod_9_adr_var.get()
        self.dev_9_adr_var = dev_9_adr_var.get()

        self.mod_10_adr_var = mod_10_adr_var.get()
        self.dev_10_adr_var = dev_10_adr_var.get()

        self.mod_11_adr_var = mod_11_adr_var.get()
        self.dev_11_adr_var = dev_11_adr_var.get()

        self.mod_12_adr_var = mod_12_adr_var.get()
        self.dev_12_adr_var = dev_12_adr_var.get()

        self.mod_13_adr_var = mod_13_adr_var.get()
        self.dev_13_adr_var = dev_13_adr_var.get()

        self.mod_14_adr_var = mod_14_adr_var.get()
        self.dev_14_adr_var = dev_14_adr_var.get()

        self.mod_15_adr_var = mod_15_adr_var.get()
        self.dev_15_adr_var = dev_15_adr_var.get()

        self.mod_16_adr_var = mod_16_adr_var.get()
        self.dev_16_adr_var = dev_16_adr_var.get()

        self.mod_17_adr_var = mod_17_adr_var.get()
        self.dev_17_adr_var = dev_17_adr_var.get()

        self.mod_18_adr_var = mod_18_adr_var.get()
        self.dev_18_adr_var = dev_18_adr_var.get()

        self.data_1 = data_1    
        self.data_2 = data_2   
        self.data_3 = data_3   
        self.data_4 = data_4    
        self.data_5 = data_5    
        self.data_6 = data_6    
        self.data_7 = data_7   
        self.data_8 = data_8   
        self.data_9 = data_9    
        self.data_10 = data_10  
        self.data_11 = data_11
        self.data_12 = data_12
        self.data_13 = data_13
        self.data_14 = data_14
        self.data_15 = data_15
        self.data_16 = data_16
        self.data_17 = data_17
        self.data_18 = data_18

        self.save_control = save_control
        self.t = t
        self.delta_t = delta_t

        

    # @property
    # def data_1(self):
    #     return self.__data_1
    #
    # @data_1.setter
    # def data_1(self, data_1):
    #     self.__data_1 = data_1
    #
    # @data_1.getter
    # def data_1(self):
    #     return self

    # solution.to_csv(str(self.view.save_name_var.get()), sep=';', decimal=',', index=False, encoding='utf-8')

    def stop_save(self):
        print('stop')
