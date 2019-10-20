import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk

HEIGHT = 500
WIDTH = 600
root = tk.Tk()
root.title("Przelicznik")

def naC(temp):
    converted = (5/9) * (float(temp)-32)
    converted = round(converted, 2)
    cEntry.delete(0, tk.END)
    cEntry.insert(0, converted)

def naF(temp):
    converted = (9/5) * float(temp) + 32
    converted = round(converted, 2)
    fEntry.delete(0, tk.END)
    fEntry.insert(0, converted)

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
bg_image = ImageTk.PhotoImage(Image.open("./bg.png"))
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)


frame = tk.Frame(root, bg='#80c1ff')
frame.place(rely=0.05, relx = 0.1, relwidth=0.8, relheight=0.8)

tempLabel = tk.Label(frame, text='Przelicznik temperatur:', bg='#80c1ff', font=('Tahoma', 15))
tempLabel.place(relwidth=1, relheight=0.1)

cLabel = tk.Label(frame, text='[C°]', bg='#80c1ff', font=('Tahoma', 25))
cLabel.place(rely=0.1, relx=0.01, relwidth=0.15, relheight=0.12)
fLabel = tk.Label(frame, text='[F°]', bg='#80c1ff', font=('Tahoma', 25))
fLabel.place(rely=0.26, relx=0.01, relwidth=0.15, relheight=0.12)
cEntry = tk.Entry(frame, font=('Tahoma', 15))
cEntry.place(rely=0.12, relx = 0.18, relwidth=0.5, relheight=0.1)
fEntry = tk.Entry(frame, font=('Tahoma', 15))
fEntry.place(rely=0.28, relx = 0.18, relwidth=0.5, relheight=0.1)

cButton = tk.Button(frame, text='Konwertuj\nna F°', command=lambda: naF(cEntry.get()), font=('Tahoma', 10))
cButton.place(rely=0.12, relx=0.7, relwidth=0.28, relheight = 0.1)
fButton = tk.Button(frame, text='Konwertuj\nna C°', command=lambda: naC(fEntry.get()))
fButton.place(rely=0.28, relx=0.7, relwidth=0.28, relheight = 0.1)

root.mainloop()

