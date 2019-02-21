#!/bin/bash
echo "Type du fichier :"
if [ -f$1 ]
then
	echo "$1 est un fichier ordinaire"
fi
if [ -d$1 ]
then
	echo "$1 est un répertoire"
fi
echo "Permissions :"
if [ -r$1 ]
then
	echo "$1 peut être lu."
fi
if [ -w$1 ]
then
	echo "$1 peut être écrit."
fi
if [ -x$1 ]
then
	echo "$1 peut être exécuté."
fi
