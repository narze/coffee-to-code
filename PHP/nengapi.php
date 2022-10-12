<?php
    $coffee = "Coffee";
    $code = '';

    foreach (str_split($coffee) as $char) {
        $char = ord($char) == 102 ? chr(100) : $char;
        $code = str_replace('dde', 'd', $code);
        $code = $code.$char;
    }

    echo $coffee.' is '.$code;
?>