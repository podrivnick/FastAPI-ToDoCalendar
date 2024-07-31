function close_modal__popup__register(id_modal_popup) {
    modal_popup = document.getElementById(id_modal_popup)

    if (modal_popup.classList.contains('modal__popup__login__visible')) {
        modal_popup.classList.remove('modal__popup__login__visible')
    }
}
