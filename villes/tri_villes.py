from math import radians, sin, cos, atan2, sqrt
from tkinter import *
from tkinter import filedialog
import csv
import time

class Ville :
    def __init__(self, nom_commune, codes_postaux, latitude, longitude, dist, distanceFromGrenoble):
        self.nom_commune = nom_commune
        self.codes_postaux = codes_postaux
        self.latitude = latitude
        self.longitude = longitude
        self.dist = dist
        self.distanceFromGrenoble = distanceFromGrenoble


def loadFile():
    listVille.clear()
    filename = filedialog.askopenfilename(initialdir="./",
                                          title="Selection du Fichier",
                                          filetypes=(("Text files",
                                                      "*.csv*"),
                                                     ("all files",
                                                      "*.*")))
    changeLabelFile("Fichier : "+filename)
    with open(filename, 'r', encoding='UTF-8') as file:
        csvreader = csv.reader(file)
        next(csvreader)  # skip header line
        for row in csvreader:
            data = row[0].split(";")
            try:
                ville = Ville(data[8], data[9], float(data[11]), float(data[12]), float(data[13]), 0)
                ville.distanceFromGrenoble = getDistanceFromGrenoble(ville)
                listVille.append(ville)
            except:
                continue


def getDistanceFromGrenoble(ville):
    R = 6373.0

    lat1 = radians(45.166672)
    lon1 = radians(5.71667)
    lat2 = radians(ville.latitude)
    lon2 = radians(ville.longitude)

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c

    return distance

def isLess(listVille, i, j):
    if listVille[i].distanceFromGrenoble > listVille[j].distanceFromGrenoble:
     return True


def swap(listVille, i, j):
    villeTemp= listVille[i]
    listVille[i] = listVille[j]
    listVille[j] = villeTemp

def changeLabelFile(text):
    labelFileExplorer = Label(fenetre,
                              text=text,
                              width=120, height=4,
                              fg="black", background="#579BB1")
    labelFileExplorer.place(x=150, y=offset + 40)


def changeLabelButtonSubmit(text):
    buttonValidation['text'] = text
    buttonValidation.place(x=150, y=offset + 120)


def onSelectTypeTri(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        global typeTriSelection
        typeTriSelection = data
        changeLabelButtonSubmit("Lancement du {}".format(data))


def sort():
    # effacement de la liste affichée
    listVilleSortedBox.delete(0, END)
    listVilleSorted = listVille.copy()

    if typeTriSelection == "Tri par insertion":
        listVilleSorted = insertsort(listVilleSorted)
    elif typeTriSelection == "Tri par sélection":
        listVilleSorted = selectionsort(listVilleSorted)
    elif typeTriSelection == "Tri à bulles":
        listVilleSorted = bubblesort(listVilleSorted)
    elif typeTriSelection == "Tri de Shell":
        listVilleSorted = shellsort(listVilleSorted)
    elif typeTriSelection == "Tri par fusion":
        listVilleSorted = mergesort(listVilleSorted)
    elif typeTriSelection == "Tri par tas":
        listVilleSorted = heapsort(listVilleSorted)
    elif typeTriSelection == "Tri rapide":
        listVilleSorted = quicksort(listVilleSorted)

    for ville in range(len(listVilleSorted)):
        listVilleSortedBox.insert(END, listVilleSorted[ville].nom_commune + " - " + str(listVilleSorted[ville].distanceFromGrenoble))
        listVilleSortedBox.itemconfig(ville, fg="black")

    listVilleSortedBox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listVilleSortedBox.yview)


def insertsort(listVille):
    for i in range(0, len(listVille)):
        en_cour = listVille[i]
        j = i
        while j > 0 and listVille[j - 1].distanceFromGrenoble > en_cour.distanceFromGrenoble:
            listVille[j] = listVille[j - 1]
            j = j - 1

        listVille[j] =  en_cour

    return listVille



def selectionsort(listVille):
    def swap(idxi, idxj):
        temp = listVille[idxi]
        listVille[idxi] = listVille[idxj]
        listVille[idxj] = temp

    nb = len(listVille)
    for i in range(0, nb):
        min = i
        for j in range(i + 1, nb):
            if listVille[j].distanceFromGrenoble < listVille[min].distanceFromGrenoble:
                min = j
        swap(i, min)

    return (listVille)

    return listVille

def swap(idxi, idxj):
    temp = listVille[idxi]
    listVille[idxi] = listVille[idxj]
    listVille[idxj] = temp

def bubblesort(listVille):
    passage = 0
    permutation = True
    while permutation == True:
        permutation = False
        passage = passage + 1
        for i in range(0, len(listVille) - passage):
            if listVille[i].distanceFromGrenoble > listVille[i + 1].distanceFromGrenoble:
                permutation = True
                listVille[i], listVille[i + 1] = listVille[i + 1], listVille[i]
    return listVille



def shellsort(listVille):
    espacements = []
    longueur = len(listVille)
    e = 0
    while e < longueur:
        e = (3 * e + 1)
        espacements.insert(0, e)

    for e in espacements:
        for i in range(longueur):
            valeur = listVille[i]
            j = i
            while j > e - 1 and listVille[j - e].distanceFromGrenoble > valeur.distanceFromGrenoble:
                listVille[j] = listVille[j - e]
                j = j - e
            listVille[j] = valeur

    return listVille


def mergesort(listVille):
    print("implement me !")
    return listVille


def heapsort(listVille):
    print("implement me !")
    return listVille


def quicksort(listVille):
    if not listVille:
        return []
    else:
        pivot = listVille[-1]
        plus_petit = [x for x in listVille if x.distanceFromGrenoble < pivot.distanceFromGrenoble]
        plus_grand = [x for x in listVille[:-1] if x.distanceFromGrenoble >= pivot.distanceFromGrenoble]
        return quicksort(plus_petit) + [pivot] + quicksort(plus_grand)

    print(quicksort(listVille))
    return listVille




# Creation de la fenêtre
fenetre = Tk()
width = 1000
height = 180
offset = 10
listVille = []
listTri = ["Tri par insertion",
           "Tri par sélection",
           "Tri à bulles",
           "Tri de Shell",
           "Tri par fusion",
           "Tri par tas",
           "Tri rapide"]

typeTriSelection = "Tri par insertion"

labelFileExplorer = Label()
canvas = Canvas(fenetre, width=width + 2*offset,
                height=height + 2*offset, bg='white')
buttonValidation = Button(command=sort)

list = Listbox(fenetre, width=20, height=len(listTri), selectmode="single")
list.place(x=offset, y=offset)
list.bind("<<ListboxSelect>>", onSelectTypeTri)

for typeTri in range(len(listTri)):
    list.insert(END, listTri[typeTri])
    list.itemconfig(typeTri, fg="black")

buttonFile = Button(
    fenetre, text="Importation du fichier", command=loadFile)
buttonFile.place(x=150, y=offset)

changeLabelButtonSubmit("Lancement du {}".format(typeTriSelection))

changeLabelFile("Aucun Fichier ...")

canvas.pack()

listVilleSortedBox = Listbox(
    fenetre, width=100, height=25, selectmode="single")
listVilleSortedBox.pack(side=LEFT, fill=BOTH)

scrollbar = Scrollbar(fenetre, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=BOTH)
fenetre.mainloop()
