<?php
//php file for file uploading
$target_dir="uploads/";
$target_file=$target_dir.basename($_FILES["fileupl"]["name"]);
$uploadOk=1;
$imageFileType=strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
if(isset($POST["submit"])){
	$check=getimagesize($_FILES["fileupl"]["tmp_name"]);
	if($check!==false){
		echo "file is an image_".$check["mime"].".";
	    $uploadOk=1;
	}else{
		echo "File is not image.";
		$uploadOk=0;
	}
}
//to check if file already exists
if(file_exists($target_file)){
	echo "Sorry the file already exits.";
	$uploadOk=0;
	
}
//to check file size
if($_FILES["fileupl"]["size"]>4000000){
	echo "Sorry the file is too large.";
	$uploadOk=0;
}
//allow certain file formats
if($imageFileType!="jpg" && $imageFileType!="png" && $imageFileType!="jpeg" && $imageFileType!="gif"){
	echo "Sorry only jpg/png/gif file accepted!! ";
}else{
	if(move_uploaded_file($_FILES["fileupl"]["tmp_name"],$target_file)){
		echo "The file".basename($_FILES["fileupl"]["tmp_name"])." has been uploaded.";
	}else{
		echo "Sorry, there was an error";
	}
}

echo "<br><br>";
echo $_FILES["fileupl"]["name"]."<br>";
echo $_FILES["fileupl"]["size"]."<br>";
echo $_FILES["fileupl"]["tmp_name"]."<br>";
echo $_FILES["fileupl"]["type"]."<br>";


?>