def pozdrav_ime(ime):
    return f"Pozdrav {ime}!"

dobrodosao_ime = lambda ime: f"Dobrodošao {ime}!"

def pozovi_funkciju(funkcija, ime):
    return funkcija(ime)

ime = "Mladen"

rezultat1 = pozovi_funkciju(pozdrav_ime, ime)
rezultat2 = pozovi_funkciju(dobrodosao_ime, ime)

print(rezultat1)
print(rezultat2)