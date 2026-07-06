document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const u = document.getElementById('username').value;
    const p = document.getElementById('password').value;
    const msg = document.getElementById('message');

    // Send the data to our local backend bridge
    fetch('http://127.0.0.1:5000/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username: u, password: p })
    })
    .then(response => response.json())
    .then(data => {
        msg.style.color = "green";
        msg.innerText = "🚀 SUCCESS: " + data.message;
    })
    .catch(error => {
        msg.style.color = "red";
        msg.innerText = "❌ ERROR: Could not reach backend bridge.";
        console.error(error);
    });
});