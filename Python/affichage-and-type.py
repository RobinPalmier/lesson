#coding:utf-8
# #coding:utf-8 = Forcer l'encodage en UTF-8

#Function d'affichage :
print("Hello World")

#Commentaire en Python :
#   # = commentaire 1 ligne.
#   ''' ''' ou """ """ = Commentaire multiligne

#Variable Python :

"""
Nommer une variable : doit commencer par une lettre ou un underscore
                      ne pas contenir de caractères spéciaux
                      ne pas contenir d'espace
                      utiliser des underscores (_)
                      
Type standards      : entier numérique (int)
                      nombre flottant (float)
                      chaine de caractères (str)
                      booléen (bool)
                      
Fonctions           : print()   -> afficher à l'écran
                      input()   -> insérer du texte
                      type()    -> retourne le type d'une donnée(variable etc.)
                      str.format() -> formater une chaine
"""

agePersonne = 20 #Entier numérique (int)
agePersonne2 = "20" #Chaine de caractères (str)
agePersonne3 = 120.34 #Nombre flottant (float)
agePersonne4 = True #Booléen (bool)

#La function type() permet d'afficher le type de la phrase
print(type(agePersonne))
print(type(agePersonne2))

print(agePersonne)

## ------------------------------------------------------------------- ##

name = "Robin" #Je déclare ma variable
print("Bonjour " + name) #J'affiche une string contenant ma variable


texte = "l'age de la personne est {} et le prix de la personne est de {} euros."
#La methode format() permet d'ajouter les valeurs dans l'ordre dans les "{}"
print(texte.format(agePersonne, agePersonne3))