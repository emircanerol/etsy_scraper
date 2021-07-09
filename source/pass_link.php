<?php
# $fp = fopen('connect.txt', 'w') or die("<br>Unable to open file!");
# fwrite($fp ,$_POST["name"]);
# fclose($fp);
$input = $_POST["name"];
echo $input;
$command = escapeshellcmd('python get_infos.py "-a" "$input"');
$output = shell_exec($command);
echo $output;
echo "</br>end";
?>