package com.cours4;

public class Main {

    public static void main(String[] args) {

        // Pour définir un tableau, on met les crochets au niveau du type.
        String[] names = {"Robin","Guillaume","Damien","François","Marianne","Bertrand","Louise","guillaume"};
        // Type[] nomDuTableau = {arg};

        if(names[1].equalsIgnoreCase(names[7])){
            // equalsIgnoreCase() permet de vérifier une égalité parfaite sans prendre en compte la casse.
            System.out.println("Les noms sont identiques");
        }

        int[] number = {12,6,21,2,17,10};

        // tab.length permet d'obtenir la longueur du tableau.
        int calcul = (number[0] + number[3]) / number.length;


        // Tableau multidimensionnel :

        // Quand il s'agit de tableaux multidimensionnel, nous devons doubler les [].
        int[][] chiffres = {
                {
                    7, 8, 9
                },
                {
                    4, 5, 6
                },
                {
                    1, 2, 3
                }
        };

        System.out.println(chiffres[0][2]); // Retourne 9.
        System.out.println(chiffres[2][0]); // Retourne 1.
        System.out.println(chiffres[1][1]); // Retourne 5.

        // Convertir une chaîne de caractères en tableau :

        String prenom = "Guillaume, Dany, Robin, Celine, Mélanie, Jean, Simon, Iman";

        // Le split() permet de couper la chaîne de caractères à partir d'un délimiteur.
        // Dans ce cas, on utilise la ",".
        String[] recupPrenom = prenom.split(",");

        System.out.println(recupPrenom[1]); // Retourne "Dany".
        System.out.println(recupPrenom[3]); // Retourne "Celine".
        System.out.println(recupPrenom[recupPrenom.length-1]); // Retourne "Iman".

        // tab[tab.length-1] Permet de récupérer le dernier élément du tableau.

    }
}
