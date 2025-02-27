import tkinter as tk
from tkinter import Message ,Text
from PIL import Image, ImageTk
import pandas as pd
from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as font
import tkinter.messagebox as tm
import matplotlib.pyplot as plt
import csv
import numpy as np
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter.messagebox as tm


import train as tr
import test as pred
import realtimePredictor as rp

bgcolor="#DAF7A6"
bgcolor1="#B7C526"
fgcolor="black"
def Home():
        global window4
        def clear():
            print("Clear1")
            txt.delete(0, 'end')
            
            
             
            
  



        window4 = tk.Tk()
        window4.title("Forest Fire Detection and Alerting System ")
        
 
        window4.geometry('1240x720')
        window4.configure(background=bgcolor)
        #window.attributes('-fullscreen', True)

        window4.grid_rowconfigure(0, weight=1)
        window4.grid_columnconfigure(0, weight=1)
        

        message1 = tk.Label(window4, text="Forest Fire Detection and Alerting System" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=2,font=('times', 30, 'italic bold underline')) 
        message1.place(x=100, y=1)

        lbl = tk.Label(window4, text="Select Image",width=10  ,height=1  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl.place(x=10, y=100)
        
        txt = tk.Entry(window4,width=10,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt.place(x=300, y=115)
        

        
        def browse():
                path=filedialog.askopenfilename()
                print(path)
                txt.delete(0, 'end')
                txt.insert('end',path)
                if path !="":
                        print(path)
                else:
                        tm.showinfo("Input error", "Select Image")
        

        def Trainprocess():
                tr.process("./Train")
                tm.showinfo("output", "CNN Training Successfully Finished")
               
        def Predictprocess():
                sym=txt.get()
                if sym != "":
                        result=pred.process(sym)
                        tm.showinfo("Output", "Prediction : " +str(result))
                else:
                        tm.showinfo("Input error", "Select Image File")
        def realprocess():
                rp.process()

                        
        browse = tk.Button(window4, text="Browse", command=browse  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        browse.place(x=500, y=115)

        clearButton = tk.Button(window4, text="Clear", command=clear  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=1 ,activebackground = "Red" ,font=('times', 15, ' bold '))
        clearButton.place(x=700, y=115)
        LRButton = tk.Button(window4, text="Train", command=Trainprocess  ,fg=fgcolor   ,bg=bgcolor1  ,width=15  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        LRButton.place(x=100, y=400)
        KNNButton = tk.Button(window4, text="Predict", command=Predictprocess  ,fg=fgcolor   ,bg=bgcolor1  ,width=15  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        KNNButton.place(x=300, y=400)
        KNNButton1 = tk.Button(window4, text="Realtime", command=realprocess  ,fg=fgcolor   ,bg=bgcolor1  ,width=15  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        KNNButton1.place(x=500, y=400)
        
        quitWindow = tk.Button(window4, text="Quit", command=window4.destroy  ,fg=fgcolor   ,bg=bgcolor1  ,width=15  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        quitWindow.place(x=700, y=400)
        window4.mainloop()

       
Home()

