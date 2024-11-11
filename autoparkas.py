# 1. Raskite, kurių gamintojų automobilių yra daugiau nei vienas, 
# ekrane atspausdinkite gamintojų pavadinimus. 
# 2. Sudarykite visų pasirinkto gamintojo (pvz.: „Volvo“) automobilių 
# sąrašą, ekrane atspausdinkite automobilio valstybinį numerį, modelį, bei 
# pagaminimo metus. Jei tokio automobilio sąraše nėra atspausdinkite 
# pranešimą - "Tokio gamintojo automobilių sąraše nėra".
# 3. Sudarykite sąrašą, senesnių nei 10 metų, į failą „Senienos.csv“ 
# surašykite visus jų duomenis. Jei senienų programa neranda atspausdinkite 
# pranešimą ekrane - "Senesnių nei 10 metų automobilių sąraše nėra".


# Reikalavimai: Naudoti sąrašus arba žodynus, failų skaitymą ir rašymą, 
# funkcijas.

from collections import defaultdict


autoparkas = []
with open('./autoparkas.txt', encoding="utf8") as failas:
    for eilute in failas:
        eilute = eilute.rstrip('\n')
        isskaidyta = eilute.split(',')
        auto = dict(
        nr = isskaidyta[0],
        marke = isskaidyta[1],
        modelis = isskaidyta[2],
        metai = isskaidyta[3],
        )
        autoparkas.append(auto)

print(autoparkas)

def automobiliai(autoparkas):
    gamintojas_skaic = defaultdict(int)
    for auto in autoparkas:
        gamintojas_skaic[auto['marke']] += 1
    gamintojai = [marke for marke, count in gamintojas_skaic.items() if count > 1]
    print("Gamintojai, kurių automobilių yra daugiau nei vienas: ", gamintojai)

def sarasas_pagal_gamintoja(autoparkas, pasirinktas_gamintojas):
    automobiliai = [auto for auto in autoparkas if auto['marke'] == pasirinktas_gamintojas]
    if automobiliai:
        for auto in automobiliai:
            print(f"Valstybinis numeris: {auto['nr']}, Modelis: {auto['modelis']}, Metai: {auto['metai']}")
    else:
        print("Tokio gamintojo automobilių sąraše nėra")


def seni_automobiliai(autoparkas):
    sie_metai = datetime.now().year
    seni_automobiliai = [auto for auto in autoparkas if sie_metai - auto['metai'] > 10]
    
    if seni_automobiliai:
        with open('Senienos.csv', mode='w', newline='', encoding='utf8') as file:
            writer = csv.writer(file)
            writer.writerow(['Valstybinis numeris', 'Marke', 'Modelis', 'Metai'])
            for auto in seni_automobiliai:
                writer.writerow([auto['nr'], auto['marke'], auto['modelis'], auto['metai']])
    else:
        print("Senesnių nei 10 metų automobilių sąraše nėra")
