package com.cours5;

public class Main {

    public static void main(String[] args) {

        // Boucle for :
        String sautDeLigne = System.getProperty("line.separator"); // Permet de faire un saut de ligne.

        for(int i = 0; i < 100; i++){
            System.out.print("Ceci est le tour n°" + i + sautDeLigne); // Retourne 100x le Systeme.out.print().
        }


        // Boucle foreach :
        String[] names = {"Louise", "Robin", "Jordan", "John", "Karim", "Stephen"};

        // for(Type nom : LeTableauQuonVeutRecuperer)
        for(String prenom : names){
            System.out.println(prenom); // Retourne tous les prénoms du tableau.
        }


        // Calculer une moyenne avec la boucle foreach :
        int[] notes = {7,8,9,10,2};
        int calcul = 0;

        for(int moyenneNote : notes){
            calcul = calcul + moyenneNote;
        }
        System.out.println("La moyenne des notes est de " + (calcul / notes.length)); // Retourne 7.


        // Boucle While :
        int i = 0;
        while (i != 7){
            System.out.println("Je teste la boucle while");
            i++; // Le i++ permet d'incrémenter i à chaque tour de boucle. Cela permet de ne pas tomber dans une boucle infinie.
        }
    }
}
