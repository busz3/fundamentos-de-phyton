import tkinter as tk
import random

root = tk.Tk()
root.geometry('400x400')

frame = tk.Frame(root, bg='#ffff00')
frame.place(y=0, x=0, relheight=1, relwidth=1)

# Gerar cor aleatória
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
color = f'#{r:02x}{g:02x}{b:02x}'
frame.config(bg=color)

root.mainloop()
