<?php
	$con = mysqli_connect("sql.server.come", "username", "password");
	if(!$con){
		die('Could not connect: '.mysqli_error($con));
	}
	mysqli_select_db($con,"rjb57");
	$sql="SELECT * FROM rjb57.lightSeq where display='y';";
	$result = mysqli_query($con,$sql);
	$sql="SELECT * FROM rjb57.lightSeq;";
	$allfiles = mysqli_query($con,$sql);
	mysqli_close($con);
	$name = mysqli_fetch_row($result);
	$displayfile = $name[0];
	if($displayfile=="morse" || $displayfile=="countdown" || $displayfile=="custom"){
		$displayfile = $displayfile." ".$name[2];
	}
	
	/*$formcode = "<form style='margin-top:100px;margin-left:20px' action='' method='POST'>
				<select name='sequence'>";*/
	while($pdf=mysqli_fetch_row($allfiles)){
		if($pdf[1]=='y'){
			$formcode .= "<option selected value='".$pdf[0]."'>".$pdf[0]."</option>";
		}
		else{$formcode .= "<option value='".$pdf[0]."'>".$pdf[0]."</option>";}
	}
		
?>
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>LED Picker</title>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
		<script src="jquery-3.3.1.min.js"></script>
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
		<script src="jscolor.js"></script>
	</head>
	<body>
	<?php
		if($_SERVER["REQUEST_METHOD"] == "POST"){			
			$con = mysqli_connect("sql.server.come", "username", "password");
			if (!$con) {
				die('Could not connect: ' . mysqli_error($con));	
			}
			mysqli_select_db($con,"rjb57");
				
				if($_POST['submit']=="Show Sequence"){
					$sql="UPDATE rjb57.lightSeq SET display='n';";
					mysqli_query($con,$sql);
					$chosenfile = mysqli_real_escape_string($con,$_POST['sequence']);
					if($chosenfile=="countdown" || $chosenfile=="morse"){
						$message = mysqli_real_escape_string($con,$_POST['msg']);
						$sql="UPDATE lightSeq SET display='y',value='$message' WHERE sequence='$chosenfile';";
						mysqli_query($con,$sql);
					}
					elseif ($chosenfile=="custom"){
						$color = mysqli_real_escape_string($con,$_POST['color']);
						$sql="UPDATE lightSeq SET display='y',value='$color' WHERE sequence='$chosenfile';";
						mysqli_query($con,$sql);
					}
					else{
						$sql="UPDATE lightSeq SET display='y' WHERE sequence='$chosenfile';"; //HARD CODED SEQUENCE NAMES ONLY
						mysqli_query($con,$sql);
					}
					
				}
			mysqli_close($con);
			echo "<script> window.location.replace('https://web.njit.edu/~rjb57/RPi/ledPicker.php'); </script>";
		}
		?>
		<div id="serverData"><?=$displayfile; ?></div>
		<div class="container">
			<form style='margin-top:100px;margin-left:20px' action='' method='POST'>
				<label for="seq">Pick which light sequence to show:</label>
				<select class="form-control" name='sequence' id="seq">
				<?=$formcode; ?>
				</select><br id="break">
				<input id="chosenColor" required name="color" style="display: none;"><br>
				<button id='colorpick' class='jscolor {valueElement:"chosenColor"} btn btn-secondary' style="display: none;">Pick Color</button><br>
				<button type='submit' class='btn btn-lg btn-primary d-flex justify-content-center' name='submit' value='Show Sequence'>Show Sequence</button>
			</form>
		</div>
	</body>
	
	<script>
		function update(val) {
			//document.getElementById('rect').style.backgroundColor = '#' + jscolor
			console.log(val);
		}
		function addInput() {
						if ($("#msgInput").length){//($('#seq').val() != "morse" || $('#seq').val() != "countdown" || $('#seq').val() != "custom") && 
							console.log("removing seq")
							$("#msgInput").remove();
						}
						else if (document.getElementById("colorpick").style.display=="block") {
							document.getElementById("colorpick").style.display = "none";
							document.getElementById("chosenColor").style.display = "none";
						}
						if ($('#seq').val() == "morse") {
							$("#break").after("<input id='msgInput' required type='text' name='msg' placeholder='Message'>");
							//console.log("adding seq")
						}
						else if($('#seq').val() == "countdown"){
							$("#break").after("<input id='msgInput' required type='number' min='0' value='10' name='msg'>");
						}
						else if($('#seq').val() == "custom"){
							document.getElementById("colorpick").style.display = "block";
							document.getElementById("chosenColor").style.display = "block";
							document.getElementById("chosenColor").value = "<?= $name[2] ?>";
						}
					}
	
		$(document).ready(function () {
			$('#seq').change(function () {
				if ($("#msgInput").length){//($('#seq').val() != "morse" || $('#seq').val() != "countdown" || $('#seq').val() != "custom") && 
					console.log("removing seq")
					$("#msgInput").remove();
				}
				else if (document.getElementById("colorpick").style.display=="block") {
					document.getElementById("colorpick").style.display = "none";
					document.getElementById("chosenColor").style.display = "none";
				}
				if ($('#seq').val() == "morse") {
					$("#break").after("<input id='msgInput' required type='text' name='msg' placeholder='Message'>");
					//console.log("adding seq")
				}
				else if($('#seq').val() == "countdown"){
					$("#break").after("<input id='msgInput' required type='number' min='0' value='10' name='msg'>");
				}
				else if($('#seq').val() == "custom"){
					document.getElementById("colorpick").style.display = "block";
					document.getElementById("chosenColor").style.display = "block";
				}
			});
		});
		/*if(typeof(EventSource)!=="undefined") {
			///create an object, passing it the name and location of the server side script
			//var eSource = new EventSource("send_sse.php");
			///detect message receipt
			//eSource.onmessage = function(event) {
				///write the received data to the page
				//document.getElementById("serverData").innerHTML = event.data;
			}
		}
		else {
			//document.getElementById("serverData").innerHTML="Whoops! Your browser doesn't receive server-sent events.";
		}*/
		addInput();
		
	</script>
</html>
