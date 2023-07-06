import re

regex = r"^m.*[0-5].*\s+.*s$"

string = input("Unesite string: ")

if re.match(regex, string):
    print("Podudaranje pronađeno!")
else:
    print("Podudaranje nije pronađeno.")