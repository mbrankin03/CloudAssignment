<?php
echo "Test Script Starting\n";
// require('index.php');

$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, "http://localhost:2000/?item_1=item1&item_2=item2&item_3=item3&item_4=item4&attendance_1=33&attendance_2=22&attendance_3=44&attendance_4=55");
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_HEADER, 0);

$server_output = curl_exec($ch);

$myJSON = json_decode($server_output);

$error = $myJSON->error;
$max_answer = $myJSON->max;
$min_answer = $myJSON->min;
$answer = $myJSON->answer;


echo "Test No error should be returned\n";
if ($error == false) {
    echo "Test Passed\n";
} else {
    echo "Test Failed\n";
    exit(1);
}

echo "Test Correct answer should be returned\n";
if ($max_answer == "item4 - 55" && $min_answer == "item2 - 22") {
    echo "Test Passed\n";
    exit(0);
} else {
    echo "Test Failed\n";
    exit(1);
}
