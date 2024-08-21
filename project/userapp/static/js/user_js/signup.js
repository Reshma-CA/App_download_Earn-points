document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const usernameField = document.getElementById('username');
    const emailField = document.getElementById('email');
    const passwordField = document.getElementById('password');
    const confirmPasswordField = document.getElementById('confirm-password');

    form.addEventListener('submit', function(event) {
        let isValid = true;

        // Clear previous error messages
        document.querySelectorAll('.error-message').forEach(el => el.textContent = '');

        // Check if fields are not empty
        if (!usernameField.value.trim()) {
            isValid = false;
            document.getElementById('username-error').textContent = 'Username is required.';
        }
        if (!emailField.value.trim()) {
            isValid = false;
            document.getElementById('email-error').textContent = 'Email is required.';
        }
        if (!passwordField.value.trim()) {
            isValid = false;
            document.getElementById('password-error').textContent = 'Password is required.';
        }
        if (!confirmPasswordField.value.trim()) {
            isValid = false;
            document.getElementById('confirm-password-error').textContent = 'Please confirm your password.';
        }

        // Validate passwords match
        if (passwordField.value !== confirmPasswordField.value) {
            isValid = false;
            document.getElementById('confirm-password-error').textContent = 'Passwords do not match.';
        }

        // Validate email format
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (emailField.value && !emailPattern.test(emailField.value)) {
            isValid = false;
            document.getElementById('email-error').textContent = 'Invalid email format.';
        }

        if (!isValid) {
            event.preventDefault(); // Prevent form submission
        }
    });
});
