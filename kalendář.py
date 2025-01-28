import calendar

year = input("Zadej rok: ")
try:
    year = int(year)
except ValueError:
    print("To co jste napsal není číslo")
    exit()

month = input("Zadej měsíc: ")
try:
    month = int(month)
except ValueError:
    print("To co jste napsal není číslo")
    exit()

print(calendar.month(year, month))