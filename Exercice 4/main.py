colors = ['B', 'R', 'N', 'V', 'J', 'O', 'G']

import random
formula = ''.join(random.choices(colors, k=5))

attempts = 0

while True:
  guess = input("Proposez une formule de 5 couleurs : ")
  
  if guess == formula:
    break
  
  attempts += 1
  
  well_placed = sum(1 for g, f in zip(guess, formula) if g == f)
  misplaced = sum(1 for g in guess if g in formula) - well_placed
  
  print(f"Il y a {well_placed} couleur(s) bien placée(s) et {misplaced} couleur(s) mal placée(s).")

if attempts <= 5:
  print("Bravo ! Vous avez trouvé en moins de 5 essais.")
elif attempts <= 10:
  print("Correct ! Vous avez trouvé en moins de 10 essais.")
else:
  print("Décevant ! Vous avez mis plus de 10 essais pour trouver.")

print(f"Vous avez utilisé {attempts} essai(s).")