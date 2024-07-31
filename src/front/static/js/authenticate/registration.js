document.getElementById('form_register_user_').addEventListener('submit', async function(event) {
        event.preventDefault(); // Предотвращаем отправку формы по умолчанию

        const form = event.target;
        const formData = new FormData(form);
        const jsonData = Object.fromEntries(formData.entries());
        const is_two_password_equals = is_two_passwords_equal(jsonData.password, jsonData.password2)

        if (is_two_password_equals) {
            delete jsonData.password2
            console.log(JSON.stringify(jsonData))
            try {
                const response = await fetch('/registration/register', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(jsonData),
                });

                const result = await response.json();

                if (response.ok) {
                    close_modal__popup__register('modalRegistr')
                    showNotification(REGISTERED_PROFILE)
                    console.log('Registration successful', result);
                } else {
                    console.error('Registration failed', result);
                }
            } catch (error) {
                console.error('Error:', error);
            }
        } else {
            console.log('password not equal')
        }
    });

