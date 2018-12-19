<?php
// On définit le décalage horaire par défaut de toutes les fonctions date et heure
date_default_timezone_set ("Europe/Berlin");

// Sert à afficher toutes les erreurs. 
// À commenter en prod.
error_reporting(E_ALL);

// Forcer l'affichage des erreurs en contournant la configuration du fichier php.ini
// À commenter en prod.
ini_set('display_errors', 'on'); 


/* Connexion à la BDD : */

// Configuration de base :
$bddOptions = array(
    // On force l'encodage en utf8.
    PDO::MYSQL_ATTR_INIT_COMMAND    => "SET NAMES utf8",
    // On récupère les résultats sous forme de tableau associatif.
    PDO::ATTR_DEFAULT_FETCH_MODE     => PDO::FETCH_ASSOC,
    // On affiche les erreurs de type warning. 
    // À commenter en prod.
    PDO::ATTR_ERRMODE               => PDO::ERRMODE_WARNING
);

// Le champ de droite est à modifié !
define('TYPEBDD','mysql'); // Type de la base de données.
define('HOST', 'domaine'); // Domaine du serveur.
define('USER','username'); // Nom de l'utilisateur.
define('PASSWORD','password'); // Mot de passe.
define('DBNAME','dbname'); // Nom de la base de données.

try{ 
    // On essaie de se connecter à la base de donné.
    $pdo = new PDO(TYPEBDD . ':host=' . HOST . ';dbname=' . DBNAME,USER,PASSWORD,$bddOptions);
}
catch(Exception $e){
    // Indique une erreur si on ne peut pas se connecter à la base de données.
    die('Error BDD : ' . $e ->getMessage());
}

// Adapte le HTTP de façon automatique. 
// 'htdocs/racine_site/' <- À commenter lors de la mise en ligne.
define('URL', $_SERVER['REQUEST_SCHEME'] . '://' . $_SERVER['HTTP_HOST'] . 'htdocs/racine_site/');
?>