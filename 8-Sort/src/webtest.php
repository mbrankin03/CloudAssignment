<?php
echo "Test Script Starting\n";
// require('index.php');

$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, "http://localhost:2000/?item_1=item1&item_2=item2&item_3=item3&item_4=item4&attendance_1=33&attendance_2=22&attendance_3=44&attendance_4=55");
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_HEADER, 0) ;

$server_output = curl_exec($ch);

$myJSON = json_decode($server_output);

$error = $myJSON->error;
$sorted = $myJSON->sorted_attendance;

$expected_sorted_attendance = array(
  array("item"=>"item4","attendance"=>55),
  array("item"=>"item3","attendance"=>44),
  array("item"=>"item1","attendance"=>33),
  array("item"=>"item2","attendance"=>22)
);
$sorted = $myJSON->sorted_attendance;

// Initialize an empty array to store the new format
$sortedAsArray = [];

foreach ($sorted as $obj) {
    // Convert each stdClass object to an associative array
    $sortedAsArray[] = [
        'item' => $obj->item,
        'attendance' => $obj->attendance,
    ];
}

echo "Test No error should be returned\n";
if ($error == false) {
    echo "Test Passed\n";
} else {
    echo "Test Failed\n";
    exit(1);
}

echo "Test Correct answer should be returned\n";
if ($sortedAsArray == $expected_sorted_attendance) {
    echo "Test Passed\n";
    exit(0);
} else {
    echo "Test Failed\n";
    exit(1);
}






