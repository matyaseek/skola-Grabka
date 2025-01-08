from datetime import datetime
# Zjištění aktuálního data a času
a = datetime.now().year
# Zde to po nás bude chtít zadat rok narození
cislo = input("Zadejte rok narození: ")
try:
    cislo = float(cislo)  
    #Zde to odečte rok narození od aktuálního roku
    vysledek = a - cislo
    #Zde to vypíše věk
    print(f"Věk je: {vysledek}")
    #Zde to napíše error pokud zadaný údaj není číslo
except ValueError:
    print("To co jste napsal není číslo")
