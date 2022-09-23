import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.ttk import *


root = tk.Tk()
root.title("Rpg way finder")
root.geometry('1080x800')

#Escala adaptavel
normal_width = 1920
normal_height = 1080
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
percentage_width = screen_width / (normal_width / 100)
percentage_height = screen_height / (normal_height / 100)
scale_factor = ((percentage_width + percentage_height) / 2) / 100


user_name = tk.StringVar()
main = ttk.Frame(root, padding=(20, 10, 20, 0))
main.grid(row=1, column=0,sticky="NE")

root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

#Escolha das cidades
name_label = ttk.Label(main, text="Name:")
combo = Combobox(main,width=27)
combo['values']= ("Aldeia do Mundo dos Sonhos", "Aldeia do Paladino", "Altrim", "Bek'ground", "Cidade Submarina dos Dhanariatis",
                  "Cidadela de Khalmyr","Colinas dos Bons Halflings","Cosamhir","Curanmir","Doher",
                  "Durtras","Farddenn","Fenn","Fillene","Gallienn","Kannilar","Khalifor","Lendilkar","Lenórien","Lenórienn","Malpetrim",
                  "Nhardmaren","Norm", "Pequena Colina", "Ragnarkhorrangor", "Rarnaakk", "Remnora", "Shanower", "Tiberus", "Trandia",
                  "Triumphus","Triunphus","Trokhard","Valkaria","Vectora","Vectoria","Vila","Vila do Arkam","Willen","Zakharin")
combo["state"]= "readonly"
combo.current(0)
combo.grid(column=0, row=0)
combo2 = Combobox(main,width=27)
combo2['values']= ("Aldeia do Mundo dos Sonhos", "Aldeia do Paladino", "Altrim", "Bek'ground", "Cidade Submarina dos Dhanariatis",
                  "Cidadela de Khalmyr","Colinas dos Bons Halflings","Cosamhir","Curanmir","Doher",
                  "Durtras","Farddenn","Fenn","Fillene","Gallienn","Kannilar","Khalifor","Lendilkar","Lenórien","Lenórienn","Malpetrim",
                  "Nhardmaren","Norm", "Pequena Colina", "Ragnarkhorrangor", "Rarnaakk", "Remnora", "Shanower", "Tiberus", "Trandia",
                  "Triumphus","Triunphus","Trokhard","Valkaria","Vectora","Vectoria","Vila","Vila do Arkam","Willen","Zakharin")
combo2["state"]= "readonly"
combo2.current(0)
combo2.grid(column=1, row=0, padx=(0,20))

#def handle_selection(event):
    #print("Ir da cidade", combo.get())
    #print("para a cidade", combo2.get())
    #print(combo.current())
    #print(combo2.current())

#combo.bind("<<ComboboxSelected>>", handle_selection)
#combo2.bind("<<ComboboxSelected>>", handle_selection)

#sair
buttons = ttk.Frame(root, padding=(20, 10))
buttons.grid(row=1, column=0, sticky="SE")
buttons.columnconfigure(0, weight=1)
buttons.columnconfigure(1, weight=1)
quit_button = ttk.Button(buttons, text="Sair", command=root.destroy)
quit_button.grid(row=0, column=1, sticky="EW")

#Mapa
map = ttk.Frame(root, padding=(20, 10))
map.grid(row=1, column=0,sticky="SW")
map.columnconfigure(0, weight=1)
map.columnconfigure(1, weight=1)
img = Image.open("map.jpg").resize((900,600))
photo = ImageTk.PhotoImage(img)
label = ttk.Label(map, image=photo, padding=5)
label.pack()


root.mainloop()
