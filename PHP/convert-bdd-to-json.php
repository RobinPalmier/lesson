<?php

// [ Database conversion to Json file
/* |  */   $reqSQL = $pdo->prepare('SELECT * FROM table');
/* |  */   $reqSQL->execute();
/* |  */   $data = $reqSQL->fetchAll(); 
/* |  */   $reqSQL->closeCursor();
/* |  */   $jsonEncode = json_encode($data);
/* |  */   $file = 'asset/file.json';
/* |  */   $fileJson = fopen($file, 'w+');
/* |  */   fwrite($fileJson, $jsonEncode);
/* |  */   fclose($fileJson); 
// [ End of the conversion of the database into a Json file 

?>