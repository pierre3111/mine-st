// static/js/registration.js
document.addEventListener('DOMContentLoaded', function () {
  const registerButton = document.getElementById('register-button');
  const registrationForm = document.getElementById('registration-form');

  registerButton.addEventListener('click', function () {
    registrationForm.style.display = 'block';
  });

  window.addEventListener('click', function (event) {
    if (event.target === registrationForm) {
      registrationForm.style.display = 'none';
    }
  });

  const form = document.getElementById('registration-form-content');
  form.addEventListener('submit', function (event) {
    event.preventDefault();
    if (validateForm()) {
      // Form is valid, submit the data to the server (you can implement this part with AJAX or fetch API)
      alert('Registration successful!'); // Replace this with actual form submission logic
      form.reset(); // Reset the form after successful submission
    }
  });

  function validateForm() {
    // Your form validation logic here
    // ...
  }
});

// In registration.js or any other JavaScript file you use
document.addEventListener('DOMContentLoaded', function () {
  const registerButton = document.getElementById('register-button');
  const modal = document.querySelector('.modal');

  registerButton.addEventListener('click', function () {
    modal.style.display = 'block';
  });

  window.addEventListener('click', function (event) {
    if (event.target === modal) {
      modal.style.display = 'none';
    }
  });
});
