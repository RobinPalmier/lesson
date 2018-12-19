#La function input() permet de saisir des informations
#input() retourne se que l'utilisateur à saisie
#Si on ne met pas input() dans une variable, l'ensemble du contenue saisie sera perdu !

produit = input("Choissez un produit : ")

prixHT = input("Entrer un prix HT : ") #On demande à l'utilisateur d'entrer un prix.

# La valeur de prixHT est une string, car la valeur a été enregistré entre des balises de textes.

prixHT = int(prixHT) #On convertit le prix en integer avec la fonction int()
prixTTC = prixHT + (prixHT * 20/100) #On effectue l'opération
print("prix TTC =", prixTTC) #On affiche le résultat de prix TTC

