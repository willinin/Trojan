<?php

if ($_SERVER["HTTP_REFERER"] == "") {
	exit("<!--Hi-->");
}

require "./config.php";
require_once LIB_PATH . "/kernel.php";
$aid = explode(",", $_GET["adsid"]);
$pid = explode(",", $_GET["planid"]);
if ($aid && $pid) {
	$i = 0;

	foreach ((array) $aid as $a ) {
		$data = array("views" => (int) $_GET["sep"], "day" => DAYS, "planid" => (int) $pid[$i], "adsid" => (int) $a, "zoneid" => (int) $_GET["zoneid"], "plantype" => $_GET["plantype"], "siteid" => (int) $_GET["siteid"], "uid" => (int) $_GET["uid"], "adtplid" => (int) $_GET["adtplid"]);
		dr("api/api_stats.update_stats", $data);
		$i++;
	}ssss
}

?>
