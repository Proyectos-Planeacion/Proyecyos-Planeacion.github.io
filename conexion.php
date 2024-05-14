<?php
$mysqli = new mysqli("127.0.0.1", "root", "", "bases_sunshine");

if ($mysqli->connect_errno) {
    echo "Fallo al conectar a MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
} else {
    echo '<script>console.log("Conexion exitosa");</script>';
}



?>


