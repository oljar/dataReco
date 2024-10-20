from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile
from tkinter import *


from Model import *
class GetData:



    def __init__(self):
        self.mod_adress_1 = StringVar()
        self.mod_adress_2 = StringVar()
        self.mod_adress_3 = StringVar()
        self.mod_adress_4 = StringVar()
        self.mod_adress_5 = StringVar()
        self.mod_adress_6 = StringVar()
        self.mod_adress_7 = StringVar()
        self.mod_adress_8 = StringVar()
        self.mod_adress_9 = StringVar()
        self.mod_adress_10 = StringVar()
        self.mod_adress_11 = StringVar()
        self.mod_adress_12 = StringVar()
        self.mod_adress_13 = StringVar()
        self.mod_adress_14 = StringVar()
        self.mod_adress_15 = StringVar()
        self.mod_adress_16 = StringVar()
        self.mod_adress_17 = StringVar()
        self.mod_adress_18 = StringVar()






        def start_parser():

            diction = {}
            keys = []
            values = []

            # with open('default_config.txt', 'r', encoding='utf-8') as file:
            #     lines = file.readlines()

            # for ln in lines:
            #     key, value = ln.strip('\n').split('=')
            #     diction[key] = value

            # return diction
        
        self.mod_adress_1.set(0)
        self.mod_adress_2.set(2)
        self.mod_adress_3.set(4)
        self.mod_adress_4.set(6)
        self.mod_adress_5.set(8)
        self.mod_adress_6.set(10)
        self.mod_adress_7.set(12)
        self.mod_adress_8.set(14)
        self.mod_adress_9.set(16)
        self.mod_adress_10.set(0)
        self.mod_adress_11.set(2)
        self.mod_adress_12.set(4)
        self.mod_adress_13.set(6)
        self.mod_adress_14.set(8)
        self.mod_adress_15.set(10)
        self.mod_adress_16.set(12)
        self.mod_adress_17.set(14)
        self.mod_adress_18.set(16)





        
        
        # try:
        #     self.mod_adress_1.set(start_parser()['1'])
        #     self.mod_adress_2.set(start_parser()['2'])
        #     self.mod_adress_3.set(start_parser()['3'])
        #     self.mod_adress_4.set(start_parser()['4'])
        #     self.mod_adress_5.set(start_parser()['5'])
        #     self.mod_adress_6.set(start_parser()['6'])
        #     self.mod_adress_7.set(start_parser()['7'])
        #     self.mod_adress_8.set(start_parser()['8'])
        #     self.mod_adress_9.set(start_parser()['9'])
        #     self.mod_adress_10.set(start_parser()['10'])
        #     self.mod_adress_11.set(start_parser()['11'])
        #     self.mod_adress_12.set(start_parser()['12'])
        #     self.mod_adress_13.set(start_parser()['13'])
        #     self.mod_adress_14.set(start_parser()['14'])
        #     self.mod_adress_15.set(start_parser()['15'])
        #     self.mod_adress_16.set(start_parser()['16'])
        #     self.mod_adress_17.set(start_parser()['17'])
        #     self.mod_adress_18.set(start_parser()['18'])

        # except:

        #     self.mod_adress_1.set(0)
        #     self.mod_adress_2.set(0)
        #     self.mod_adress_3.set(0)
        #     self.mod_adress_4.set(0)
        #     self.mod_adress_5.set(0)
        #     self.mod_adress_6.set(0)
        #     self.mod_adress_7.set(0)
        #     self.mod_adress_8.set(0)
        #     self.mod_adress_9.set(0)
        #     self.mod_adress_10.set(0)
        #     self.mod_adress_11.set(0)
        #     self.mod_adress_12.set(0)
        #     self.mod_adress_13.set(0)
        #     self.mod_adress_14.set(0)
        #     self.mod_adress_15.set(0)
        #     self.mod_adress_16.set(0)
        #     self.mod_adress_17.set(0)
        #     self.mod_adress_18.set(0)


    # #
    #
    def dicto_paresr(self):
        file33 = askopenfile(initialdir='C:\\Users\oljar\PycharmProjects\jupiter02', mode='r',filetypes=[('TXT Files', '*.txt')])

        diction = {}
        keys = []
        values = []

        with open(str(file33.name), 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for ln in lines:
            key, value = ln.strip('\n').split('=')
            diction[key] = value

        self.mod_adress_1.set(diction['1'])
        self.mod_adress_2.set(diction['2'])
        self.mod_adress_3.set(diction['3'])
        self.mod_adress_4.set(diction['4'])
        self.mod_adress_5.set(diction['5'])
        self.mod_adress_6.set(diction['6'])
        self.mod_adress_7.set(diction['7'])
        self.mod_adress_8.set(diction['8'])
        self.mod_adress_9.set(diction['9'])
        self.mod_adress_10.set(diction['10'])
        self.mod_adress_11.set(diction['11'])
        self.mod_adress_12.set(diction['12'])
        self.mod_adress_13.set(diction['13'])
        self.mod_adress_14.set(diction['14'])
        self.mod_adress_15.set(diction['15'])
        self.mod_adress_16.set(diction['16'])
        self.mod_adress_17.set(diction['17'])
        self.mod_adress_18.set(diction['18'])
