<?php
if (isset($_COOKIE["u"]) && $_COOKIE["u"] === 'hacky mchack') {
	echo $flag = '<div>__TEMPLATE__</div>';
}
?>