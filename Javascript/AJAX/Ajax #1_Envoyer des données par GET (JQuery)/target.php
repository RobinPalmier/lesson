<?php
// On vérifie si des données ont été envoyé par $_GET.
if(!empty($_GET)){
    // Si $_GET n'est pas vide, on stock dans la variable $text le texte.
    $text = strip_tags($_GET['text']);
    // On stock la longueur de la chaîne de caractères $text.
    $length = strlen($text);
    // On renvoie au client la longueur de la chaîne de caractères.
    echo "Le texte comporte {$length} caractères.";
}
?>