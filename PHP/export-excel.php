<?php
header('Content-Type: text/csv');
header('Content-Disposition: attachment; filename="file_excel.csv"');
try{
    $pdoCSV = new PDO('mysql:host=[host];dbname=[database name]','[user]','[password]');
    $pdoCSV->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_WARNING);
    $pdoCSV->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE,PDO::FETCH_OBJ);
}catch(PDOException $e){
    echo 'Connection Failed';
}

$req = $pdoCSV->prepare('SELECT column1,column2,column3 FROM table');
$req->execute();
$data = $req->fetchAll();
?>"Last Name";"First Name";"Email"<?php


foreach($data as $d){
    echo "\n{$d->column1};{$d->column2};{$d->column3};";
}
?>