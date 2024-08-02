document.getElementById('logout_link__').addEventListener('click', async function() {
    try {
        const response = await fetch(API_LOGOUT, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            credentials: 'include' // включение куки в запрос
        });

        if (response.ok) {
            // Перезагрузка страницы после успешного logout
            window.location.reload();
        } else {
            console.error('Logout failed');
        }
    } catch (error) {
        console.error('Error:', error);
    }
});
