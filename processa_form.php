<?php
// Configurações do banco de dados
$servername = "localhost"; // Geralmente é "localhost" para um servidor local
$username = "root"; // Substitua por seu nome de usuário do MySQL
$password = "root"; // Substitua pela sua senha do MySQL
$dbname = "projeto_rad_python"; // Substitua pelo nome do seu banco de dados

// Criando a conexão
$conn = new mysqli($servername, $username, $password, $dbname);

// Verifica se houve erro na conexão
if ($conn->connect_error) {
    die("Falha na conexão: " . $conn->connect_error);
}

// Recebe os dados do formulário
$nome = $_POST["nome"];
$email = $_POST["email"];
$curso = $_POST["curso"];
$idade = $_POST["idade"];

// Cria a consulta SQL para inserir os dados
$sql = "INSERT INTO alunos (nome, email, curso, idade) VALUES ('$nome', '$email', '$curso', $idade)";

// Executa a consulta
if ($conn->query($sql) === TRUE) {
    echo "Novo registro criado com sucesso!";
} else {
    echo "Erro: " . $sql . "<br>" . $conn->error;
}

// Fecha a conexão
$conn->close();
?>