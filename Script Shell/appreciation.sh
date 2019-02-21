#!/bin/bash
echo "Entrer votre note :"
read note

if [ $note -ge 16 ] && [ $note -le 20 ]
then
echo "Très bien"
elif [ $note -ge 14 ] && [ $note -lt 16 ]
then
echo "Bien"
elif [ $note -ge 12 ] && [ $note -lt 14 ]
then
echo "Assez bien"
elif [ $note -ge 10 ] && [ $note -lt 12 ]
then
echo "Moyen"
elif [ $note -ge 0 ] && [ $note -lt 10 ]
then
echo "Insuffisant"
else
echo "La note n'est pas comprise entre 0 et 20"
fi
