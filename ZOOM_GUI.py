import webbrowser
import tkinter as tk
from functools import partial
import random
classes = {'physics': 'https://us02web.zoom.us/j/85914273974?pwd=bGJkcjJwWURiQmY5TXI1cjBsaUp3UT09',
     'french': 'https://us02web.zoom.us/j/82801323935?pwd=QVVzYUdDNysxbGJHWFlKTFpiYS9BQT09',
     'stats': 'https://us02web.zoom.us/j/3626433862?pwd=MVpSWkYvQjdtMS9yaituakpaY09udz09',
     'english': 'https://us02web.zoom.us/j/6582756454?pwd=SHlzSXhlUlRvaldvMEFIdTNDSFhqUT09',
     'drawing': 'https://meet.google.com/lookup/dwbdbgmbdi?authuser=0&hs=179'}

def select_class(classes):
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
    
def join_class(classkey,classes):
    url = classes.get(classkey)
    webbrowser.open(url)

select_class(classes)
