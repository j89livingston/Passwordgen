#import dependencies

import tkinter as tk
from tkinter.constants import BOTTOM, CENTER, END, N, NW, TOP
import random
from typing import Text

window = tk.Tk()

window.title("SPG")

window.geometry("525x200")

# FUNCTIONS

# shuffle feature for generator
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

# generator code
def gen():
 
    uppercase1 = chr(random.randint(65,90))
    uppercase2 = chr(random.randint(65,90))
    lowercase1 = chr(random.randint(97,122))
    lowercase2 = chr(random.randint(97,122))
    digit1 = chr(random.randint(48,57))
    digit2 = chr(random.randint(48,57))
    punctuation1 = chr(random.randint(33,152))
    punctuation2 = chr(random.randint(33,152))
    password = uppercase1 + uppercase2 + lowercase1 + lowercase2 + digit1 + digit2 + punctuation1 + punctuation2
    password = shuffle(password)
    
    return password

#generator code display
def gen_display():
    showup = str(gen())
    fare_display = entry_km
    fare_display.delete(0, END)
    fare_display.insert(tk.END, showup)
    

# LABEL

label_head = tk.Label(text="My Simple Password Generator", font=("The New Roman", 36))
label_head.pack(side=TOP)

label_enter = tk.Label(text='Click "GENERATE" to start')
label_enter.pack(side=TOP)


#  TEXT ENTRY
entry_km = tk.Entry(font=("The New Roman", 52), justify='center')
entry_km.pack(side=TOP)
entry_km.delete(0, END)

# button

button_submit = tk.Button(text="GENERATE", bg="pink", command=gen_display) 
button_submit.pack(side=TOP)


window.mainloop()