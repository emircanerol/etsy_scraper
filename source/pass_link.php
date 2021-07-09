<?php
$input = $_POST["name"];
echo "input: $input</br>";

$command = escapeshellcmd("python get_infos.py -a '".$input."' ");
# escapeshellarg(string $input): string
$output = shell_exec($command);
echo $output;
echo "</br>end";
?>
