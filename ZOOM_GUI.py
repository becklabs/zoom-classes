import time
import webbrowser
import tkinter as tk
from functools import partial
import random
import os
import pandas as pd


def input_classes():
    print('Running first time setup... input class info below')
    print('\n')
    data = pd.DataFrame(columns = ['classkey','url'])
    i = 0
    more_classes = 'y'

    while more_classes == 'y':
        classkey = str(input('Class Name: '))
        url = str(input('Class Meeting Link: '))
        more_classes = str(input('Add another class?(y/n): '))
        data.loc[i,'classkey'] = classkey
        data.loc[i,'url'] = url
        i+=1
    data.to_csv('classes.csv',index=False)

def get_classes():
    if 'classes.csv' not in os.listdir(os.getcwd()):
        input_classes()
    data = pd.read_csv('classes.csv')
    classes = dict(zip(data['classkey'],data['url']))
    return classes

def join_class(classkey,classes):
    url = classes.get(classkey)
    webbrowser.open(url)
    
def select_class():
    classes = get_classes()
    master = tk.Tk()  
    master.geometry('200x300')
    buttons = []
    r = lambda: random.randint(0,255)
    for i in range(len(classes.keys())):
        buttons.append(tk.Button(master,
                                 bg = '#%02X%02X%02X' % (r(),r(),r()),
                                 text=list(classes.keys())[i],
                                 command=partial(join_class, list(classes.keys())[i], classes)))
        buttons[i].grid(row=i, column=3, padx=10, pady=10)
    master.mainloop()

  
select_class()
