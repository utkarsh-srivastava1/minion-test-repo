const form = document.getElementById('login-form');
const errorMessage = document.getElementById('error-message');
const usernameRegex = /^[a-zA-Z0-9_]{3,16}$/;
const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
const csrfToken = document.getElementById('csrf-token');

// Generate a random CSRF token
fetch('/api/generate-csrf-token', {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json'
    }
})
.then(response => response.json())
.then(data => {
    csrfToken.value = data.csrfToken;
})
.catch(error => {
    console.error('Error:', error);
});

form.addEventListener('submit', (e) => {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    if (username === '' || password === '') {
        errorMessage.innerText = 'Please fill in all fields.';
    } else if (!usernameRegex.test(username)) {
        errorMessage.innerText = 'Username should be between 3 and 16 characters long and contain only letters, numbers, and underscores.';
    } else if (!passwordRegex.test(password)) {
        errorMessage.innerText = 'Password should be at least 8 characters long, contain at least one lowercase letter, one uppercase letter, one number, and one special character.';
    } else {
        // Add your login logic here
        fetch('https://your-website.com/api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRF-Token': csrfToken.value
            },
            body: JSON.stringify({ username, password })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                console.log(`Login successful for ${username}`);
                errorMessage.innerText = '';
            } else {
                errorMessage.innerText = 'Invalid username or password.';
            }
        })
        .catch(error => {
            console.error('Error:', error);
            errorMessage.innerText = 'An error occurred while logging in.';
        });
    }
});