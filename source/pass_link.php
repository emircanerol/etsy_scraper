<?php
$input = $_POST["name"];
echo $input;
$command = escapeshellcmd('python get_infos.py "-a" "$input"');
$output = shell_exec($command);
echo $output;
echo "</br>end";
?>
