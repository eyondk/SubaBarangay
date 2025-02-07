function openModal() {
    const modalContainer = document.getElementById('registermodal');
    modalContainer.classList.add('visible'); // Show the Register Organization modal using the 'visible' class
}

function closeRegisterModal() {
    const modalContainer = document.getElementById('registermodal');
    modalContainer.classList.remove('visible'); // Remove 'visible' class to hide the modal
}

function closeModals() {
    // Close both modals
    const registermodal = document.getElementById('registermodal');
    const successModal = document.getElementById('successModal');
    
    // Hide modals by removing 'visible' class or setting display to 'none'
    registermodal.classList.remove('visible');
    successModal.style.display = 'none';

    // Re-enable the "Add" button functionality
    const addButton = document.querySelector('.add-btn');
    addButton.disabled = false;


}

function showSuccessModal() {
    document.getElementById("successModal").style.display = "block";
}

function closeModal() {
    // Close the success modal
    document.getElementById("successModal").style.display = "none"; 
}

