#Conditions Python avec else :
lettre_hasard = "e"

if lettre_hasard not in "aeiouy":
    print("C'est une consonne")
else:
    print("C'est un voyelle")
    
## ------------------------------------------------------------------- ##

#Conditions Python avec elif :
age = 24

if age == 18:
    print("Tu viens d'être majeur")
elif age == 50:
    print("Tu viens d'avoir 50 ans")
elif age == 60:
    print("Tu viens d'avoir 60 ans")
else:
    print("Tu as", age, "ans")

## ------------------------------------------------------------------- ##

jeu_charge = True #True = vrai (=1)

#Il est inutile d'utiliser des opérateurs de comparaison dans le cas des booléens car le if vérifie si "jeu_charge == True".

#Si la condition aurait été "if not jeu_charge", dans ce cas il vérifie si "jeu_charge == False".

if jeu_charge:
    print("Le jeu est en marche")
else:
    print("Le jeu a été quitté")
    
## ------------------------------------------------------------------- ##

#Conditions avec fourchette de valeurs
age = input("Quel âge as-tu ?")
age = int(age)

#Avec une fourchette de valeurs, on dit que age doit être compris entre 0 et 100 inclus.
#Ecriture plus propre.
if 0 < age <= 100:
    print("L'age est validé")
else:
    print("L'age est incorrect")
