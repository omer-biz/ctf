<?php
$fd = fopen("file.txt", "a+");
fwrite($fd, "hello\n");
fclose($fd);
?>
