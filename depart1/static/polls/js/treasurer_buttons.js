function openUpdateOrgModal() {
    document.getElementById("updateOrgModal").style.display = "flex";
}

function openAddOrgModal() {
    document.getElementById("addOrgModal").style.display = "flex";
}

function closeUpdateOrgModal() {
    document.getElementById("updateOrgModal").style.display = "none";
}

function closeAddOrgModal() {
    document.getElementById("addOrgModal").style.display = "none";
}

// Success Modal Functions
function openSuccessModal(message) {
    document.getElementById("successMessage").innerText = message; // Set dynamic message
    document.getElementById("successModal").style.display = "flex";
}

function closeSuccessModal() {
    document.getElementById("successModal").style.display = "none";
}

// Handle form submissions
document.getElementById("updateOrgForm").addEventListener("submit", function(event) {
    event.preventDefault(); 
    closeUpdateOrgModal();
    openSuccessModal("Organization has been successfully updated.");
});

document.getElementById("addOrgForm").addEventListener("submit", function(event) {
    event.preventDefault(); 
    closeAddOrgModal();
    openSuccessModal("Organization has been successfully added.");
});


// Confirm delete function
function confirmDelete() {
    closeConfModal(); // Close the confirmation modal
    openSuccessModal("Organization for this resident has been successfully deleted"); // Show success modal
}
