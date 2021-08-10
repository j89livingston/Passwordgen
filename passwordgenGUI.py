#import dependencies

import tkinter as tk
from tkinter import ttk
from tkinter.constants import BOTTOM, CENTER, END, LEFT, N, NW, RIGHT, TOP
from tkinter import *
import random
import string

window = tk.Tk()
window.title("SPG")
window.geometry("615x240")
window.resizable(width=False, height=False)

# FUNCTIONS

# Number Generator
def gen():
    LC = string.ascii_lowercase
    if Checkbutton1.get() == 1:
      LC += string.ascii_uppercase 
    if Checkbutton2.get() == 1:
      LC += string.digits
    if Checkbutton3.get() == 1:
      LC += string.punctuation
    return ''.join(random.choice(LC) for x in range(random.randint(8,16)))
    

#generator code display
def gen_display():
    showup = str(gen())
    fare_display = entry_km
    fare_display.delete(0, END)
    fare_display.insert(tk.END, showup)

# copy button code
def copy_button():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(entry_km.get()) 
    clip.destroy()
    

# LABEL for Head and Sub

label_head = tk.Label(text="Simple Password Generator", font=("The New Roman", 36))
label_head.pack(side=tk.TOP)

label_enter = tk.Label(text='Click "GENERATE" to start', font=("The New Roman", 16))
label_enter.place(x=215, y=55)


#  TEXT ENTRY
entry_km = tk.Entry(font=("The New Roman", 36), justify='center', width=16,)
entry_km.place(x=25, y=97) #25 95
entry_km.delete(0, END)

# Generate Button

button_submit = tk.Button(window, text="GENERATE", font=("The New Roman", 14), 
                          height=3, 
                          width=10, 
                          bg='blue', 
                          command=gen_display, 
                          
                          ) 
button_submit.place(x=500, y=97)

# Creating a photoimage object to use image
photo = PhotoImage(file = '~/Documents/Python_Projects/Passwordgen/Resources/copyicon.png')
photo = photo.zoom(10,10)
photo = photo.subsample(35)

# set image on button
copy_button1 = tk.Button(window, text = 'COPY', font=("The New Roman", 14), 
                        image = photo, 
                        compound="left",
                        command=copy_button, 
                        padx=10, 
                        pady=17
                        )
copy_button1.place(x=410, y=97)


# CheckButton 1,2,3

Checkbutton1 = IntVar(value=1)  
Checkbutton2 = IntVar(value=1)
Checkbutton3 = IntVar(value=1)

Button1 = Checkbutton(window, text = "Case-Sensitve",
                      selectcolor= 'blue',
                      variable = Checkbutton1,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 15,
                      justify='left'
                      )
  
Button2 = Checkbutton(window, text = "Include Numbers",
                      variable = Checkbutton2,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 15,
                      selectcolor='blue',
                      justify='right'
                      )

Button3 = Checkbutton(window, text = "Include Symbols",
                      variable = Checkbutton3,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 14,
                      selectcolor='blue',
                      justify='right'
                      )
                      

Button1.place(x=50, y=180)
Button2.place(x=230, y=180)
Button3.place(x=410, y=180)


window.mainloop()