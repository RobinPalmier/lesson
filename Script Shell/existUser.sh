
#!/bin/bash
if [ $# -eq 1 ]
then
dir="/etc/passwd"
awk -v var=$1 -F : '{
if(var==$1 || var==$3)
print "Cet utilisateur nommé "$1" existe avec comme UID : "$3}'$dir
else
echo "Erreur, vous devez rentrer un utilisateur ou un UID."
fi
