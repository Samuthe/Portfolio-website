let form = document.getElementById('form');
let formSubmitBtn = document.getElementById('form-submit');
let formName = document.getElementById('form-name');
let formEmail = document.getElementById('form-email');
let formMessage = document.getElementById('form-message');
let recaptchaContainer = document.getElementById('recaptcha');
let recaptchaInput = document.getElementById('recaptcha-input');
let recaptchaError = document.getElementById('recaptcha-error');
let recaptchaCompleted = false;
let resendMessage = true;

// Function to get CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

// reCAPTCHA Callback when completed
function RecaptchaCallback(token) {
    recaptchaCompleted = true;
    recaptchaInput.value = token;  // Store the token in the hidden input field
    recaptchaError.innerHTML = ''; // Clear previous errors
}

// reCAPTCHA Expired Callback
function expiredRecaptchaCallback() {
    recaptchaCompleted = false;
    recaptchaInput.value = ''; // Clear token
    recaptchaError.innerHTML = `<small class="error-text"><i class="fa fa-exclamation-triangle"></i> reCAPTCHA expired, please verify again!</small>`;
}

// Show reCAPTCHA when user starts typing
if (formName && formEmail && formMessage) {
    formName.addEventListener("input", () => recaptchaContainer.style.display = 'block');
    formEmail.addEventListener("input", () => recaptchaContainer.style.display = 'block');
    formMessage.addEventListener("input", () => recaptchaContainer.style.display = 'block');
}

// Handle form submission
if (formSubmitBtn) {
    formSubmitBtn.addEventListener('click', (e) => {
        e.preventDefault();  // Prevent default submission
        resendMessage = false;

        // Check if reCAPTCHA is completed
        if (!recaptchaCompleted || recaptchaInput.value === '') {
            recaptchaContainer.style.display = 'block';
            recaptchaError.innerHTML = `<small class="error-text"><i class="fa fa-exclamation-triangle"></i> Please complete the reCAPTCHA!</small>`;
            resendMessage = true;
            return;
        }

        // Prepare form data
        let formData = new FormData();
        formData.append('name', formName.value);
        formData.append('email', formEmail.value);
        formData.append('message', formMessage.value);
        formData.append('recaptcha', recaptchaInput.value);  // Send reCAPTCHA token

        // Send data via Fetch API
        fetch("/", {
            method: "POST",
            body: formData,
            credentials: 'same-origin',
            headers: {
                "X-CSRFToken": csrftoken
            }
        })
        .then(response => response.json())
        .then(data => {
            function toggleValidation(element, isValid) {
                element.parentElement.classList.remove('has-danger', 'has-success');
                element.parentElement.classList.add(isValid ? 'has-success' : 'has-danger');
            }

            function clearInputs() {
                formName.value = '';
                formEmail.value = '';
                formMessage.value = '';
                formName.parentElement.classList.remove('has-danger', 'has-success');
                formEmail.parentElement.classList.remove('has-danger', 'has-success');
                formMessage.parentElement.classList.remove('has-danger', 'has-success');
                recaptchaError.innerHTML = '';
                document.getElementById('name-error').innerHTML = '';
                document.getElementById('email-error').innerHTML = '';
                document.getElementById('message-error').innerHTML = '';
            }

            if (data.success) {
                clearInputs();
                resendMessage = false;
                document.getElementById('modal-toggle').click();
                grecaptcha.reset();  // Reset reCAPTCHA
                recaptchaContainer.style.display = 'none';
            } else {
                resendMessage = true;
                toggleValidation(formName, !data.errors.name);
                toggleValidation(formEmail, !data.errors.email);
                toggleValidation(formMessage, !data.errors.message);
                document.getElementById('name-error').innerHTML = data.errors.name ? `<small class="error-text"><i class="fa fa-exclamation-triangle"></i> ${data.errors.name}</small>` : '';
                document.getElementById('email-error').innerHTML = data.errors.email ? `<small class="error-text"><i class="fa fa-exclamation-triangle"></i> ${data.errors.email}</small>` : '';
                document.getElementById('message-error').innerHTML = data.errors.message ? `<small class="error-text"><i class="fa fa-exclamation-triangle"></i> ${data.errors.message}</small>` : '';
            }
        })
        .catch(error => {
            console.error("Error submitting form:", error);
            resendMessage = true;
        });
    });
}
