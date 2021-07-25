#!/bin/php
<?php
/* $cookie = base64_decode('ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw='); */
/* ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D */

/* $secret = 'qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jq'; */
$secret = 'qw8J';


function xor_encrypt($in) {
    global $secret;
    /* $key = '{"showpassword":"no","bgcolor":"#ffffff"}'; */
    $key = $secret;
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
        $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

$data = array("showpassword"=>"yes", "bgcolor"=>"#ffffff");

$cookie = base64_encode(xor_encrypt(json_encode($data)));
print($cookie . "\n");
?>
