<?php
	$con = mysqli_connect("sql.server.com", "username", "password");
		if(!$con){
			die('Could not connect: '.mysqli_error($con));
		}
		mysqli_select_db($con,"rjb57");
		$sql="SELECT * FROM rjb57.lightSeq where display='y';";
		$result = mysqli_query($con,$sql);
		mysqli_close($con);
		$name = mysqli_fetch_row($result);
		$displayfile = $name[0];
		if($displayfile=="morse" || $displayfile=="countdown" || $displayfile=="custom"){
			$displayfile = $displayfile." ".$name[2];
		}
		echo $displayfile;
?>
