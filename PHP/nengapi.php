<?php
    $coffee = "Coffee";
    $code = '';

    foreach (str_split($coffee) as $char) {
        $char = ord($char) == 102 ? chr(100) : $char;
        $code = $code.$char;
    }
    echo str_replace('dde', 'd', $code);

?>