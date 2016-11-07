import csv
from tkinter import *

def hoofdmenu():
    labelbericht = Label(master=root,   #Menu met tekst
              text= tweetcontrole(),    #Gaat naar de functie tweetcontrole
              width=50,
              height=8,)
    labelbericht.pack()

    button = Button(master=root,    #Ja knop
                text="Goedkeuren",
                command=japopup)    #Gaat naar de functie japopup
    button.pack(pady=10, side=LEFT)

    button = Button(master=root,    #Nee knop
                text="Afkeuren",
                command=neepopup)   #Gaat naar de functie neepopup
    button.pack(pady=10, side=RIGHT)

def tweetcontrole():    #leest de eerste zin uit de file queue.csv
    queue = 'queue.csv'
    with open(queue, "r") as csvfile:
        berichtreader = csv.reader(csvfile, delimiter=';')
        for line in berichtreader:
            return "Datum en Tijd: " + line [0] + "\n" + "De tweet: " + line[1] + "\n" + "Door: " + line[2] + "\n" + "Uit: " + line[3] #opmaak van het menu
        csvfile.close()
    return tweetcontrole()

def japopup():
    def close():    #sluit de popup
        subwindow.withdraw()
    def goedgekeurdclose(): #activeert de functie tweetgoedkeuren en sluit daarna de popup
        tweetgoedkeuren()
        subwindow.withdraw()

    subwindow = Toplevel(master=root)   #maakt een popup aan
    labelbericht = Label(master=subwindow,  #de tekst in de popup
              text= "Weet u het zeker?",
              width=15,
              height=2,)
    labelbericht.pack()
    button2 = Button(master=subwindow,
                     text = "Ja",
                     command=goedgekeurdclose)  #roept goedgekeurdclose aan
    button2.pack(pady=10, side=LEFT)
    button3 = Button(master=subwindow,
                     text = "Nee",
                     command=close) #roept de functie close aan
    button3.pack(pady=10, side=RIGHT)

def neepopup():
    def close():    #sluit de popup
        subwindow.withdraw()
    def afgekeurdclose():   #activeert de functie tweetafkeuren en sluit daarna de popup
        tweetafkeuren()
        subwindow.withdraw()

    subwindow = Toplevel(master=root)   #maakt een popup aan
    labelbericht = Label(master=subwindow,  #de tekst in de popup
              text= "Weet u het zeker?",
              width=15,
              height=2,)
    labelbericht.pack()
    button2 = Button(master=subwindow,
                     text = "Ja",
                     command=afgekeurdclose)    #roept afgekeurdclose aan
    button2.pack(pady=10, side=LEFT)
    button3 = Button(master=subwindow,
                     text = "Nee",
                     command=close)     #roept de functie close aan
    button3.pack(pady=10, side=RIGHT)

def tweetgoedkeuren():
    queue = 'queue.csv'
    goedgekeurd = 'goedgekeurd.csv'
    with open(queue, "r") as csvfile:   #opent queue.csv
        berichtreader = csv.reader(csvfile, delimiter=';')
        for line in berichtreader:  #leest de eerste zin uit queue.csv
            tekst = line
    csvfile.close()
    with open(goedgekeurd, 'a', newline='') as csvfile: #opent goedgekeurd.csv
        berichtwriter = csv.writer(csvfile, delimiter=';')
        berichtwriter.writerow(tekst)   #schrijft de eerste zin uit queue.csv in goedgekeurd.csv

def tweetafkeuren():
    queue = 'queue.csv'
    afgekeurd = 'afgekeurd.csv'
    with open(queue, "r") as csvfile:   #opent queue.csv
        berichtreader = csv.reader(csvfile, delimiter=';')
        for line in berichtreader:  #leest de eerste zin uit queue.csv
            tekst = line
    csvfile.close()
    with open(afgekeurd, 'a', newline='') as csvfile:   #opent afgekeurd.csv
        berichtwriter = csv.writer(csvfile, delimiter=';')
        berichtwriter.writerow(tekst)   #schrijft de eerste zin uit queue.csv in afgekeurd.csv

root = Tk()
hoofdmenu()
root.mainloop()
