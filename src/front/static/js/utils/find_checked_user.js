function getSelectedUser() {
    const radios = document.getElementsByName('calendar_user__access');
    let selectedValue;
    for (const radio of radios) {
        if (radio.checked) {selectedValue = radio.value;
            break;
        }
    }
    return selectedValue
}
