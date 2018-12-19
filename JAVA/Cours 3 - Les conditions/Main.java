package com.cours3;

public class Main {

    public static void main(String[] args) {

        // Vérifications de majorité :
        byte age = 11;

        if(age >= 18){
            System.out.println("Vous êtes majeur.");
        }
        else if(age < 0){
            System.out.println("La personne n'est pas encore né.");
        }
        else{
            System.out.println("Vous n'êtes pas majeur.");
        }

        // Le switch :

        switch (age){
            case 10: // Le case équivaut au else if.
                System.out.println("La personne à 10 ans.");
                break; // Le break permet de casser la boucle.

            case 11:
                System.out.println("La personne à 11 ans");
                break;

                // Dans le cas ou on est pas sur 10 ni sur 11, on met quelque chose par défaut.
                default: System.out.println("Rien n'a ajouté....");
        }

    }
}
