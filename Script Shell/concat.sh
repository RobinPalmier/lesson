#!/bin/bash
if(($# != 2))
then echo "Il y a $# paramètres. Veuillez entrer exactement 2 paramètres."
else
echo $1 $2
echo "Il y a $# paramètres"
fi
