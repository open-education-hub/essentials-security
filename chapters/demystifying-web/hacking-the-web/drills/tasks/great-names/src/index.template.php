<?php
session_start();

setcookie("marco", "?", time() + 86400);

if (!isset($_SESSION['step'])) {
	$_SESSION['step'] = 0;
} else {
	if (isset($_COOKIE['marco']) && $_COOKIE['marco'] === 'polo') {
		$_SESSION['step'] = 1;
		setcookie("fernando", "?");
	}
	if (isset($_COOKIE['fernando']) && $_COOKIE['fernando'] === 'magellan') {
		$_SESSION['step'] = 2;
		setcookie("christopher", "?");
	}
	if (isset($_COOKIE['christopher']) && $_COOKIE['christopher'] === 'columbus') {
		$_SESSION['step'] = 3;
		setcookie("GG", "Now look closer in the document body");
	} 
}

if ($_SESSION['step'] == 3) {
	echo '<!--__TEMPLATE__-->';
}
?>
