import csv
import time
import datetime
from tkinter import *
from tkinter.messagebox import showinfo
import sys
import os

def clearbox():
    entrybericht.delete(0, END)
    entrynaam.delete(0, END)
    entrywoonplaats.delete(0, END)

def berichtcontrole():
    bericht = entrybericht.get()
    naam = entrynaam.get()
    woonplaats = entrywoonplaats.get()
    totaal = bericht + naam + woonplaats
    if len(bericht) > 124 or len(bericht) <= 0:
        popup = "Sorry, uw bericht dient minimaal 1 en maximaal 124 karakters te bevatten."
        showinfo(title="Error", message=popup)
    if len(naam) > 124 or len(naam) <= 0:
        popup = "Sorry, uw naam dient minimaal 1 en maximaal 124 karakters te bevatten."
        showinfo(title="Error", message=popup)
    if len(woonplaats) > 124 or len(woonplaats) <= 0:
        popup = "Sorry, uw woonplaats dient minimaal 1 en maximaal 124 karakters te bevatten."
        showinfo(title="Error", message=popup)
    if len(totaal) > 124 or len(totaal) <= 0:
        popup = "Sorry, uw totaal aantal karakters is hoger dan 124."
        showinfo(title="Error", message=popup)
    if len(bericht) > 0 and len(bericht) <= 124 and len(naam) > 0 and len(naam) <= 124 and len(woonplaats) > 0 and len(woonplaats) <= 124 and len(totaal) > 0 and len(totaal) <= 124:
        popup = "Uw bericht is verzonden"
        showinfo(title="Verzonden", message=popup)
        vandaag = datetime.datetime.today()
        s = vandaag.strftime("%a %d %b %Y, at %H:%M:%S,")
        queue = 'queue.csv'
        with open(queue, 'a', newline='') as csvfile:
            berichtwriter = csv.writer(csvfile, delimiter=';')
            berichtwriter.writerow((s, bericht, naam, woonplaats))
        csvfile.close()
        clearbox()


root = Tk()

labelbericht = Label(master=root,
              text="Geef hier uw mening",
              width=40,
              height=1,)
labelbericht.pack()
entrybericht = Entry(master=root)
entrybericht.pack(pady=10)

labelnaam = Label(master=root,
              text="Geef hier uw voornaam op (optioneel)",
              width=40,
              height=1,)
labelnaam.pack()
entrynaam = Entry(master=root)
entrynaam.pack(pady=10)

labelwoonplaats = Label(master=root,
              text="Geef hier uw woonplaats op (optioneel)",
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
