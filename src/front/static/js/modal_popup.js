document.addEventListener('DOMContentLoaded', function () {
    function setupModal(openBtnId, modalId, closeBtnClass) {
        if (openBtnId && modalId) {
            const openBtn = document.getElementById(openBtnId);
            const modal = document.getElementById(modalId);
            const closeBtn = modal.querySelector('.' + closeBtnClass);

            openBtn.addEventListener('click', function () {
                modal.classList.add('modal__popup__login__visible');
            });

            closeBtn.addEventListener('click', function () {
                modal.classList.remove('modal__popup__login__visible');
            });

            window.addEventListener('click', function (event) {
                if (event.target == modal) {
                    modal.classList.remove('modal__popup__login__visible');
                }
            });
        } else {
            console.error(`Element not found for modal setup: {openBtnId: '${openBtnId}', modalId: '${modalId}'`);
        }
    }
    let is_authenticated = document.querySelector('.userIsAuthenticatedInput').value

    console.log(is_authenticated.value)

    if (is_authenticated === 'true') {
        setupModal('openModalAddNewCalendar', 'modalAddNewCalendar', 'close_popup_packet_btn');
    } else {
        setupModal('openModalLoginBtn', 'modalLogin', 'close_popup_packet_btn');
        setupModal('openModalRegisterBtn', 'modalRegistr', 'close_popup_packet_btn');
    }
});

