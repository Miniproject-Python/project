import csv
import time
import datetime
from tkinter import *
from tkinter.messagebox import showinfo

def berichtcontrole():
    bericht = entrybericht.get()
    naam = entrynaam.get()
    woonplaats = entrywoonplaats.get()
    if len(bericht + naam + woonplaats) > 140 or len(bericht + naam + woonplaats) <= 0:
        popup = "Sorry, uw bericht dient maximaal 140 karakters en minimaal 1 te bevatten."
        showinfo(title="Error", message=popup)
    if len(bericht + naam + woonplaats) > 0 and len(bericht + naam + woonplaats) <= 140:
        popup = "Uw bericht is verzonden"
        showinfo(title="Verzonden", message=popup)
        vandaag = datetime.datetime.today()
        s = vandaag.strftime("%a %d %b %Y, at %H:%M:%S,")
        queue = 'queue.csv'
        with open(queue, 'a', newline='') as csvfile:
            berichtwriter = csv.writer(csvfile, delimiter=';')
            berichtwriter.writerow((s, bericht, naam, woonplaats))
        csvfile.close()


root = Tk()

labelbericht = Label(master=root,
              text="Geef hier uw mening",
              width=40,
              height=1,)
labelbericht.pack()
entrybericht = Entry(master=root)
entrybericht.pack(pady=10)

labelnaam = Label(master=root,
              text="Geef hier u voornaam op (optioneel)",
              width=40,
              height=1,)
labelnaam.pack()
entrynaam = Entry(master=root)
entrynaam.pack(pady=10)

def jemoederskut():
    naam = entrynaam.get()
    tering = len(naam)
    return tering

labelwoonplaats = Label(master=root,
              text="Geef hier u woonplaats op (optioneel)",
              width=40,
              height=1,)
labelwoonplaats.pack()
entrywoonplaats = Entry(master=root)
entrywoonplaats.pack(pady=10)

labelcounter = Label(master=root,
                     text="Pas op u mag niet meer dan 140 characters gebruiken",
                     width=90,
                     height=1,)
labelcounter.pack()

button = Button(master=root,
                text="Verzend bericht",
                command=berichtcontrole)
button.pack(pady=10)

root.mainloop()
