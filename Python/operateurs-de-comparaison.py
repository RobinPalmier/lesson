"""
Opérateurs de comparaison :     ==  : (égal à)
                                !=  : (différent de)
                                <   : (plus petit que)
                                >   : (plus grand que)
                                <=  : (plus petit ou égal à)
                                >=  : (plus grand ou égal à)
                                
Conditions multiples :          and         : (ET)
                                or          : (OU)
                                in / not in : (DANS / PAS DANS)
                                
Mots clés des conditions :      if / elif / else



Règles d'indentation :

> Le resultat du else ou du if doit avoir une tabulation avant de débuter, sinon il ne sera pas pris en compte dans la condition et sera traîté à part.

"""

#Conditions Python :
identifiant = "Robin"
mot_de_passe = "admin123"

print('Interface de connexion')

user_id = input("Entrez votre identifiant : ")
user_password = input("Entrez votre mot de passe : ")

if user_id == identifiant and user_password == mot_de_passe:
    print("Vous êtes connectés, bienvenue", user_id)
