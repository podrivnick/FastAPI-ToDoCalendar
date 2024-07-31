document.addEventListener('DOMContentLoaded', function () {
    function setupModal(openBtnId, modalId, closeBtnClass) {
        const openBtn = document.getElementById(openBtnId);
        const modal = document.getElementById(modalId);
        const closeBtn = modal.querySelector('.' + closeBtnClass);
        const copyBtn = document.getElementById('copyBtn');
        const tokenInput = document.getElementById('tokenInput');

        openBtn.addEventListener('click', function () {
            modal.classList.add('modal_visible');
        });

        closeBtn.addEventListener('click', function () {
            modal.classList.remove('modal_visible');
        });

        window.addEventListener('click', function (event) {
            if (event.target == modal) {
                modal.classList.remove('modal_visible');
            }
        });
    }
    copyBtn.addEventListener('click', function () {
        tokenInput.select();
        document.execCommand('copy');
        alert('Token copied to clipboard');
    });
    setupModal('openModalBtn', 'modal__profile', 'close_popup_packet_btn');
});
