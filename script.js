function showSignup() {
    document.getElementById("login-form").style.display = "none";
    document.getElementById("signup-form").style.display = "flex";
    document.getElementById("btn").style.left = "110px"; // Adjust button position
}

function showLogin() {
    document.getElementById("signup-form").style.display = "none";
    document.getElementById("login-form").style.display = "flex";
    document.getElementById("btn").style.left = "0"; // Adjust button position
}

// Initialize to show login form by default
document.addEventListener("DOMContentLoaded", function() {
    showLogin();
});