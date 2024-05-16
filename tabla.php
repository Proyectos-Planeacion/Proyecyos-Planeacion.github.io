<?php
@include_once('conexion.php');



?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Tabla</title>
</head>

<body>
    
    <h1>Flor En Transito</h1>
    <table>
        <tr>
            <th>Producto</th>
            <th>Color</th>
            <th>Grado</th>
            <th>Flor Por Ingresar</th>


        </tr>
        <?php
        while ($row = $result->fetch_assoc()) {
            echo "<tr>";
            echo "<td>" . $row['Producto'] . "</td>";
            echo "<td>" . $row['Color'] . "</td>";
            echo "<td>" . $row['Grado'] . "</td>";
            echo "<td>" . $row['Flor Por Ingresar'] . "</td>";
            echo "</tr>";



        }
        ?>
    </table>
</body>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Poppins', sans-serif;
}

table {
    width: 100%;
    border-collapse: collapse;
    border-spacing: 0;
    font-family: 'Poppins', sans-serif;
}

th, td {
    padding: 12px 15px;
    text-align: left;
    border-bottom: 1px solid #ddd;
    border-radius: 8px;
}

th {
    background-color: #4220e9;
    color: white;
}

tr:nth-child(even) {
    background-color: #252525;
}

tr:hover {
    background-color: #1e1e1e;
}

td {
    color: #ddd;
}



body {
    background-color: #252525;
    font-family: 'Poppins', sans-serif;
}

table {
    margin: 20px auto;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
}

th, td {
    transition: all 0.3s;
}

th:hover {
    background-color: #2c2c2c;
}

tr:nth-child(even) td {
    background-color: #1e1e1e;
}

tr:nth-child(even):hover td {
    background-color: #1a1a1a;
}

h1 {
    color: white;
    text-align: center; 
}
</style>


