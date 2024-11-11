# Sukurti Python programą, kuri:

# !!! Sukurtų duomenų bazę ir atliktų nurodytus veiksmus su ja, pasirinktu duomenų bazės apdorojimo principu, naudojant užklausas (sqlite3), arba Pandas dataframe.

# 1. Sukurtų lentelę Saldainiai su stulpeliais: Pavadinimas, Tipas, Kaina/kg, Perkamas kiekis, Suma.
# 2. Užpildytu saldainių duomenų bazę duomenimis iš tekstinio failo saldainiai.txt (jei norite galite pasiversti ir į csv). Ps. (Kainą apskaičiuosime ir įtrauksime)
# 3. Užpildykite stulpelį Suma įtraukdami apskaičiuotas sumos vertes prie atitinkamo saldainio.
# 4. Atspausdintų tik tuos saldainius kurių tipas įvedamas klaviatūra pvz. "Šokoladinis" ir kaina > 5 eur - įvedama klaviatūra.
# 5. Panaikintų input pagalba įvesto saldainio pavadinimo duomenis - ištrintų visą eilutę lentelėje apie tą saldainį.
# 6. Naudodamiesi Seaborn arba Matplotlib Python bibliotekomis, atvaizduokite bent du grafikus (skirtingų tipų - linijinių, stulpelinių, taškinių ar kt. ). Pasitelkite fantaziją ir kūrybą kaip norite ką norite atvaizduokite.  
# Pakaitaliokite grafikų parametrus, pvz. spalvų paletė. Grafikai turi turėti ašių pavadinimus, vertes ant ašių, pavadinimą. Dar gali turėti legendą ar kt. pasirinktą info.

# PASTABA: 
# Spausdinkite tarpinius rezultatus kiekvieną eilutę atskirai. Pvz."Miglė", "Šokoladinis", 6, 2,
# "Miglė", "Šokoladinis", 6, 2,
# "Miglė", "Šokoladinis", 6, 2,

saldainiai = []
with open('saldainiai.txt', encoding="utf8") as failas:
    for eilute in failas:
        eilute = eilute.rstrip('\n')
        print(eilute)
        isskaidyta = eilute.split(',')
        print(isskaidyta)
        saldainis = [
            isskaidyta[0],
            isskaidyta[1],
            float(isskaidyta[2]),
            int(isskaidyta[3])
        ]
        saldainiai.append(tuple(saldainis))
for saldainis in saldainiai:
    print(saldainis)
import sqlite3
conn = sqlite3.connect("saldainiai.db")
c = conn.cursor()
with conn:
    c.execute("CREATE TABLE IF NOT EXISTS saldainiai\
               (pavadinimas text, skonis text, kaina float, kiekis integer)")
    
c.executemany('INSERT OR REPLACE INTO saldainiai (pavadinimas, skonis, kaina, kiekis) VALUES (?, ?, ?, ?)', saldainiai)
c.execute(f"""ALTER TABLE saldainiai ADD COLUMN suma 'float'""")
sarasas = c.execute("SELECT * From saldainiai").fetchall()
for saldainis in sarasas:
    kiekis = saldainis[2] * saldainis[3]

    c .execute(f"UPDATE saldainiai set suma = {kiekis} where pavadinimas = '{saldainis[0]}'")

skonis = input('Iveskite saldainiu pavadinima: ')
kainos_limitas = float(input('Iveskite kainos limita: '))
saldainiai WHERE pavadinimas = ? and kaina < ?"
paieskos_rez = c.execute(f"SELECT * From saldainiai WHERE skonis ='{skonis}' and kaina = '{kainos_limitas}'").fetchall()
print(paieskos_rez)


conn.close()




conn.commit()
conn.close()