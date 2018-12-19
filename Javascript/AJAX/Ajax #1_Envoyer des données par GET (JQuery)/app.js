$(document).ready(function(){
    var button = $('#button'); // On sélectionne le bouton.
    
    // Aux cliques, on exécute la fonction :
    $(button).on('click', function(){
        // On stock dans la variable monTexte, le texte qui figure sur le bouton.
        var monTexte = $(this).text();
        // On envoie avec la fonction JQuery $.get
        // Au script 'target.php',
        // Puis on envoie la variable text qui aura pour valeur 'monTexte',
        // function(data) va récupérer les données qui vont revenir du serveur.
        $.get('target.php', {text: monTexte}, function(data){
            // On affiche les données retournées dans l'ID reponse.
            document.getElementById('reponse').innerHTML = data;
            
        });
    });
});