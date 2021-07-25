<?php
class Exa {
    public $some_var;

    function __destruct() {
        system("echo {$this->some_var} > a.txt");
    }
}

$user_data = unserialize($_GET['data']);

echo "Page loaded";
?>
