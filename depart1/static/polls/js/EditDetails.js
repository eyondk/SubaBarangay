// START: EDIT TABS AND CONTENT JS
const tabs = document.querySelectorAll('.tab-edit');
const tabContents = document.querySelectorAll('.tab-edit-content');

tabs.forEach(tab => {
    tab.addEventListener('click', () => {
        tabs.forEach(t => t.classList.remove('active'));
        tabContents.forEach(content => content.classList.remove('active'));

        tab.classList.add('active');
        const tabKey = tab.getAttribute('data-tab');
        document.getElementById(`tab-content-${tabKey}`).classList.add('active');
    });
});

// END: EDIT TABS AND CONTENT JS


// CONFIRAMTION IF SUCCESS/UNSUCCESSFUL PAG ADD SA HH MEMBER
function openConfirmUnSuccModal() {
    document.getElementById('confirmationUn-SuccessModal').style.display = 'flex';
}

function closeConfirmUnSuccModal() {
    document.getElementById('confirmationUn-SuccessModal').style.display = 'none';
}