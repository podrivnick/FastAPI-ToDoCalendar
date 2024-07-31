function showNotification(message) {
    const notification = document.getElementById('notification__message_registration');
    notification.innerText = message;
    notification.classList.remove('hidden__registration');
    notification.style.display = 'block';

    // Скрываем уведомление через 5 секунд
    setTimeout(() => {
        notification.style.display = 'none';
    }, 5000);
}
