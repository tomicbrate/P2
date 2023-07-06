import re

unos_emaila = input("Unesite e-mail: ")
regex_emaila = "(^[a-zA-Z].*)[.]([a-zA-Z].*)@fpmoz.sum.ba$"
rezultat_emaila = re.match(regex_emaila, unos_emaila)

unos_eduida = input("Unesite eduId: ")
regex_eduida = "^([a-zA-Z])([a-zA-Z].*)[0-9]*@sum.ba$"
rezultat_eduida = re.match(regex_eduid, unos_eduida)

if rezultat_emaila:
    print("Email je ispravan.")
else:
    print("Email nije ispravan.")

if rezultat_eduida:
    print("EduId je ispravan.")
else:
    print("EduId nije ispravan.")