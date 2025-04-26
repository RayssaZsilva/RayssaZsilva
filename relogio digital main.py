import tkinter as tk 
from time import strftime

root = tk.Tk()
root.title("Relogio Digital")

def relogio():
    hora = strftime ('%H:%M:%S')
    label.config(text=hora)
    label.after(1000, relogio)
label = tk.Label(root, font=('Helvetica', 48),
                 background='hex',  foreground='cyan')
label.pack(anchor='center')

relogio()
root.mainloop() 
