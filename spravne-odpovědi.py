def vyhodnot_odpovedi(spravne_odpovedi, odpovedi_uzivatele):
    celkem_otazek = len(spravne_odpovedi)
    spravne = sum(1 for spravna, uzivatel in zip(spravne_odpovedi, odpovedi_uzivatele)
                   if spravna.strip().lower() == uzivatel.strip().lower())
    
    uspesnost = (spravne / celkem_otazek) * 100 if celkem_otazek > 0 else 0
    
    print(f"Uživatel odpověděl správně na {spravne} z {celkem_otazek} otázek. Úspěšnost: {uspesnost:.1f}%.")

spravne_odpovedi = ["Praha", "Brno", "Liberec", "Ostrava", "Olomouc"]
odpovedi_uzivatele = ["praha", "Brno", "Liberec", "Olomouc", "Ostrava"]

vyhodnot_odpovedi(spravne_odpovedi, odpovedi_uzivatele)
