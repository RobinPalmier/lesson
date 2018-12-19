// On sélectionne les éléments ayant la class carre.
var blockClass = document.querySelectorAll('.carre');
// On sélectionne les éléments d'affichage de résultat.
var resultat = document.querySelectorAll('.result');

for (var x in blockClass){
    blockClass[x].onclick = function(){
        // On définit l'opérateur this.
        var blockClick = this;
        // On affiche le résultat.
        resultat[0].innerHTML = "Vous avez cliqué sur le carré " + this.getAttribute('value')+".";
    }
}

// On sélectionne l'élément parent.
var blockId = document.getElementById('block');

// On écoute le click de l'évènement parent.
blockId.addEventListener('click', function(event){
    // On affiche le résultat.
    resultat[1].innerHTML = "Vous avez cliqué sur le carré " + event.target.id + ".";
})