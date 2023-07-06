from csv import reader

with open('rezultati.csv', 'r', encoding="utf8") as read_obj:
    csv_reader = reader(read_obj)
    studenti = list(map(tuple, csv_reader))

studenti.sort(key=lambda el: el[1])

ocjene_dict = {}

def calculate_grade(bodovi):
    if bodovi >= 90:
        return 'Izvrstan'
    elif bodovi >= 80:
        return 'Vrlo dobar'
    elif bodovi >= 65:
        return 'Dobar'
    elif bodovi >= 50:
        return 'Dovoljan'
    else:
        return 'Nedovoljan'

for student in studenti:
    prezime = student[1]
    bodovi = int(student[2])
    ocjena = calculate_grade(bodovi)
    
    if ocjena in ocjene_dict:
        ocjene_dict[ocjena] += 1
    else:
        ocjene_dict[ocjena] = 1

print(studenti)
print(ocjene_dict)