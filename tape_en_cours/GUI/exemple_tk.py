from tkinter import *
from tkinter import ttk

import time
import threading

from tape_en_cours.GUI.metier import traitement_donnees


def on_click_sync():
    # print("on m'a cliqué")
    # time.sleep(15)
    # try:
    #     var_label.set(int(value1.get()) + int(value2.get()))
    # except ValueError:
    #     var_label.set("Des nombres SVP")
    # print("on a mis a jour la valeur")
    res = traitement_donnees(value1.get(), value2.get())
    var_label.set(res)


def on_click():
    print("debut on click")
    t = threading.Thread(target=on_click_sync)
    t.start()
    print("fin on click")


# class Button():
#     def react_on_event(self, event):
#         if event == "clic gauche":
#             self.command()
# bouton = Button(fenetre, text="cliquez-moi !", command=on_click())

fenetre = Tk()

value1 = StringVar()
value2 = StringVar()
var_label = StringVar()

entry_nombre1 = Entry(fenetre, textvariable=value1)
entry_nombre2 = Entry(fenetre, textvariable=value2)
bouton = Button(fenetre, text="cliquez-moi !", command=on_click)
label = Label(fenetre, textvariable=var_label)

entry_nombre1.pack()
entry_nombre2.pack()
bouton.pack()
label.pack()


fenetre.mainloop()
