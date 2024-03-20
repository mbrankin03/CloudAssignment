<?php
echo "Test Script Starting\n";
require('functions.inc.php');

$items = array("item1","item2","item3","item4","item5");
$attendances = array(10,20,30,40,50);

// Sort the items by attendance
$item_attendances = getSortedAttendance($items, $attendances);

// Expected sorted items with their attendances
$expected_sorted_items = array(
  array("item"=>"item5","attendance"=>50),
  array("item"=>"item4","attendance"=>40),
  array("item"=>"item3","attendance"=>30),
  array("item"=>"item2","attendance"=>20),
  array("item"=>"item1","attendance"=>10)
);

echo "Sorted Items: ";
print_r($item_attendances);

echo "Expected Sorted Items: ";
print_r($expected_sorted_items);

// Check if the sorted items are as expected
if ($item_attendances == $expected_sorted_items) {
  echo "Sort Test Passed\n";
} else {
  echo "Sort Test Failed\n";
}
echo "Test Script Ending\n";
