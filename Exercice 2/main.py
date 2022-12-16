m = int(input("Saisir le numéro du mois : "))

if not 12 >= m >= 0:
    print("Le numéro du mois doit être compris entre 1 et 12")
else:
    if m == 2:
        print("Le mois numéro", m, "est février et il a 28 jours")
    elif m in [4, 6, 9, 11]:
        print("Le mois numéro", m, "est un mois de 30 jours")
    else:
        print("Le mois numéro", m, "est un mois de 31 jours")

