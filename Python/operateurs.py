"""
Opérateurs en Python : + = addition
                       - = soustraction
                       * = multiplication
                       / = division
                       % = modulo (reste d'une division Euclidienne)
"""

calcul = 5 / 2
calcul = int(calcul) #La fonction int(), permet d'assurer une bonne conversion

print("Resultat = ", calcul) #On affiche le résultat de calcul

## ------------------------------------------------------------------- ##

niveauPersonnage = input("Niveau de départ ? ") #L'utilisateur entre un chiffre
niveauPersonnage = int(niveauPersonnage) #On convertit en integer

print("Niveau de personnage", niveauPersonnage) #On affiche le nom du personnage

print("combat réussi, tu gagnes un niveau !") 
#Le combat est réussi, donc le personnage prend 1 niveau
 
niveauPersonnage = niveauPersonnage + 1 
#On rajoute un niveau à notre personnage

print("Niveau de personnage", niveauPersonnage) 
#On affiche le nouveau niveau de notre personnage