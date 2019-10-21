import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import requests


HEIGHT = 450
WIDTH = 400

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

def naPLN(amount):
    converted = float(amount) * float (priceUSD)
    converted = round(converted, 2)
    plnEntry.delete(0, tk.END)
    plnEntry.insert(0, converted)

def naUSD(amount):
    converted = float(amount) / float (priceUSD)
    converted = round(converted, 2)
    usdEntry.delete(0, tk.END)
    usdEntry.insert(0, converted)

url = 'http://api.nbp.pl/api/exchangerates/rates/a/usd?format=json'
try:
    response = requests.get(url=url)
    data = response.json()
    priceUSD = data['rates'][0]['mid']
except:
    priceUSD = 'Błąd połączenia'

root = tk.Tk()
root.title("Przelicznik")
root.minsize(WIDTH, HEIGHT)

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
bg_image = ImageTk.PhotoImage(Image.open("./bg.png"))
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff')
frame.place(rely=0.05, relx = 0.1, relwidth=0.8, relheight=0.8)

tempLabel = tk.Label(frame, text='Przelicznik temperatur:', bg='#80c1ff', font=('Tahoma', 14))
tempLabel.place(relwidth=1, relheight=0.1)

cLabel = tk.Label(frame, text='[C°]', bg='#80c1ff', font=('Tahoma', 20))
cLabel.place(rely=0.1, relx=0.01, relwidth=0.20, relheight=0.12)
cEntry = tk.Entry(frame, font=('Tahoma', 15))
cEntry.place(rely=0.12, relx = 0.23, relwidth=0.4, relheight=0.1)
cButton = tk.Button(frame, text='Konwertuj\nna F°', command=lambda: naF(cEntry.get()), font=('Tahoma', 10))
cButton.place(rely=0.12, relx=0.68, relwidth=0.28, relheight = 0.11)

fLabel = tk.Label(frame, text='[F°]', bg='#80c1ff', font=('Tahoma', 20))
fLabel.place(rely=0.26, relx=0.01, relwidth=0.20, relheight=0.12)
fEntry = tk.Entry(frame, font=('Tahoma', 15))
fEntry.place(rely=0.28, relx = 0.23, relwidth=0.4, relheight=0.1)
fButton = tk.Button(frame, text='Konwertuj\nna C°', command=lambda: naC(fEntry.get()))
fButton.place(rely=0.28, relx=0.68, relwidth=0.28, relheight = 0.11)

currencyLabel = tk.Label(frame, text="Przelicznik Walut: ", bg='#80c1ff', font=('Tahoma', 14))
currencyLabel.place(rely = 0.4, relwidth=1, relheight=0.15)

plnLabel = tk.Label(frame, text='[PLN]', bg='#80c1ff', font=('Tahoma', 18))
plnLabel.place(rely=0.56, relx=0.01, relwidth=0.2, relheight=0.12)
plnEntry = tk.Entry(frame, font=('Tahoma', 15))
plnEntry.place(rely=0.58, relx = 0.23, relwidth=0.4, relheight=0.1)
plnButton = tk.Button(frame, text='Konwertuj\nna USD', command=lambda: naUSD(plnEntry.get()), font=('Tahoma', 10))
plnButton.place(rely=0.58, relx=0.68, relwidth=0.28, relheight = 0.11)

usdLabel = tk.Label(frame, text='[USD]', bg='#80c1ff', font=('Tahoma', 18))
usdLabel.place(rely=0.72, relx=0.01, relwidth=0.2, relheight=0.12)
usdEntry = tk.Entry(frame, font=('Tahoma', 15))
usdEntry.place(rely=0.74, relx = 0.23, relwidth=0.4, relheight=0.1)
usdButton = tk.Button(frame, text='Konwertuj\nna PLN', command=lambda: naPLN(usdEntry.get()))
usdButton.place(rely=0.74, relx=0.68, relwidth=0.28, relheight = 0.11)

rateText = "Obecny kurs USD: " + str(priceUSD) + "zl"
usdRate = tk.Label(frame, text=rateText, bg='#80c1ff', font=('Tahoma', 10))
usdRate.place(rely=0.86, relwidth=1, relheight=0.05)

footerText = "Białecki & Jankiewicz A.D. 2019"
footer = tk.Label(frame, text=footerText, bg='#70b0ee', font=('System', 10))
footer.place(rely=0.93, relx=0.02, relwidth=0.97, relheight = 0.05)

root.mainloop()
