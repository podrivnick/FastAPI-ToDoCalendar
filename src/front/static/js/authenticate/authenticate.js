document.getElementById('form_login__users').addEventListener('submit', async function(event) {
    event.preventDefault(); // Предотвращаем отправку формы по умолчанию

    const form = event.target;
    const formDataBase = new FormData(form);
    const jsonData = Object.fromEntries(formDataBase.entries());

    console.log(jsonData)

    let login_username = jsonData.username
    let login_password = jsonData.password

    const formData = new URLSearchParams();
    formData.append('username', login_username);
    formData.append('password', login_password);

    try {
        const response = await fetch('/login/jwt/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: formData.toString(),
        });

        if (response.ok) {
            window.location.reload();
            showNotification(ENTERED_TO_PROFILE)
            console.log('Registration successful', result);
        } else {
            console.error('Registration failed', result);
        }
    } catch (error) {
        console.error('Error:', error);
    }
});