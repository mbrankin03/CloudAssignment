<?php
header("Access-Control-Allow-Origin: *");
header("Content-type: application/json");
require('functions.inc.php');

$output = array(
	"error" => false,
  "items" => "",
	"attendance" => 0,
	"max_item" => "",
	"min_item" => ""
);

$item_1 = $_REQUEST['item_1'];
$item_2 = $_REQUEST['item_2'];
$item_3 = $_REQUEST['item_3'];
$item_4 = $_REQUEST['item_4'];
$attendance_1 = $_REQUEST['attendance_1']; // 33
$attendance_2 = $_REQUEST['attendance_2']; // 22
$attendance_3 = $_REQUEST['attendance_3']; // 44 
$attendance_4 = $_REQUEST['attendance_4']; // 55


function isValidString($str) {
    // check if string is set, is a string, and is not numeric
    return isset($str) && is_string($str) && !is_numeric($str) && strlen($str) > 0;
}

function isValidInt($int) {
	return isset($int) && is_numeric($int) && !empty(trim($int)) && $int > 0;
}

// check if items 1-4 are strings
if (!isValidString($item_1) || !isValidString($item_2) || !isValidString($item_3) || !isValidString($item_4)) {
	$outputError = array(
		"error" => true,
		"status" => 400,
		"message"=> "Invalid input. Please check your input and try again. Items 1-4 must be string values."
		);
	echo json_encode($outputError);
	exit();
}

// check if attendances 1-4 are integers
if (!isValidInt($attendance_1)|| !isValidInt($attendance_2) || !isValidInt($attendance_3) || !isValidInt($attendance_4)) {
	$outputError = array(
		"error" => true,
		"status" => 400,
		"message"=> "Invalid input. Please check your input and try again. Attendances 1-4 must be numeric values."
		);
	echo json_encode($outputError);
	exit();
}

if ($attendance_1 > 33 || $attendance_2 > 22 || $attendance_3 > 44 || $attendance_4 > 55) {
	$outputError = array(
		"error" => true,
		"status" => 400,
		"message"=> "Invalid input. Please check your input and try again. Attendances 1-4 must be within the range of 1-33, 1-22, 1-44, and 1-55 respectively."
		);
	echo json_encode($outputError);
	exit();
}

$items = array($item_1,$item_2,$item_3,$item_4);
$attendances = array($attendance_1,$attendance_2,$attendance_3,$attendance_4);

$max_min_items=getMaxMin($items, $attendances);

$output['items']=$items;
$output['attendance']=$attendances;
$output['max_item']=$max_min_items[0];
$output['min_item']=$max_min_items[1];

echo json_encode($output);
exit();
