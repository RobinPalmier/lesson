package com.cours6;

public class Main {

    public static void main(String[] args) {
	// Accessibilité :
        // public : Accessible partout.
        // private : Accessible uniquement dans la Class.
        // protected : Accessible uniquement dans la Class en question et les classes qui vont s'en servir.

        // La fonction se lance lorsqu'on exécute le programme.
        sendMessage(); // Retourne "Test".
        messageArg("Hello World"); // Retourne "Hello World".

        int money = 2300;
        int priceTelephone = 800;
        boolean hasPhone = false;
        System.out.println(getResult(money,priceTelephone,hasPhone)); // Retourne le résultat de la condition de la fonction getResult() et la différence entre le portefeuille et la somme du téléphone.

    }

    // static permet de désigner un accès direct à la fonction.
    private static void sendMessage() {
        System.out.println("Test");
    }

    private static void messageArg(String message){
        System.out.println("Le message est : " + message);
    }

    private static int getResult(int money, int priceTelephone, boolean hasPhone){
        if(money >= priceTelephone && !hasPhone){
            System.out.println("Tu peux acheter le téléphone");
        }
        else{
            System.out.println("Tu n'as pas assez d'argent pour acheter ou tu as déjà un téléphone.");
        }

        // Renvoie la différence entre les deux valeurs.
        return money - priceTelephone;
    }
}
