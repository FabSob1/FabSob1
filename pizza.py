#Program porównujący ilość pizzy pomiędzy trzema pizzami z reztauracji
#Znajdź restaurację i za pomocą wbudowanej biblioteki
#Dane nazwa_restauracji, nazwa_pizzy, 3xrozmiar_pizzy, 3xcena_pizzy

import sys
import math

wyniki = sys.argv

def printing_pizza():
    pizza1 = []
    pizza2 = []
    pizza3 = []
    pizza1.append(wyniki[1:5])
    pizza2.append(wyniki[1:3])
    pizza3.append(wyniki[1:3])

    pizza2.append(wyniki[5:7])
    pizza3.append(wyniki[7:9])

    print(pizza1)
    print(pizza2)
    print(pizza3)

def porownaj(wyniki):

    printing_pizza()
    
    koszt = []
    ilosc = []

    rozmiar1 = str(wyniki[3])
    cena1  = str(wyniki[4])
    rozmiar2 = str(wyniki[5])
    cena2 = str(wyniki[6])
    rozmiar3 = str(wyniki[7])
    cena3 = str(wyniki[8])
    
    rozmiar1 = int(rozmiar1)
    rozmiar2 = int(rozmiar2)
    rozmiar3 = int(rozmiar3)

    cena1 = int(cena1)
    cena2 = int(cena2)
    cena3 = int(cena3)

    pi = 3.14

    pole1 = (rozmiar1 * rozmiar1 * pi)/2
    pole2 = (rozmiar2 * rozmiar2 * pi)/2
    pole3 = (rozmiar3 * rozmiar3 * pi)/2

    najlepsza  = cena1 / pole1
    naj = "Najmniejsza pizza jest najbardziej opłacalna"
    if najlepsza > cena2 / pole2:
        najlepsza = cena2 / pole2
        naj = "Średnia pizza jest najbardziej opłacalna"
    
    if najlepsza > cena3 / pole3:
        najlepsza = cena3 / pole3
        naj = "Największa pizza jest najbardziej opłacalna"
    print(naj)

porownaj(wyniki)
