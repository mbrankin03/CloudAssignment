<?php
echo "Test Script Starting\n";
require('functions.inc.php');

$items = array("item1","item2","item3","item4","item5");
$attendances = array(10,20,30,40,50);

$expected_max = "item5 - 50";
$expected_min = "item1 - 10";

list($max_item,$min_item) = getMaxMin($items,$attendances);

if ($max_item == $expected_max) {
  echo "Max Test Passed\n";
} else {
  echo "Max Test Failed\n";
}

if ($min_item == $expected_min) {
  echo "Min Test Passed\n";
} else {
  echo "Min Test Failed\n";
}

echo "Test Script Ending\n";