<?php
function log_str($str) {
	$log_file = fopen("/volume1/web/tving/sjva_log.txt", "a");  
	fwrite($log_file, $str."\r\n");  
	fclose($log_file);  
}

function attack_log($str) {
	$log_file = fopen("/volume1/web/attack.txt", "a");  
	fwrite($log_file, $str."\r\n");  
	fclose($log_file);  
}

function get_html() {
	$url = func_get_arg(0);
	$headers = func_get_arg(1);
	$query = (func_num_args() == 3) ? func_get_arg(2) : null;
	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, $url);
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
	curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_HEADER, 0);
	//curl_setopt($ch, CURLOPT_COOKIEJAR, 'cookies.txt');
	//curl_setopt($ch, CURLOPT_COOKIEFILE, 'cookies.txt');
	if ( $query != null) {
		curl_setopt($ch, CURLOPT_POST, 1);
		curl_setopt($ch, CURLOPT_POSTFIELDS, $query);
	}
	$data = curl_exec($ch);
	return $data;
}	

$url = $_POST['url'];
$cookie = $_POST['cookie'];

log_str($url);
log_str($cookie);

$headers = array('Cookie: '.$cookie.';');
$data = get_html($url, $headers);
header('Content-type: application/json');
echo $data;

#echo json_encode($array);
	
?> 
