<?php
header("Content-type: text/xml");
echo "<?xml version='1.0' encoding='UTF-8'?>";
echo "<Response>";
echo "<Say voice='man'>Hello, you have reached the ambulance. Do not panic. Kindly provide us with your details so that we may reach you faster.</Say>";
echo "<Pause length = '1'/>";
echo "<Say voice='man'>Name of the patient ?</Say>";
echo "<Pause length='1'/>";
echo "<Say voice='man'>Name of the caller ?</Say>";
echo "<Pause length='1'/>";
echo "<Say voice='man'>Provide the address where the ambulance must reach.</Say>";
echo "<Pause length='300'/>";
echo "<Say voice='man'>We will send an ambulance immediately. Thank you.</Say>";
echo "<Pause length='300'/>";
echo "</Response>";
?>