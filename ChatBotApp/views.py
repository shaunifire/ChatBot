from django.shortcuts import render
#from .models import Odpowiedz
import random
def odpowiedz_bota(request):
    return render (request, 'C:/Users/student/Desktop/repozytorium/ChatBot/ChatBotApp/baza_danych1.csv', {})


chosen=0

    #chosen == 99 to zmienna kontrolna, która zmieni się gdy zostanie wysłana informacja z templatki z kliknięciem na button. Ponieważ będzie ona miała wartość zgodną z randomową liczbą wybraną prze kompa, muszę jej nadać kontrolną liczbę która NA PEWNO nie wystąpi podczaslosowania.
def funkcja_buttona(request):
    chosen=1
    return test(request,chosen)
    #ładujemy bazę danych

def test (request, chosen):
    import os
    import pandas
    import csv
    lista=[]
    with open('C:/Users/student/Desktop/repozytorium/ChatBot/ChatBotApp/baza_danych1.csv', 'r', newline='\n') as csvfile:
        data=csv.reader(csvfile)
        dictionary=[]
        for row in data:
            dictionary.append(row[0].split(";"))
    #Ładujemy pytania do bota które wrzucimy pod buttony. Zrobiłam to bez pętli, żeby moja partnerka rozumiała co się dzieje.
    pytanie1=random.randint (0,len(dictionary)-1)
    pytanie2=random.randint (0,len(dictionary)-1)
    pytanie3=random.randint (0,len(dictionary)-1)
    pytanie4=random.randint (0,len(dictionary)-1)
    button1=dictionary[pytanie1][0]
    button2=dictionary[pytanie2][0]
    button3=dictionary[pytanie3][0]
    button4=dictionary[pytanie4][0]
    #testowa=pytanie1
        #zmienna chosen jest wysyłana do nas za drugim załadowaniem
    #if chosen==1:
    odpowiedz=random.randint(1,dictionary[chosen])
    odpowiedz_bota_z_listy=dictionary[chosen][odpowiedz]
    return render (request, 'C:/Users/student/Desktop/repozytorium/ChatBot/ChatBotApp/templates/odpowiedz.html', {"testowa":testowa, "button1":button1,"button2":button2,"button3":button3,"button4":button4, "odpowiedz_bota_z_listy":odpowiedz_bota_z_listy} )
#    else:
        #return render (request, 'C:/Users/student/Desktop/repozytorium/ChatBot/ChatBotApp/templates/odpowiedz.html', #{"button1":button1,"button2":button2,"button3":button3,"button4":button4, "odpowiedz_bota_z_listy":"ddddddddddkdkdkdkdkd"} )
