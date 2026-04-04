<!doctype html>
<html>
	<head>
		<title>This is the title of the webpage!</title>
	</head>
	<body>
		<?php
			$message='<p>I only answer to King-Kong!</p>';
			if (isset($_SERVER['HTTP_USER_AGENT'])) {
				if ($_SERVER['HTTP_USER_AGENT'] == 'King-Kong') {
					$message='<p>SSS_CTF{godzilla_got_nothing_on_me}</p>\n';
				}
			}
			echo $message . "\n";
		?>
	</body>
</html>
