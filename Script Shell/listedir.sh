#!/bin/sh
liste_file=$(ls)
repo_courant=$(pwd)
echo "####### Fichiers dans /boot/"
for entree in $liste_file
do
if [ -f "$entree" ]; then
echo "$entree"
fi
done

echo "####### Repertoires dans /boot/"
for entree in $liste_file
do
if [ -d "$entree" ]; then
echo "$entree"
fi
done
