<?php
session_start(); // Open session

//Storing the value of the captcha
$captcha = rand(100,9999);
$_SESSION['captcha'] = $captcha;
extract($_SESSION);

//Create IMG:
//#imagecreatetruecolor() : need 2 arguments : width & height
$dimensionImage = imagecreatetruecolor(45,24);

#imagecolorallocate(): 4 arguments : the image in which I work, value of red, green and blue component.
$background = imagecolorallocate($dimensionImage,22,86,165);
$texteColor = imagecolorallocate($dimensionImage,255,255,255);

#imagefill() :
imagefill($dimensionImage,0,0,$background);

#imagestring() :
imagestring($dimensionImage,5,5,5,$captcha,$texteColor);
header("Content-type: image/png");
imagepng($dimensionImage);
imagedestroy($dimensionImage);

?>
