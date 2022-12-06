m = int(input("Saisir le numéro du mois : "))

if m < 1 or m > 12:
    print("Le numéro du mois doit être compris entre 1 et 12")
else:
    if m == 2:
        print("Le mois numéro", m, "est février et il a 28 jours")
    elif m == 4 or m == 6 or m == 9 or m == 11:
        print("Le mois numéro", m, "est un mois de 30 jours")
    else:
        print("Le mois numéro", m, "est un mois de 31 jours")

