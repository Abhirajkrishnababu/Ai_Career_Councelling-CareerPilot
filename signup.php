<?php
// Connect to the MySQL database
$conn = new mysqli('localhost', 'root', '', 'career_roadmap');

// Check for connection errors
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get form data
$username = $_POST['username'];
$email = $_POST['email'];
$password = password_hash($_POST['password'], PASSWORD_DEFAULT); // Securely hash the password

// Insert the user data into the database
$sql = "INSERT INTO users (username, email, password) VALUES ('$username', '$email', '$password')";
if ($conn->query($sql) === TRUE) {
    echo "Sign-up successful!";
} else {
    echo "Error: " . $conn->error;
}

$conn->close();
?>
