document.getElementById('form_add_calendar_user_').addEventListener("submit",
    async function(event) {
        event.preventDefault()

        const form = event.target;
        const formBaseData = new FormData(form);
        const jsonData = Object.fromEntries(formBaseData.entries());

        let user_token = jsonData.token

        const requestData = {
            user_token: user_token
        };
        const formData = new URLSearchParams();
        formData.append('user_token', user_token);

        console.log(requestData)
        console.log(JSON.stringify(requestData))

        const url = new URL(API_ADD_CALENDAR, window.location.origin);
        url.searchParams.append('user_token', user_token);

        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    "access-control-allow-credentials": "true",
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({}),
            });

            if (response.ok) {
                window.location.reload();
                showNotification(ADDED_ANOTHER_USER)
                console.log('Registration successful', result);
            } else {
                console.error('Registration failed', result);
            }
        }
        catch (error) {
            console.log(error)
        }
    }
);

