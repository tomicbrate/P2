import random

imena = ['Karlo', 'Ana-Marija', 'Antonio', 'Marko', 'Matea', 'Vice', 'Sara', 'Ivana', 'Ante', 'Ivan Entoni', 'Tonka',
             'Antonio', 'Mateo', 'Mateo', 'Josip', 'Marko', 'Tino', 'Azer', 'Tomislava', 'Katarina', 'Karlo', 'David',
             'Ivan', 'Petar', 'Marija', 'Antonio', 'Mario', 'Josip', 'Leonardo', 'Antonio', 'Renato', 'Matej', 'Matej',
             'Jozo Matej', 'Petar', 'Ivan', 'Stjepan', 'Petar', 'Dražen', 'Zvonimir', 'Marin', 'Antonio', 'Stipe', 'Ana',
             'Mate', 'Miroslav', 'Karlo', 'Marino', 'Mija', 'Kristijan', 'Ante', 'Ana', 'Iva', 'Mladen', 'Ivan', 'Frano',
             'Mate', 'Mateo', 'Harun']

ocjene = []
for ime in imena:
    ocjena = random.randint(1, 5)
    ocjene.append({"ime": ime, "ocjena": ocjena})

broj_ocjena = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

for ime in ocjene:
    ocjena = ime["ocjena"]
    broj_ocjena[ocjena] += 1

prolaznost = sum(broj_ocjena[ocjena] for ocjena in range(2, 6)) / sum(broj_ocjena.values()) * 100

print("Broj ocjena:", broj_ocjena)
print("Prosjecna prolaznost:", prolaznost, "%")
