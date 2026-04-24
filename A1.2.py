import tkinter as tk

root = tk.Tk()
root.geometry('400x400')

# Cor rosa
rosa = '#FFC0CB'

frame = tk.Frame(root, bg=rosa)
frame.place(y=0, x=0, relheight=1, relwidth=1)

root.mainloop()