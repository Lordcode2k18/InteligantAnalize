import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
from matplotlib.dates import DayLocator, DateFormatter
from numpy import array
from pandas import to_datetime
from collections import Counter
from tkinter import *

DataBase = "DATABASE.csv"

root = Tk()

#Парсимо і доводимо до нормального вигляду

def parser(DataBase):
    
    df = pd.read_csv("DATABASE.csv", sep=';')
    df = df.rename(columns={'day/month': 'Date'})
    df = df.rename(columns={'Wind Gust': 'Wind_Gust'})
    df = df.rename(columns={'Wind Speed': 'Wind_Speed'})
    df = df.rename(columns={'Dew Point': 'Dew_Point'})

    for i in range(df.shape[0]):
        df.Date[i] = df.Date[i].replace('Jul', '07.2019').replace('Aug', '08.2019')
        
        df.Time[i] = datetime.strptime(df.Time[i] , "%I:%M %p")
        df.Time[i]  = datetime.strftime(df.Time[i] , "%H:%M")

    df = df.set_index('Date')

    return df

df = parser(DataBase)

def Temperature(event):
    plt.figure(figsize=(20, 10))
    date = df.index.tolist()
    plt.plot(date, df.Temperature,'ro', label = 'Temperature')
    plt.title("Temperature") 
    plt.xlabel("Date", fontsize = 15) 
    plt.ylabel("Temperature", fontsize = 15) 
    plt.grid()
    plt.gcf().autofmt_xdate()
    plt.legend()
    plt.show()

def Dew_Point(event):
    plt.figure(figsize=(20, 10))
    date = df.index.tolist()
    plt.bar(date, df.Dew_Point, label = 'Dew Point')
    plt.title("Dew Point") 
    plt.xlabel("Date", fontsize = 15) 
    plt.ylabel("Dew Point", fontsize = 15) 
    plt.gcf().autofmt_xdate()
    plt.legend()
    plt.show()

def Wind_Speed(event):
    plt.figure(figsize=(20, 10))
    date = df.index.tolist()
    plt.plot(date, df.Wind_Speed, 'ro', label = 'Wind Speed')
    plt.plot(date, df.Wind_Gust, 'bx', label = 'Wind Gust')
    plt.title("Wind Speed") 
    plt.xlabel("Date", fontsize = 15) 
    plt.ylabel("Wind Speed", fontsize = 15) 
    plt.grid()
    plt.gcf().autofmt_xdate()
    plt.legend()
    plt.show()


def Pressure(event):
    plt.figure(figsize=(20, 10))
    date = df.index.tolist()
    plt.barh(date, df.Pressure, label = 'Pressure')
    plt.title("Pressure") 
    plt.xlabel("Date", fontsize = 15) 
    plt.ylabel("Pressure", fontsize = 15) 
    plt.gcf().autofmt_xdate()
    plt.legend()
    plt.show()

def Condition(event): 
    plt.figure(figsize=(20, 10))
    date = df.index.tolist()
    y = df['Condition']
    plt.bar(date, y, label='Condition', color='blue')
    plt.title("Condition  during day")
    plt.xlabel("Date", fontsize=15)
    plt.ylabel("Condition", fontsize=15)
    plt.grid()
    plt.legend()
    plt.gcf().autofmt_xdate()
    plt.show()

f_top = Frame(root) 
f_bot = Frame(root)

b1 = Button(f_top, text="Temperature", width = 40, height = 5)
b2 = Button(f_top, text="Wind_Speed", width = 40, height = 5)
b3 = Button(f_bot, text="Dew_Point", width = 40, height = 5)
b4 = Button(f_bot, text="Pressure", width = 40, height = 5)
b5 = Button(f_bot, text="Condition", width = 40, height = 5)

b1.bind('<Button-1>', Temperature)
b2.bind('<Button-1>', Wind_Speed)
b3.bind('<Button-1>', Dew_Point)
b4.bind('<Button-1>', Pressure)
b5.bind('<Button-1>', Condition)

f_top.pack()
f_bot.pack()
b1.pack(side = LEFT)
b2.pack(side = LEFT)
b3.pack(side = LEFT)
b4.pack(side = LEFT)
b5.pack(side = LEFT)




root.mainloop()

print(df)


